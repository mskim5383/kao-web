# -*- coding: utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from public_web.models import WebContent

# Create your views here.



def home(request):
    try:
        main_text = WebContent.objects.filter(type='home_main')[0]
    except:
        main_text = None
    try:
        sub_text = WebContent.objects.filter(type='home_sub')[0]
    except:
        sub_text = None
    try:
        slider = WebContent.objects.filter(type='slider')[0]
    except:
        slider = None

    return render(request, 'public_web/home.html', {'slider': slider,
                                                    'main_text': main_text,
                                                    'sub_text': sub_text})

def about_us(request):
    return render(request, 'public_web/about_us.html', {'dark_ui': True})

def contact_us(request):
    return render(request, 'public_web/contact_us.html', {'dark_ui': True})

def faq(request):
    try:
        web_content = WebContent.objects.filter(type='faq')[0]
    except:
        web_content = None
    return render(request, 'public_web/faq.html', {'dark_ui': True,
                                                   'faq': web_content})
