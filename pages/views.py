from django.shortcuts import render
import csv
from .algo import lms_algo
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from wsgiref.util import FileWrapper
from .models import Data
import os
# Create your views here.
im1 = ""
im2 = ""
def home(request):
    context = {
            'mse':0,
            'mae':0,
            'err':0,
            'img1':" ",
            'img2':" "
    }
    if(request.POST):
        formdata = request.POST
        file = request.FILES['file']
        v1,v2,v3,img1,img2 = lms_algo(file)
        v1 = round(v1,2)
        v2 = round(v2,2)
        v3 = round(v3,2)
        #img_1 = "media/"+img1
        #img_2 = "media/"+img2
        if(v1 and v2 and v3 and img1 and img2):
            context = {
            'mse':v1,
            'mae':v2,
            'err':v3,
            'img1':img1,
            'img2':img2
            }
            print(context['img1'])
            im1 = img1
            im2 = img2

        #fs = default_storage()
        #fs.save(file.name,file)
    return render(request,'home/home.html',context)

