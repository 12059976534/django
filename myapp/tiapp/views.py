from django.shortcuts import render,reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import User,Info,Matkul
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.core.paginator import Page, Paginator


def index(request):
    dat=Info.objects.order_by('-id')
    paginator = Paginator(dat, 2)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'tiapp/index.html',{'page':page})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin(request):
    if request.session.has_key('user'):
        if request.method == "POST":
            username=request.POST['user']
            password=request.POST['pas'] 
            palidasi=request.POST['pallid']
            user=User.objects.filter(username=username)
            if user:
                messages.add_message(request, messages.INFO, 'user sudah ter daftar !!!',extra_tags='ready')
                return HttpResponseRedirect(reverse('admin'))

            if password == palidasi:
                save = User(
                    username=username, 
                    password=password
                    )
                save.save()    
                messages.add_message(request, messages.INFO, 'register succes...',extra_tags='resil')
                return HttpResponseRedirect(reverse('admin'))
            
            messages.warning(request,'password not palid !!!',extra_tags='regal')  
            return HttpResponseRedirect(reverse('admin'))
        data=User.objects.all()
        return render(request, 'tiapp/admin.html',{'data':data})  
    return HttpResponseRedirect(reverse('login'))    

def info(request):
     if request.session.has_key('user'):
        if request.method == 'POST':
            info=request.POST['info']
            sesku=request.session['user']
            save=Info(content=info,user=str(sesku))
            save.save()
            
            messages.add_message(request, messages.INFO,'succes ...',extra_tags='insil')
            return HttpResponseRedirect(reverse('admin'))    
     return HttpResponseRedirect(reverse('login'))       



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def tambah(request):
    if request.session.has_key('user'):
        if request.method == 'POST':
            matkul=request.POST['matkul']
            dosen=request.POST['dosen']
            hari=request.POST['hari']
            jam=request.POST['jam']
            save=Matkul(matakuliah=matkul,dose=dosen,hari=hari,jam=jam)
            save.save()
            messages.add_message(request, messages.INFO, 'register succes...',extra_tags='tasil')
            return HttpResponseRedirect(reverse('tambah'))
        return render(request, 'tiapp/tambah.html')
    return HttpResponseRedirect(reverse('login'))        

def update(request):
    return render(request, 'tiapp/update.html')    
