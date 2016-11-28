from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission, Group
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Registro, Item, Movimentacao, Tipo, Tarefas

from .forms import RegistroForm, TipoForm, ItemForm, UserForm, MovimentacaoForm, TarefasForm

# Create your views here.



def users_view(request):

	form = RegistroForm(request.POST or None)
	
	queryset = Registro.objects.all()
        tarefas = Tarefas.objects.all()

	context = {
	"queryset": queryset,
	"form": form,
    "tarefas": tarefas,
	}

	if form.is_valid():
		#form.save()
		instance = form.save(commit=False)
		#if not instance.full_name:
		#    instance.full_name = "Justin"
		instance.save()

	return render(request, "usuarios.html", context)


def novo_registro_view(request):

    form = RegistroForm(request.POST or None)

    form_user = UserForm(request.POST or None)
    
    print(form_user)

    if form_user.is_valid():

        user = form_user.save(commit=False)
        username = form_user.cleaned_data['username']
        password = form_user.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)

        updated_data = request.POST.copy()
        updated_data.update({'user': user}) 
        form = RegistroForm(data=updated_data) 

        if form.is_valid():
            print("Entrou")
            instance = form.save(commit=False)
            instance.save()

        # if user is not None:
        #     if user.is_active:
        #         login(request, user)
        #         registro = Registro.objects.filter(user=request.user)
        #         queryset = Registro.objects.all()
        #         context = {
        #             "registro": registro,
        #             "queryset":queryset,
        #         }
        #         return render(request, 'login.html', )

    context = {
    "form": form,
    "form_user": form_user,
    }
    
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

def novo_tarefa_view(request):
    
    form = TarefasForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        # tarefas = Tarefas.objects.all()

        # context = {
        # "tarefas":tarefas,
        # "form": form,
        # }

        return redirect("teste:users")

    context = {
    "form": form,
    }
    
    return render(request, "tarefa.html", context)


def novo_item_view(request):

    form = ItemForm(request.POST or None)

    queryset = Item.objects.all()

    context = {
    "form": form,
    "queryset": queryset
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(request, "novo-item.html", context)


def novo_tipo_view(request):

    form = TipoForm(request.POST or None)

    queryset = Tipo.objects.all()

    context = {
    "form": form,
    "queryset": queryset
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(request, "novo-tipo.html", context)

def novo_movimentacao_view(request):

    form = MovimentacaoForm(request.POST or None)

    queryset = Movimentacao.objects.all()

    context = {
    "form": form,
    "queryset": queryset
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(request, "novo-movimentacao.html", context)


def editar_movimentacao_view(request, id=None):

    movimentacao = get_object_or_404(Movimentacao, id=id)
    form_movimentacao = MovimentacaoForm(request.POST or None, instance=movimentacao)

    if form_movimentacao.is_valid():
        #form.save()
        movimentacao = form_movimentacao.save(commit=False)
        # tipo.item = item
        #if not instance.full_name:
        #    instance.full_name = "Justin"
        movimentacao.save()

    context = {
    "movimentacao": movimentacao,
    "form_movimentacao": form_movimentacao,
    }

    return render(request, "editar-movimentacao.html", context)


def editar_tipo_view(request, id=None):

    tipo = get_object_or_404(Tipo, id=id)
    form_tipo = TipoForm(request.POST or None, instance=tipo)

    if form_tipo.is_valid():
        tipo = form_tipo.save(commit=False)
        tipo.save()


    context = {
    "tipo": tipo,
    "form_tipo": form_tipo,
    }

    return render(request, "editar-tipo.html", context)


def editar_item_view(request, id=None):
    item = get_object_or_404(Item, id=id)
    form_item = ItemForm(request.POST or None, instance=item)

    if form_item.is_valid():
        #form.save()
        item = form_item.save(commit=False)
        # tipo.item = item
        #if not instance.full_name:
        #    instance.full_name = "Justin"
        item.save()

    context = {
    "item": item,
    "form_item": form_item,
    }

    return render(request, "editar-item.html", context)


def excluir_item_view(request, id=None):
    item = get_object_or_404(Item, id=id)
    item.delete()

    return redirect("teste:itens")


def excluir_tipo_view(request, id=None):
    tipo = get_object_or_404(Tipo, id=id)
    tipo.delete()

    return redirect("teste:itens")


def excluir_movimentacao_view(request, id=None):
    item = get_object_or_404(Movimentacao, id=id)
    item.delete()

    return redirect("teste:itens")

def excluir_tarefa_view(request, id=None):
    tarefa = get_object_or_404(Tarefas, id=id)
    tarefa.delete()

    tarefas = Tarefas.objects.all()

    context = {
    "tarefas":tarefas,
    }

    return redirect("teste:users")
    # return render(request, "usuarios.html", context)


def new_view(request, id=None):

    form_movimentacao = MovimentacaoForm(request.POST or None)

    tipo = get_object_or_404(Tipo, id=id)
    form_tipo = TipoForm(request.POST or None, instance=tipo)

    if form_tipo.is_valid():
        #form.save()
        tipo = form_tipo.save(commit=False)
        # tipo.item = item
        #if not instance.full_name:
        #    instance.full_name = "Justin"
        tipo.save()

    if form_movimentacao.is_valid():
        #form.save()
        movimentacao = form_movimentacao.save(commit=False)
        # movimentacao.item = item
        #if not instance.full_name:
        #    instance.full_name = "Justin"
        movimentacao.save()

    context = {
    "tipo": tipo,
    "form_tipo": form_tipo,
    "form_movimentacao": form_movimentacao,
    }

    return render(request, "new.html", context)


def itens_view(request):

    form_item = ItemForm(request.POST or None)
    form_tipo = TipoForm(request.POST or None)
    form_movimentacao = MovimentacaoForm(request.POST or None)
    print(form_item)
    #if request.user.is_authenticated():
    #    title = "My title %s" %(request.user)

    #if request.method == "POST":
    #    print request.POST

    if form_item.is_valid():
        #form.save()
        instance = form_item.save(commit=False)
        #if not instance.full_name:
        #    instance.full_name = "Justin"
        instance.save()

    if form_tipo.is_valid():
        #form.save()
        tipo = form_tipo.save(commit=False)
        #if not instance.full_name:
        #    instance.full_name = "Justin"
        tipo.save()

    if form_movimentacao.is_valid():
        #form.save()
        movimentacao = form_movimentacao.save(commit=False)
        #if not instance.full_name:
        #    instance.full_name = "Justin"
        movimentacao.save()

    query_item = Item.objects.all()
    query = request.GET.get("q")

    if query:
        query_item = query_item.filter(
            Q(tipo__nome__icontains=query) |
            Q(patrimonio__icontains=query) |
            Q(origem__icontains=query) |
            Q(descricao__icontains=query)
            ).distinct()

    
    tipos = Tipo.objects.all()
    # print(str(item.tipo))

    context = {
    "item": query_item,
    "tipos": tipos,
    "form_tipo": form_tipo,
    "form_movimentacao": form_movimentacao,
    }

    return render(request, "new-item.html", context)


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
    return redirect("teste:login")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        queryset = Registro.objects.all()
        if user is not None:
            if user.is_active:

                login(request, user)
                return render(request, 'usuarios.html', {'albums': queryset})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


def registro_view(request):
    form = UserForm(request.POST or None)
    print(form)
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
                registro = Registro.objects.filter(user=request.user)
                queryset = Registro.objects.all()
                context = {
                    "registro": registro,
                    "queryset":queryset,
                }
                return render(request, 'usuarios.html', )
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)