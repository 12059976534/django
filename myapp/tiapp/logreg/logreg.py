from django.contrib.messages.api import error
from django.shortcuts import render,reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from tiapp.models import User
from django.contrib import messages

def login(request):
    if request.session.has_key('user'):
        return HttpResponseRedirect(reverse('admin'))
    if request.method == 'POST':
        user=request.POST['user']
        pas=request.POST['pas']
        
        try:
            data=User.objects.get(username=user)
            if data:
                if data.password == pas:
                    request.session['user'] = user
                    return HttpResponseRedirect(reverse('admin'))
                messages.warning(request,'password not palid !!!',extra_tags='inpalidpas')  
                return HttpResponseRedirect(reverse('login'))  
        except User.DoesNotExist:    
            messages.info(request,'your account is not exis !!',extra_tags='not_exist')  
            return HttpResponseRedirect(reverse('login'))  

    return render(request, 'tiapp/login.html')

def logout(request):
    if request.session.has_key('user'):
        try:
            del request.session['user']
        except:
            return HttpResponse('erorr')    
        return HttpResponseRedirect(reverse('login'))
    return HttpResponseRedirect(reverse('index'))    
    

