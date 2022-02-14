from re import template
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import City

class Home(TemplateView):
    template_name = "home.html"


class CityList(TemplateView):
    template_name = "city_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["cities"] = City.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["cities"] = City.objects.all()
            context["header"] = "Featured Cities"
        return context

class CityCreate(CreateView):
    model = City
    fields = ['name', 'image', 'population', 'attractions']
    template_name = "city_create.html"
    
    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.object.pk})

class CityDetail(DetailView):
    model = City
    template_name = "city_detail.html"

class CityUpdate(UpdateView):
    model = City
    fields = ['name', 'image', 'population', 'attractions']
    template_name = "city_update.html"
    
    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.object.pk})