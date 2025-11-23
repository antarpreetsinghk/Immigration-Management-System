from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from .models import Application, Lead


# @receiver(post_save, sender=Application)
# def delete_lead(sender, instance, created, **kwargs):
#     if created:
#         lead = get_object_or_404(Lead, id=instance.id)
#         lead.delete()
