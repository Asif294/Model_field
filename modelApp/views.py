

from django.shortcuts import render
from .forms import StudentForm

def home(request):
    form = StudentForm()
    return render(request, 'home.html', {'form': form})
