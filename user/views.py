from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import *
from django.contrib.auth import get_user_model

from user.forms import RegisterForm
from user.models import Film
# Create your views here.

class IndexView(TemplateView):
     template_name = 'index.html'
class Login(LoginView):
    template_name = 'registration/login.html'

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("This username already exists")
    else:
        return HttpResponse("")


class Filmlist(ListView):
    template_name = 'registration/films.html'
    model = Film
    context_object_name = 'films'


    def get_queryset(self):
        user = self.request.user
        return  user.films.all()

def add_film(request):
    name = request.POST.get('filmname')
    
    # add film
    film = Film.objects.create(name=name)
    
    # add the film to the user's list
    request.user.films.add(film)

    # return template fragment with all the user's films
    films = request.user.films.all()
    return render(request, 'registration/film-list.html', {'films': films})
