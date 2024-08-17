from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

def home(request):
    return render(request, 'base/index.html')

def index(request):
    return render(request, 'index.html')

def project_details(request):
    return render(request, 'project-details.html')

def web_app_1(request):
    return render(request, 'App_details/web_app_1.html')

def enviar_correo_formulario(request):
    success = False  # Indicador de éxito
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Nombre: {name}\nCorreo: {email}\n\nMensaje:\n{message}"

        send_mail(
            subject=subject,
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,  # Debe coincidir con EMAIL_HOST_USER
            recipient_list=['czamorano@claudev.cl'],  # Correo al que deben llegar los mensajes
            fail_silently=False,
        )
        success = True  # Cambia el indicador a True si se envió con éxito

    return render(request, 'index.html', {'success': success})