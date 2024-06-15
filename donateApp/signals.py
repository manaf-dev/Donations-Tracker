# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.core.mail import send_mail
# from .models import Donation
# from DonationTracker import settings

# @receiver(post_save, sender=Donation)
# def send_donation_notification(sender, instance, created, **kwargs):
#     if created:
#         subject = 'New Donation Made'
#         message = f'A new donation has been made to {instance.event.title}'
#         recipient_list = [instance.event.admin.email]

#         send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

#         # send donor an SMS also.

