from django.shortcuts import render, redirect
from .forms import UploadFileForm

# Create your views here.
def menu(request):
    
    return render(request, 'index.html')

def upload(request):
    
    if request.method == 'GET':
       print('get already')

    if request.method == 'POST':
       print('post already\n',request.POST)
       print(request.FILES)

       form = UploadFileForm(request.POST, request.FILES)

       if form.is_valid():
            form.save()
            
        
    return render(request, 'upload.html')
