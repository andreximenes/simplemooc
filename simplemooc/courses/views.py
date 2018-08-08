from django.shortcuts import render
from .models import Course

# Create your views here.
def index(request):
    template_name='courses/index.html'
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, template_name, context)
