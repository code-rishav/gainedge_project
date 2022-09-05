from django.shortcuts import render
import csv
from .algo import lms_algo, output
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from wsgiref.util import FileWrapper
from .models import Data
# Create your views here.
def home(request):
    if(request.POST):
        formdata = request.POST
        name = formdata['name']
        mu = formdata['number']
        file = request.FILES['file']
        '''fs = FileSystemStorage()
        fs.save(file.name,file)'''

        #lms_algo()
        output(file)
        
        #fs = default_storage()
        #fs.save(file.name,file)
    return render(request,'home/home.html')
