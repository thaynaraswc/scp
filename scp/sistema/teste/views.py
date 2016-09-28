from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegistroForm
from .models import Registro

# Create your views here.

def users_view(request):

	form = RegistroForm(request.POST or None)
	#if request.user.is_authenticated():
	#    title = "My title %s" %(request.user)

	#if request.method == "POST":
	#    print request.POST
	context = {
	"form": form,
	}

	if form.is_valid():
		print ("nada")
		#form.save()
		instance = form.save(commit=False)
		#if not instance.full_name:
		#    instance.full_name = "Justin"
		instance.save()

	return render(request, "usuarios.html", context)
