from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
import re

# Create your views here.
def home(request):
    return  render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "userame already exists, try with some other name")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists, try with some other email")
                return redirect('register')
            else:           
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Registered successfully, now login to website")
                return redirect('login')
        else:
            messages.error(request, "!!passwords dont match, try agan.")
            return redirect('register')

    else:
        return render(request, 'login.html')


def Login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
        
    else:
        return render(request, 'login.html')

def Logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):
    return  render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def chat(request):
    conversation = []  # Initialize an empty list to store the conversation

    if request.method == 'POST':
        user_input = request.POST['user_input']
        ai_response = 'AI response'#get_ai_response(user_input)  # Call your AI model integration function

        # Append the user's input and AI's response to the conversation
        conversation.append({'role': 'user', 'message': user_input})
        conversation.append({'role': 'ai', 'message': ai_response})
    else:
        user_input = ''
        ai_response = ''

    context = {
        'user_input': user_input,
        'ai_response': ai_response,
        'conversation': conversation,  # Pass the entire conversation to the template
    }

    return render(request, 'chat.html', context)
