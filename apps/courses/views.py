from django.shortcuts import render ,redirect, HttpResponse
from .models import * 

# Create your views here.
def index (request):
    context = {
        'course' : Course.objects.all(),
        'description': Description.objects.all(),
    }
    return render (request,'index.html', context)

def create(request):
    if 'course_name' not in request.POST or 'description' not in request.POST:
        return redirect('/')
    if len(request.POST['course_name']) < 6 or len(request.POST['description']) < 16: 
        return redirect('/')
    if request.method =='POST':
        c = Course.objects.create(name = request.POST['course_name'])
        d = Description(course= c, text = request.POST['description'] )
        d.save()
    return redirect('/')

def destroy (request,id):
    context = {
        'course': Course.objects.get(id=id),
        'description': Description.objects.get(course_id=id),
    }
    return render (request, 'courses.html', context)
def deletecourse(request, id):
    Course.objects.get(id =id).delete()
    return redirect('/')
