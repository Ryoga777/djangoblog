from django.db import models
from taggit.managers import TaggableManager

# Il Post sarà formato così:
# Titolo (un CharField di lunghezza massima 120 caratteri)
# Contenuto del post (un TextField grande)
#
# Poi ci saranno due campi ImageField per le immagini: 
# nel primo verrà caricata l'immagine principale del post, visualizzabile nella pagina del singolo post,
# nell' altro invece, verrà caricata un'immagine di 240x240, che verrà visualizzata nella Home Page
# e sarà l'anteprima del post
# 
# Un campo DateTimeField (invisibile), che conterrà la data di creazione del post 
# (ma non delle successive modifiche) e la visualizzerà nella pagina pubblica
#
# Un campo SlugField, che autogenererà lo slug del titolo del post.
#
# Un campo TaggableManager, in cui verranno aggiunti i tag relativi al post, separati da virgole

class Post(models.Model):

    titolo = models.CharField(max_length = 120)
    contenuto = models.TextField()
    immagine = models.ImageField(default='media/no-image-big.jpg', blank = True)

    data = models.DateTimeField(auto_now = False, auto_now_add = True)
    slug = models.SlugField()

    tag = TaggableManager()

    def __str__(self):
        return self.titolo 

class Comment(models.Model):
    
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)