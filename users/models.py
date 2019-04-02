from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from branch.models import Branch


class Permissions(models.Model):
    GEN = 'General User'
    ENC = 'Encoder'
    SYS = 'System Admin'
    SUP = 'Super User'

    PERMISSIONS = (
        (GEN, 'General User'),
        (ENC, 'Encoder'),
        (SYS, 'System Admin'),
        (SUP, 'Super User')
    )

    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE
    )
    permission = models.CharField(max_length=20, choices=PERMISSIONS)
    branch = models.ForeignKey(
        Branch,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )


    def __str__(self):
        return self.user.username


    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            profile, created = Permissions.objects.get_or_create(user=instance)  

    post_save.connect(create_user_profile, sender=User)


    class Meta:
        verbose_name = 'Permission'
        verbose_name_plural = 'Permissions'
