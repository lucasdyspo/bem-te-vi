from distutils.command.upload import upload
from pickle import TRUE
from django.db import models
from django.utils.translation import gettext_lazy as _
# from art.models import Art
# Create your models here.

#Usuario: caio12
#email: caio@gmail.com
#senha: teste1234


# class Arts_list:
#     art = models.ForeignKey(Art, on_delete=models.CASCADE, blank =True, null=True)

class Usuario(models.Model):
    nome = models.CharField(max_length=80)
    vulgo = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    # arts = models.ForeignKey(Art, on_delete=models.CASCADE, blank = True, null=True)
    # artss = models.ForeignKey(Arts_list, on_delete=models.CASCADE, blank = True, null=True)
    # similarity = models.CharField(max_length=64)
    
    
    def __str__(self):
        return str(self.vulgo) 
    



class Users_similarity(models.Model):
    to_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    from_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='similariaty')
    similariatyforgenres = models.FloatField()


class Friend(models.Model):
    to_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='friends')
    from_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    # objects = FriendshipManager()

    class Meta:
        verbose_name = _("Friend")
        verbose_name_plural = _("Friends")
        unique_together = ("from_Usuario", "to_Usuario")

    def __str__(self):
        return f"Usuario #{self.to_Usuario_id} is friends with #{self.from_Usuario_id}"



class FriendshipRequest(models.Model):
    """ Model to represent friendship requests """

    from_Usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="friendship_requests_sent",
    )
    to_Usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="friendship_requests_received",
    )

    message = models.TextField(_("Message"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    rejected = models.BooleanField(blank=True, null=True)
    viewed = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = _("Friendship Request")
        verbose_name_plural = _("Friendship Requests")
        unique_together = ("from_Usuario", "to_Usuario")

    def __str__(self):
        return f"Usuario #{self.from_Usuario_id} friendship requested #{self.to_Usuario_id}"

    







class Img_test(models.Model):
    img = models.ImageField(blank=True, null=True)
    
    

    
    



    

