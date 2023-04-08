from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone



from common.models import IndexedTimeStampedModel

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=60, null=True, blank=True, unique=True)
    name = models.CharField(max_length=60, null=True, blank=True)
    bio = models.TextField(max_length=60, null=True, blank=True)
    # birth = models.DateField(null=True, blank=True, default=None)
    country = models.CharField(max_length=40, null=True, blank=True, verbose_name=_('country'))

    # age = models.IntegerField()
    img = models.ImageField(upload_to='profiles', blank=True, null=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    behance = models.URLField(max_length=200, null=True, blank=True)



    is_staff = models.BooleanField(
        default=False, help_text=_("Designates whether the user can log into this admin " "site.")
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )
    createdAt = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name=_('Data de Criação'))
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name=_('Data de Modificação'))
    objects = UserManager()

    USERNAME_FIELD = "email"

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        if self.username:
            return self.username
        else:
            return self.email

    # @property
    # def is_staff(self):
        # "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        # return self.is_admin








class Friend(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = _("Friend")
        verbose_name_plural = _("Friends")
        unique_together = ("from_user", "to_user")

    def __str__(self):
        return f"User #{self.to_user_id} is friends with #{self.from_user_id}"







class FriendshipRequest(models.Model):
    """ Model to represent friendship requests """

    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="friendship_requests_sent",
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="friendship_requests_received",
    )

    message = models.TextField(_("Message"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(null=True)
    viewed = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = _("Friendship Request")
        verbose_name_plural = _("Friendship Requests")
        unique_together = ("from_user", "to_user")

    def __str__(self):
        return f"User #{self.from_user_id} friendship requested #{self.to_user_id}"



    def accept(self):
        """ Accept this friendship request """
        Friend.objects.create(from_user=self.from_user, to_user=self.to_user)
        Friend.objects.create(from_user=self.to_user, to_user=self.from_user)
        friendship_request_accepted.send(
            sender=self, from_user=self.from_user, to_user=self.to_user
        )

        self.delete()

        # Delete any reverse requests
        FriendshipRequest.objects.filter(
            from_user=self.to_user, to_user=self.from_user
        ).delete()

        return True

    def reject(self):
        """ reject this friendship request """
        self.rejected = timezone.now()
        self.save()
        return True

    def cancel(self):
        """ cancel this friendship request """
        self.delete()
        friendship_request_canceled.send(sender=self)
        return True

    def mark_viewed(self):
        self.viewed = timezone.now()
        friendship_request_viewed.send(sender=self)
        self.save()
        return True





