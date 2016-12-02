from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Item, Movimentacao, Tipo

from .forms import TipoForm, ItemForm, MovimentacaoForm

# Create your views here.

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

    return redirect("usuarios:itens")


def excluir_tipo_view(request, id=None):
    tipo = get_object_or_404(Tipo, id=id)
    tipo.delete()

    return redirect("usuarios:itens")


def excluir_movimentacao_view(request, id=None):
    item = get_object_or_404(Movimentacao, id=id)
    item.delete()

    return redirect("usuarios:itens")


def lista_itens_view(request):

    if not request.user.is_authenticated():
        return render(request, 'cadastro_out.html')
    else:

        queryset = Item.objects.all()

        # query_itens = Itens.objects.all()
        # query = request.GET.get("q")
        #
        # if query:
        #     query_cadastro = query_cadastro.filter(
        #         Q(user__username__icontains=query) |
        #         Q(nome__icontains=query) |
        #         Q(patrimonio__icontains=query) |
        #         Q(cpf__icontains=query) |
        #         Q(email__icontains=query)
        #         ).distinct()

        context = {
        "queryset": queryset,
        }

        return render(request, "lista-itens.html", context)

def itens_view(request):

    form_item = ItemForm(request.POST or None)
    form_tipo = TipoForm(request.POST or None)
    form_movimentacao = MovimentacaoForm(request.POST or None)

    if form_item.is_valid():
        instance = form_item.save(commit=False)
        instance.save()

    if form_tipo.is_valid():
        tipo = form_tipo.save(commit=False)
        tipo.save()

    if form_movimentacao.is_valid():
        movimentacao = form_movimentacao.save(commit=False)
        movimentacao.save()

    query_item = Item.objects.all()
    query_tipo = Tipo.objects.all()
    query = request.GET.get("q")
    query2 = request.GET.get("p")

    if query:
        query_item = query_item.filter(
            Q(id__icontains=query) |
            Q(tipo__nome__icontains=query) |
            Q(patrimonio__icontains=query) |
            Q(origem__icontains=query) |
            Q(tipo__descricao__icontains=query)
            ).distinct()

    if query2:
        query_tipo = query_tipo.filter(
            Q(nome__icontains=query2) |
            Q(codigo__icontains=query2) |
            Q(descricao__icontains=query2)
            ).distinct()


    context = {
    "item": query_item,
    "tipos": query_tipo,
    "form_tipo": form_tipo,
    "form_item": form_item,
    "form_movimentacao": form_movimentacao,
    }

    return render(request, "new-item.html", context)
