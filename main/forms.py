from django import forms
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your name')
    message = forms.CharField(max_length=600, widget=forms.Textarea)

    def send_mail(self):
        logger.info('Sending email to customer service')
        message = f'From {self.cleaned_data["name"]} \n'
        message += f'{self.cleaned_data["message"]}'
        send_mail(
            'Site message',
            message,
            'test@mail.com',
            ['testcustserveice@mail.com'],
            fail_silently=False
        )