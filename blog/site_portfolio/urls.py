from django.urls import path, re_path
from . import views
from django.views.generic import ListView, DetailView
from .models import Site_Portfolio

urlpatterns = [
    # Pagina Portfolio (riepilogo siti)
    re_path(r'^$', ListView.as_view(
        queryset = Site_Portfolio.objects.all().order_by("nome"),
        template_name = "portfolio.html",
        paginate_by = 6), name = "site_portfolio"),

    #Pagina con la descrizione di un singolo sito selezionato
    re_path(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', DetailView.as_view(
        model = Site_Portfolio,
        template_name = "selected-site"), name="selected"),
]