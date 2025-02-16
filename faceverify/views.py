from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.conf import settings

import os
import json
from .check import KycForm
from deepface import DeepFace

# Create your views here.
# def index(request):
#     return HttpResponse('Hello World!')

def kyc_image_view(request):
    if request.method == 'POST':
        form = KycForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace", "GhostFaceNet"]
            path1 = os.path.join(settings.MEDIA_ROOT, 'photo_image.jpg')
            path2 = os.path.join(settings.MEDIA_ROOT, 'id_image.jpg')

            result = DeepFace.verify(
                img1_path = path1, img2_path = path2,
                model_name = models[6], threshold=0.8
            )
            response = HttpResponse(json.dumps(result), content_type='application/json')
            return response
    else:
        form = KycForm()

    return render(request, 'upload.html', {'form': form})


def success(request):
    return HttpResponse('Successfully uploaded!')
