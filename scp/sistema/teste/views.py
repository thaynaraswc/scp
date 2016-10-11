from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.shortcuts import render, get_object_or_404

from .forms import RegistroForm, UserForm
from .models import Registro

# Create your views here.

def users_view(request):

	form = RegistroForm(request.POST or None)
	#if request.user.is_authenticated():
	#    title = "My title %s" %(request.user)

	#if request.method == "POST":
	#    print request.POST

	queryset = Registro.objects.all()

	context = {
	"queryset": queryset,
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

def novo_view(request):

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

    return render(request, "new-user.html", context)


def lista_view(request):

    form = RegistroForm(request.POST or None)
    #if request.user.is_authenticated():
    #    title = "My title %s" %(request.user)

    #if request.method == "POST":
    #    print request.POST

    queryset = Registro.objects.all()

    context = {
    "queryset": queryset,
    "form": form,
    }

    return render(request, "list.html", context)


def registro_alterar(request, registro_id):
    instance = get_object_or_404(Registro, pk=registro_id)
    form = RegistroForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "instance": instance,
        "form":form,
    }
    return render(request, "alterar.html", context)


def registro_deletar(request, registro_id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Registro, pk=registro_id)
    instance.delete()
    return render(request, 'usuarios.html', {})


def logout_view(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        queryset = Registro.objects.all()
        if user is not None:
            if user.is_active:

                login(request, user)
                albums = Registro.objects.filter(user=request.user)
                return render(request, 'usuarios.html', {'albums': albums})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


def registro_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Registro.objects.filter(user=request.user)
                queryset = Registro.objects.all()
                context = {
                    "albums": albums,
                    "queryset":queryset,
                }
                return render(request, 'usuarios.html', )
    context = {
        "form": form,
    }
    return render(request, 'registro.html', context)