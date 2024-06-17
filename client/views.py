from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Client
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

@api_view(['POST'])
def append_client_api(request):
    data = request.data
    f_i_o = data.get('name')
    telefon_raqam = data.get('phone_number')
    Client.objects.create(f_i_o=f_i_o, telefon_raqam=telefon_raqam)
    subject = "CosmosTJ"
    template = render_to_string('email/email.html', {'f_i_o': f_i_o, 'telefon_raqam': telefon_raqam})
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['kosmostj.pm@gmail.com',]
    message = EmailMultiAlternatives(
        subject=subject,
        body=template,
        from_email=from_email,
        to=recipient_list
    )
    message.attach_alternative(template, "text/html")
    try:
        message.send()
    except Exception as e:
        return JsonResponse({'status': False, 'error': str(e)}, status=500)
    return JsonResponse({'status': True}, status=200)

