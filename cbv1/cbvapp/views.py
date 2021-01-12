from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from cbvapp.models import student
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
class studentlistView(ListView):
    model=student
class studentDetailView(DetailView):
    model=student
class studentCreateView(CreateView):
    model=student
    fields=('name','number','marks','place')
class studentUpdateView(UpdateView):
    model=student
    fields=('name','marks')
class studentDeleteView(DeleteView):
    model=student
    success_url=reverse_lazy('student')
