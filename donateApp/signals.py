from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from .models import Donation

@receiver(post_save, sender=Donation)
def send_donation_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'New Donation Made'
        message = 'A new donation has been made to your event.'
        from_mail = 'remsgrafix@gmail.com'
        recipient_list = [instance.event.admin.email]

        send_mail(subject, message, from_mail, recipient_list)

        # send donor an SMS also.

