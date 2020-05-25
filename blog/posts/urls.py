from django.urls import path, re_path
from . import views
from django.views.generic import ListView, DetailView
from .models import Post

urlpatterns = [
    #homepage (lista post)
    re_path(r'^$', ListView.as_view(
        queryset = Post.objects.all().order_by("-data"),
        template_name = "lista-post.html",
        paginate_by = 6), name = "lista"),

    #Pagina di un singolo post
    re_path(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', DetailView.as_view(
        model = Post,
        template_name = "post-singolo.html"), name="singolo"),

    #Pagina dei contatti
    re_path(r'^contatti/$', views.contatti, name="contatti"),

]