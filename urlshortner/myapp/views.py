from django.shortcuts import render,redirect
from .models import URLmodel
import random
import string

# Create your views here..
def home(request):

    if request.method == 'POST':
        yoururl = request.POST.get('orignal_url')
        random_chars = string.ascii_letters  # This includes both lowercase and uppercase letters
        shortened_url = ''.join(random.sample(random_chars, 7))

        URLmodel.objects.create(orignal_url=yoururl,new_url=shortened_url)

        shorturl = "http://localhost:8000/"+shortened_url
        return render(request,'home.html',{'yoururl':yoururl,'shorturl':shorturl})

    return render(request,'home.html')


def orignalurlredirect(request,newurl):
    url = URLmodel.objects.get(new_url=newurl)
    print('This is :',url)
    return redirect(url.orignal_url)
