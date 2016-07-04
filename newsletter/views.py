from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.shortcuts import render
from .form import SingnUpForm,ContactForm
# Create your views here.
def home(request):
    title="Welcome"
    form= SingnUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        if not form.cleaned_data.get("full_name"):
            instance.full_name="Siddharth Singh"
        instance.save()
        context["title"]="Thank You"

    return render(request,"home.html",context)
def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        'form': form
    }
    if(form.is_valid()):
        email=form.cleaned_data.get('email')
        message=form.cleaned_data.get('message')
        full_name=form.cleaned_data.get('full_name')
        print(email)
        to_email=[email]
        send_mail('Subjecthere', message, settings.EMAIL_HOST_USER, to_email, fail_silently=False)
   # myemail=EmailMessage("HI","WORLD",to=[email])
  #  myemail.send()

    return render(request,"forms.html",context)
def about_us(request):
    return render(request,"about_us.html",{})