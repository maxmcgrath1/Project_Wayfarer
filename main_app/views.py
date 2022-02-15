from re import template
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import City, Post
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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

@method_decorator(login_required, name='dispatch')
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

class CityDelete(DeleteView):
    model = City
    template_name = "city_delete_confirmation.html"
    success_url = "/cities/"

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("city_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

# @method_decorator(login_required, name='dispatch')
class PostCreate(View):
    def post(self, request, pk):
        title = request.POST.get("title")
        body = request.POST.get("body")
        city = City.objects.get(pk=pk)
        Post.objects.create(title=title, body=body, city=city)
        return redirect('city_detail', pk=pk)

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(PostCreate, self).form_valid(form)

    # def get_success_url(self):
    #     print(self.kwargs)
    #     return reverse('city_detail', kwargs={'pk': self.object.pk})

    # def login(request):
    #     nxt = request.GET.get("next", None)
    #     url = '/accounts/login/'

    #     if nxt is not None:
    #         url += '?next=' + nxt

    #     return redirect(url)

@method_decorator(login_required, name='dispatch')
class Profile(TemplateView):
    template_name = "user_profile.html"