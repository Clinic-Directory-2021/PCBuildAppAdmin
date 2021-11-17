from django.shortcuts import render, redirect
from django.http import HttpResponse

import pyrebase

import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore

config = {
  'apiKey': "AIzaSyAOPOVIE_V9fbhD0A-OM8SE7bQIpujpoIE",
  'authDomain': "pcbuildapp-519e4.firebaseapp.com",
  'projectId': "pcbuildapp-519e4",
  'databaseURL': "https://pcbuildapp-519e4-default-rtdb.firebaseio.com",
  'storageBucket': "pcbuildapp-519e4.appspot.com",
  'messagingSenderId': "400114504001",
  'appId': "1:400114504001:web:a0a5c55e4d8d20e870d1c0",
}

firebase = pyrebase.initialize_app(config)
cred = credentials.Certificate("main_app/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

auth_pyrebase = firebase.auth()

firestoreDB = firestore.client()

storage = firebase.storage()

def login(request):
    if 'user_id' in request.session:
        return redirect('/homepage')
    else:
        return render(request, 'login.html')

def login_validation(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('login_email')
            password = request.POST.get('login_password')

            user = auth_pyrebase.sign_in_with_email_and_password(email, password)

            request.session['user_id'] = user['localId']

            return render(request, 'login.html')
        except:
            return HttpResponse('Invalid Email or Password!')


def register(request):
    return render(request, 'register.html')