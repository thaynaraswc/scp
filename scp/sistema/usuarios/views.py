from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission, Group
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Cadastro, Tarefas
from registro.models import Item

from .forms import CadastroForm, UserForm, TarefasForm


def users_view(request):

	if not request.user.is_authenticated():
		return render(request, 'cadastro_out.html')
	else:

		form = TarefasForm(request.POST or None)

		queryset = Cadastro.objects.all()
		tarefas = Tarefas.objects.all()
		itens = Item.objects.all()

		context = {
		"queryset": queryset,
		"form": form,
		"tarefas": tarefas,
		"itens": itens,
		}

		if form.is_valid():
			#form.save()
			instance = form.save(commit=False)
			#if not instance.full_name:
			#    instance.full_name = "Justin"
			instance.save()

		return render(request, "usuarios.html", context)


def novo_cadastro_view(request):

	if not request.user.is_authenticated():
		return render(request, 'cadastro_out.html')
	else:

	    form = CadastroForm(request.POST or None)

	    form_user = User.objects.all()

	    if form.is_valid():
	        instance = form.save(commit=False)
	        instance.save()

	    # if user is not None:
	    #     if user.is_active:
	    #         login(request, user)
	    #         cadastro = Cadastro.objects.filter(user=request.user)
	    #         queryset = Cadastro.objects.all()
	    #         context = {
	    #             "cadastro": cadastro,
	    #             "queryset":queryset,
	    #         }
	    #         return render(request, 'login.html', )

	    context = {
	    "form": form,
	    "user": form_user,
	    }

	    return render(request, "new-user.html", context)


def inicio_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("usuarios:users")

    return render(request, "inicio.html")


def lista_view(request):

	if not request.user.is_authenticated():
		return render(request, 'cadastro_out.html')
	else:

	    form = CadastroForm(request.POST or None)

	    #if request.user.is_authenticated():
	    #    title = "My title %s" %(request.user)

	    #if request.method == "POST":
	    #    print request.POST

	    queryset = Cadastro.objects.all()
	    print(queryset)

	    query_cadastro = Cadastro.objects.all()
	    query = request.GET.get("q")

	    if query:
	        query_cadastro = query_cadastro.filter(
	            Q(user__username__icontains=query) |
	            Q(nome__icontains=query) |
	            Q(patrimonio__icontains=query) |
	            Q(cpf__icontains=query) |
	            Q(email__icontains=query)
	            ).distinct()

	    context = {
	    "queryset": queryset,
	    "form": form,
	    }

	    return render(request, "list.html", context)


def editar_cadastro_view(request, id=None):

    cadastro = get_object_or_404(Cadastro, id=id)
    form_cadastro = CadastroForm(request.POST or None, instance=cadastro)

    print(form_cadastro)

    if form_cadastro.is_valid():
        print('entrou')
        cadastro = form_cadastro.save(commit=False)
        cadastro.save()


    context = {
    "cadastro": cadastro,
    "form_cadastro": form_cadastro,
    }

    return render(request, "editar-cadastro.html", context)


def excluir_tarefa_view(request, id=None):
    tarefa = get_object_or_404(Tarefas, id=id)
    tarefa.delete()

    tarefas = Tarefas.objects.all()

    context = {
    "tarefas":tarefas,
    }

    return redirect("usuarios:users")
    # return render(request, "usuarios.html", context)


def cadastro_alterar(request, cadastro_id):
    instance = get_object_or_404(Cadastro, pk=cadastro_id)
    form = CadastroForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "instance": instance,
        "form":form,
    }
    return render(request, "alterar.html", context)


def cadastro_deletar(request, cadastro_id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Cadastro, pk=cadastro_id)
    instance.delete()
    return render(request, 'usuarios.html', {})


def logout_view(request):
    logout(request)
    form = UserForm(request.POST or None)
    return redirect("usuarios:inicio")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        queryset = Cadastro.objects.all()
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'usuarios.html', {'albums': queryset})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


def cadastro_view(request):

	form_user = UserForm(request.POST or None)

	print("entrou")

	form = CadastroForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()


	if form_user.is_valid():

		user = form_user.save(commit=False)
		username = form_user.cleaned_data['username']
		password = form_user.cleaned_data['password']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)

		form = CadastroForm(request.POST or None)

		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()

		user_query = User.objects.latest('id')

		print(user.id)

		context = {
		"form": form,
		"user": user_query,
		}

		return render(request, "new-user.html", context)


	context = {
	"form": form_user,
	}

	return render(request, 'novo-cadastro.html', context)

def erro_view(request):
	return render(request, 'cadastro_out.html')
