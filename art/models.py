from django.db import models
from distutils.command.upload import upload
from pickle import TRUE
from django import forms
from login.models  import Usuario



# Create your models here.
# class ImageUploadForm(forms.Form):
#     """Image upload form."""
#     image = forms.ImageField()
    
class ExampleModel(models.Model):
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    
    
class Img_teste(models.Model):
    img = models.ImageField(blank=True, null=True)
    
    
    
class Art(models.Model):

    GENRES = [
    ('action', 'action'), ('comedy', 'comedy'), ('drama', 'drama'), ('horror', 'horror'), 
    ('mistery', 'mistery'), ('romance', 'romance'), ('thriller', 'thriller')
    ]
    
  
    encodexname = models.CharField(max_length=160, blank=True)
    name = models.CharField(max_length=80)
    description = models.TextField()
    thumbs_path = models.CharField(blank=True, max_length=200)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # private = models.BooleanField()
    user_main = models.ForeignKey(Usuario, blank=True, null=True, on_delete=models.CASCADE, related_name='user_main')
    users_collaborators = models.ManyToManyField(Usuario, blank=True, related_name='users')
    # other_users
    genre = models.CharField(max_length=30, null=True, blank=True, choices=GENRES)
    tags = models.CharField(max_length=120, null=True, blank=True)
    
    
    class meta:
        verbose_name = "art"
    
    
    def __str__(self):
        return self.name
    
    
    
    
class favorites(models.Model):
    # user = models.OneToOneField(Usuario, related_name='favorites', on_delete=models.DO_NOTHING, primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='favorites')
    art = models.ForeignKey(Art, on_delete=models.CASCADE, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    
    
    
class Likes(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='likes')
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    
    
class Comment(models.Model):
    art = models.ForeignKey(Art, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    