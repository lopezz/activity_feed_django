from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tracking = models.ManyToManyField('self', related_name='tracked_by', blank=True, symmetrical=False)

    def __str__(self):
        return str(self.user)


class Ownable(models.Model):
    user = models.ForeignKey(RegisteredUser, verbose_name=_("Author"), related_name="%(class)ss", on_delete=models.CASCADE)

    class Meta:
        abstract = True


class FeedItem(Ownable):
    content = models.CharField(_("Content"), max_length=1000, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)