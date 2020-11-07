from django.db import models
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from blogitproject.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
# Create your models here.


class Lead(models.Model):
    name = models.CharField(max_length=60, blank=True, default='')
    subject = models.CharField(max_length=60, blank=True, default='')
    email = models.EmailField(max_length=250, blank=False, default='')
    message = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now=True, blank=True)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return self.email + ' ' + self.subject + '(' + str(self.id) + ')'

@receiver(post_save, sender=Lead)
def send_notify_to_admin(sender,instance, created, *args, **kwargs):
    if created:
        subject = 'Notify #{0} - {1}'.format(instance.id, instance.subject)
        message = 'Person: {0}.\nFrom email: {1}.\nMessage:\n{2}'.format(instance.name.title(), instance.email, instance.message)
        from_email = EMAIL_HOST_USER
        recipient_list = [user.email for user in User.objects.filter(is_superuser = True)]
        send_mail(
            subject = subject,
            message = message,
            from_email = from_email,
            recipient_list = recipient_list,
            fail_silently = False, 
        )