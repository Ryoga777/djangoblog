from django.db import models

# La pagina admin in cui si inseriranno le anteprime dei siti pubblicati e delle demo
# conterrà i seguenti campi: 
# - nome: il nome del sito (sottoforma di CharField);
# - screenshot: una piccola immagine di anteprima del sito;
# - descrizione: breve descrizione del sito e delle sue funzionalità;
# - url: l'url per raggiungere il sito;
# - slug: lo slug autogenerato per la barra di navigazione.

class Site_Portfolio(models.Model):

    nome = models.CharField(max_length = 120)
    screenshot = models.ImageField(upload_to='site-previews/', default='no-image-big.jpg')
    descrizione = models.TextField()
    url = models.URLField()

    slug = models.SlugField()

    def __str__(self):
        return self.nome