from django.shortcuts import render, redirect
from .forms import UploadFileForm
from styleTrans import main
from django.http import HttpResponse


# Create your views here.
def menu(request):
    
    return render(request, 'index.html')

def upload(request):
    
    if request.method == 'GET':
       print('get already')
       
    return render(request, 'upload.html')

def ChooseStyle(request):
  
   print(request.FILES['file'].name)
   input_file_path = request.FILES['file'].name
   request.session['input_file_path'] = input_file_path

   '''
   form = UploadFileForm(request.POST, request.FILES)
   
   if form.is_valid():
         form.save()''' 
   
   return render(request, 'choose_style.html', {'file_path': 'uploads/'+input_file_path})

def chosen(request):
   # print(request.POST['selected_image_url'])
   trans_style_url = request.POST['selected_image_url']
   start_index = trans_style_url.find('/static/')

   if start_index != -1:
      substring = trans_style_url[start_index:]  
      trans_style_path = substring
      print(trans_style_path)

      input_file_path = request.session.get('input_file_path')
   
   print(input_file_path, trans_style_path)
   main(input_file_path, trans_style_path)
   
   output_file_name = 'transfered'+input_file_path
   #transfer(input_file_path, trans_style_path)
   return render(request, 'choose_style.html', {'file_path': 'transfered/'+output_file_name})