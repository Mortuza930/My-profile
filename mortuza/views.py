from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,'mortuza/home.html')
def resume (request):
    return render(request,'mortuza/resume.html')
def interest (request):
    return render(request,'mortuza/interest.html')
