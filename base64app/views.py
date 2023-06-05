import base64
from io import BytesIO
import os
from rest_framework import status
from .serializers import FileSerializer,ImageSerializer,ImageRequestSerializer
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .models import Image
from pathlib import Path

#  file image add
@api_view(['POST'])
def FileView(request):
    try:
      if request.method == 'POST':
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return JsonResponse(file_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({"Message" : e.args , "code":500})
    

# request add image
@api_view(['POST'])   
def ImageView(request):
    try:
      if request.method == 'POST':
        image_serializer = ImageSerializer(data=request.data)
        if image_serializer.is_valid():
            image_serializer.save() 
            return JsonResponse(image_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({"Message" : e.args , "code":500})
    
@api_view(['PUT'])
def imageupdate(request,id):
    try:
      if request.method == 'PUT':
        id_image = Image.objects.filter(id=id)
        if id_image:
            update_image = Image.objects.get(id=id)
            if update_image:
                image_serializer = ImageSerializer(update_image,data=request.data)
                if image_serializer.is_valid():
                    old_image = Image.objects.filter(id=id).values('image')
                    for j in old_image:
                        data = j["image"]
                    BASE_DIR = Path(__file__).resolve().parent.parent
                    location = os.path.join(BASE_DIR, "media")
                    path = os.path.join(location, data)  
                    os.remove(path)
                    image_serializer.save()
                    return JsonResponse(image_serializer.data, status=status.HTTP_201_CREATED) 
                return JsonResponse(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
           return JsonResponse({"Message":"ID not found"})
    except Exception as e:
        return JsonResponse({"Message" : e.args, "code":500})
    
@api_view(['DELETE'])
def imagedelete(request,id):
    try:
      if request.method == 'DELETE':
        image = Image.objects.filter(id=id)
        if image:
            old_image = Image.objects.filter(id=id).values('image')
            for j in old_image:
                data = j["image"]
            BASE_DIR = Path(__file__).resolve().parent.parent
            location = os.path.join(BASE_DIR, "media")
            path = os.path.join(location, data)  
            os.remove(path)
            image.delete()
            return JsonResponse({"Message":"Image deleted successfully"}, status=status.HTTP_200_OK)
        return JsonResponse({"Message":"Image not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({"Message" : e.args, "code":500}) 
    
# def convert_to_base64(file_path):
#     with open(file_path, "rb") as file:
#         encoded_string = base64.b64encode(file.read()).decode("utf-8")
#         print(encoded_string)
#     return encoded_string

@api_view(['POST'])
def RequestImageView(request):
    try:
        if request.method == 'POST':
            image_serializer = ImageRequestSerializer(request.data)
            # print(image_serializer)
            image_data  = request.data['image']
            print(image_data)
            unsafe_encode = base64.b64encode(image_data)
            print(unsafe_encode)
            safe_encode = base64.urlsafe_b64encode(image_data)
            return JsonResponse({"Message":"Image Add successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
      
        return JsonResponse({"Message" : e.args, "code":500})
