from django.shortcuts import render, redirect
from .models import Libro
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy


# Create your views here.

class RegistroUsuario(FormView):
    template_name = "base/registro.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(RegistroUsuario, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("index")
        return super(RegistroUsuario, self).get(*args, **kwargs)



class logueo(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

class index(LoginRequiredMixin, ListView):
    model = Libro
    context_object_name = 'libros'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        valor_buscado = self.request.GET.get("buscar-libro")
        if valor_buscado:
            context['libros'] = context['libros'].filter(titulo__icontains=valor_buscado)

        context['buscar-libro'] = valor_buscado
        return context

class detalle_libro(LoginRequiredMixin, DetailView):
    model = Libro
    context_object_name = 'libro'

class nuevo_libro(CreateView):
    model = Libro
    fields = '__all__'
    success_url = reverse_lazy('index')


class eliminar_libro(DeleteView):
    model = Libro
    success_url = reverse_lazy('index')


class actualizar_libro(UpdateView):
    model = Libro
    fields = '__all__'
    success_url = reverse_lazy('index')