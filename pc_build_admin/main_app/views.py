from django.shortcuts import render, redirect
from django.http import HttpResponse

import requests
import json

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
        return redirect('/manage_products')
    elif 'super_admin' in request.session:
        return redirect('/manage_admins')
    else:
        return render(request, 'login.html')

def login_validation(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('login_email')
            password = request.POST.get('login_password')

            user = auth_pyrebase.sign_in_with_email_and_password(email, password)

            if email == 'pc.build.app.2021@gmail.com':
                request.session['super_admin'] = user['localId']
            else:
                request.session['user_id'] = user['localId']

            return HttpResponse('Success!')
        except:
            return HttpResponse('Invalid Email or Password!')


def register(request):
    return render(request, 'register.html')

def homepage(request):
    return render(request, 'homepage.html')

def orders(request):
    if 'user_id' in request.session or 'super_admin' in request.session:

        orders = firestoreDB.collection('orders').get()

        order_data = []

        for order in orders:
            value = order.to_dict()
            order_data.append(value)

        data = {
            'order_data': order_data,
        }
        return render(request, 'orders.html', data)
    else:
        return redirect('/')

def logout(request):
    try:
        if 'user_id' in request.session:
            del request.session['user_id']
        elif 'super_admin' in request.session:
            del request.session['super_admin']
    except:
        return redirect('/')
    return redirect('/')

def manage_admins(request):
    if 'user_id' in request.session:
        return render(request, 'manage_products.html')
    elif 'super_admin' in request.session:
        users = firestoreDB.collection('admin_users').get()

        user_data = []

        for user in users:
            value = user.to_dict()
            user_data.append(value)

        data = {
            'user_data': user_data,
        }

        return render(request, 'manage_admins.html', data)
    else:
        return redirect('/')
    

def manage_products(request):
    if 'user_id' in request.session or 'super_admin' in request.session:

        products = firestoreDB.collection('products').get()

        product_data = []

        for product in products:
            value = product.to_dict()
            product_data.append(value)

        data = {
            'product_data': product_data,
        }
        return render(request, 'manage_products.html', data)
    else:
        return redirect('/')

def register_admin_firebase(request):

    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    if password == confirm_password:
        try:
            #register email and password to firebase auth
            user = auth_pyrebase.create_user_with_email_and_password(email, password)
           
            doc_ref = firestoreDB.collection('admin_users').document(user['localId'])
            doc_ref.set({
                'user_id': user['localId'],
                'email': email,
                'password': password,
                'first_name': first_name,
                'last_name': last_name,
            })

            return HttpResponse('New User Registered Successfully!')
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            if error == "EMAIL_EXISTS":
                return HttpResponse('Email Already Exists!')

    else:
        return HttpResponse('Password Do not Match!')

def delete_Admin(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')

        auth.delete_user(user_id)

        firestoreDB.collection('admin_users').document(user_id).delete()

        return redirect('manage_admins') 

def delete_Product(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')

        firestoreDB.collection('products').document(product_id).delete()
        return redirect('manage_products')

def edit_Admin(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name_edit')
        last_name = request.POST.get('last_name_edit')

        doc_ref = firestoreDB.collection('admin_users').document(user_id)

        doc_ref.update({
            'first_name': first_name,
            'last_name': last_name,
            })

        return redirect('manage_admins')

def edit_product(request):
      if request.method == 'POST':
        product_id_edit = request.POST.get('product_id_edit')
        product_name_edit = request.POST.get('product_name_edit')
        product_part_edit = request.POST.get('product_part_edit')
        product_price_edit = request.POST.get('product_price_edit')
        stocks_edit = request.POST.get('stocks_edit')

        doc_ref = firestoreDB.collection('products').document(product_id_edit)

        doc_ref.update({
            'product_id': product_id_edit,
            'product_name': product_name_edit,
            'product_part': product_part_edit,
            'product_price': product_price_edit,
            'stocks': stocks_edit,
            })

        return redirect('manage_products')

def add_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_part = request.POST.get('product_part')
        product_price = request.POST.get('product_price')
        stocks = request.POST.get('stocks')

        # try:
            
        # except:
        #     print('session not yet declared')

        same_product_name = firestoreDB.collection('products').where('product_name' , '==', product_name).stream()

        if(same_product_name == None):
            del request.session['product_already_exist']
            doc_ref = firestoreDB.collection('products').document()
            doc_ref.set({
                'product_id': doc_ref.id,
                'product_name': product_name,
                'product_part': product_part,
                'product_price': product_price,
                'stocks': stocks,
                })
        else:
            request.session['product_already_exist'] = "product exist"
        return redirect('manage_products')

def forgot_password(request):
    try:
        if request.method == 'POST':
            forgot_pass_email = request.POST.get('forgot_pass_email')
            auth_pyrebase.send_password_reset_email(forgot_pass_email)
            data = {
                'success': "Successfully Sent To Your Email",
            }
        else:
            data = {
                'success': "",
            }
    except:
        data = {
                'success': "Email Not Found!",
            }

    return render(request,'forgot_password.html', data)
