from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog,Tieup,Contact
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from random import randint
from PIL import Image
import os


# Create your views here.
def index(request):
    objects = Tieup.objects.all().order_by('-id')
    count = objects.count()
    mod = count % 12
    if count < 36:
        variable = 36
    else :
        if mod == 0:
            variable = count
        else :
            v1 = round((count / 12),0) 
            v2 = int(v1) + 1
            variable = v2 * 12

    old_data = []

    for i in range(variable):
        found = False
        for key, value in enumerate(objects):
            if i == key:
                old_data.append({
                    'pos': key,
                    'name': value.name,
                    'message': value.message,
                    'profile': value.profile
                })
                found = True
                break

        if not found:
            old_data.append({
                'pos': '',
                'name': '',
                'message': '',
                'profile': ''
            })

    new_count = len(old_data)
    path = request.path
    #print(objects)
    data = {
            'objects' : objects,
            'mod' :  mod,
            'old_data' :  old_data,
            'path': path,
            'new_count' :  new_count,
    }
    
    return render(request, "index.html", data)
    
def show(request):

    objects = Contact.objects.all()

    return render(request, "show.html",{'data': objects})

#contact form
def contact(request):
    if request.method == "POST":
        en=Contact(name=request.POST.get('name'),email=request.POST.get('email'),
            subject=request.POST.get('subject'),message=request.POST.get('message'))
        if request.POST.get('name') != '' and  request.POST.get('email') !='' and request.POST.get('subject') !='' and request.POST.get('message') !='':
            en.save()
        messages.success(request, "Thank you for Contacting Us!")
    else :
        messages.warning(request, "Sorry for the inconvience!")
    #return HttpResponse(res)
    # print(request.POST)
    # objects = Blog.objects.raw("Select * from users");
    #return render(request, "index.html")
    return redirect('home')
    #return HttpResponseRedirect('/home#contact')

def resize_image(input_path, output_path, new_width, new_height):
    try:
    # Open the image
        image = Image.open(input_path)
        
    # Resize the image
        resized_image = image.resize((new_width, new_height))
        
    # Save the resized image to the specified output path
        resized_image.save(output_path)
        print("Image resized successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def tieup(request):
    if request.method == "POST":
        # uploaded_image = request.FILES['image']
        # name = 'photo_' +  str(randint(1000, 9999)) + '.' + uploaded_image.name.split('.')[-1]
        # static_path = settings.STATIC_ROOT
        # destination = static_path + "/media/uploads"
        # save_path = os.path.join(destination, name)

        # input_image_path = save_path
        # output_image_path = static_path + "/media/resized/" + name
        # new_width = 70
        # new_height = 70


        # # Create the destination directory if it doesn't exist
        # os.makedirs(destination, exist_ok=True)

        # with open(save_path, 'wb+') as destination_file:
        #     for chunk in uploaded_image.chunks():
        #         destination_file.write(chunk)

        # resize_image(input_image_path, output_image_path, new_width, new_height)

        # uploaded_image = request.FILES['image']
        # destination = os.path.join(settings.MEDIA_URL, 'uploaded_images')
        # save_path = os.path.join(destination, uploaded_image.name)
        # with open(save_path, 'wb+') as destination:
        #     for chunk in uploaded_image.chunks():
        #         destination.write(chunk)
        # fs = FileSystemStorage(location='media/uploaded_images/')
        # fs.save(uploaded_image.name, uploaded_image)
        en=Tieup(name=request.POST.get('name').title(),email=request.POST.get('email'),message = request.POST.get('message'), mobile = request.POST.get('mobile'), 
            profile = request.POST.get('profile'), instagram_id = request.POST.get('instagram'))
        if request.POST.get('name') != '' and  request.POST.get('email') !='' and  request.POST.get('message') !='' and  request.POST.get('mobile') !='' :
            mobile_number = request.POST.get('mobile')
            tieup_records = Tieup.objects.filter(mobile=mobile_number)
            if tieup_records.count() == 0 :
                en.save()
                message = "Thank you "+request.POST.get('name').title()+" for Tie Up!"
                messages.success(request, message)
                # if os.path.exists(save_path):
                #     os.remove(save_path)
            else : 
                message = "Sorry "+request.POST.get('name').title()+" this mobile number alredy Tie Up!"
                messages.error(request, message)
    else :
        messages.warning(request, "Sorry for the inconvience!")
    #return HttpResponse(res)
    # print(request.POST)
    # objects = Blog.objects.raw("Select * from users");
    #return render(request, "index.html")
    return redirect('home')
    #return HttpResponseRedirect('/home#contact')

def service(request):

    objects = Contact.objects.all()

    return render(request, "service.html",{'data': objects})





