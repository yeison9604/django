from django.urls import path
from .views import index, detalle_libro, nuevo_libro, eliminar_libro, actualizar_libro, logueo, RegistroUsuario
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", index.as_view(), name="index"),
    path("login/", logueo.as_view(), name="login"),
    path("sinup/", RegistroUsuario.as_view(), name="Registro"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("detalle-libro/<int:pk>", detalle_libro.as_view(), name="detalle"),
    path("nuevo-libro", nuevo_libro.as_view() , name="nuevo_libro"),
    path("eliminar-libro/<int:pk>", eliminar_libro.as_view(), name="eliminar"),
    path("actualizar-libro/<int:pk>", actualizar_libro.as_view(), name="editar")

]