from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import movie
from .  forms import movieForm

# Create your views here.
def index(request):
    mov=movie.objects.all()
    context={
        'movie_list':mov
    }
    return render(request,"index.html",context)
def detail(request,movie_id):
    move=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'move':move})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES.get('img')
        movi=movie(name=name,desc=desc,year=year,img=img)
        movi.save()
    return render(request,'add.html')
def update(request,id):
    move=movie.objects.get(id=id)
    form=movieForm(request.POST or None,request.FILES,instance=move)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'move':move})
def delete(request,id):
    if request.method=='POST':
        move=movie.objects.get(id=id)
        move.delete()
        return redirect('/')
    return render(request,'delete.html')