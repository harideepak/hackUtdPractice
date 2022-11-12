from simpleApp.models import PhoneBook
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
import json


@api_view(['GET'])
def about(request):
    return HttpResponse("This is a simple application")


@api_view(['GET', 'POST'])
def insertData(request, name):
    phoneBook = PhoneBook(name=name, contactNumber="080900")
    phoneBook.save()
    return HttpResponse("Inserted sucessfully")


@api_view(['POST'])
def insertDataFromBody(request):
    body_unicode = request.body.decode('utf-8')
    print(body_unicode)
    body = json.loads(body_unicode)
    name = body['name']
    print(name)
    if request.method == 'POST':
        phoneBook = PhoneBook(name=name, contactNumber="080900")
        phoneBook.save()
    return HttpResponse("Inserted sucessfully")


@api_view(['GET'])
def getData(request):
    myData = PhoneBook.objects.all().values()
    print(myData)
    return HttpResponse(myData)
