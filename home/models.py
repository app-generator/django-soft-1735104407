# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Categary(models.Model):

    #__Categary_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Categary_FIELDS__END

    class Meta:
        verbose_name        = _("Categary")
        verbose_name_plural = _("Categary")


class Item(models.Model):

    #__Item_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    categary = models.ForeignKey(categary, on_delete=models.CASCADE)

    #__Item_FIELDS__END

    class Meta:
        verbose_name        = _("Item")
        verbose_name_plural = _("Item")



#__MODELS__END
