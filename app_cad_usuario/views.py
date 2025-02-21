from django.shortcuts import render
from .models import Produto

def home(request):
    return render(request,'produto/home.html')


def produto(request):
    #salvar dados no Banco
    novo_produto = Produto()
    novo_produto.nome = request.POST.get('nome')
    novo_produto.serie = request.POST.get('serie')
    novo_produto.quantidade = request.POST.get('quantidade')
    novo_produto.save()

    #exibir produtos
    produto = {
        'produto': Produto.objects.all()
    }
    #retorna para pagina de lista de itens
    return render(request, 'produto/produto.html', produto)

# Atualizar Produto
def atualizar_produto(request, id):
    produto = atualizar_produto(Produto, id_produto=id)
    if request.method == "POST":
        produto.nome = request.POST.get("nome")
        produto.serie = request.POST.get("serie")
        produto.quantidade = request.POST.get("quantidade")
        produto.save()
        return render('listar_produtos')  # Redireciona para a lista após a atualização
    return render(request, 'produto/atualizar_produto.html', {'produto': produto})

# Deletar Produto
def deletar_produto(request, id):
    produto = deletar_produto(Produto, id_produto=id)
    if request.method == "POST":
        produto.delete()
        return render('listar_produtos')  # Redireciona para a lista após a exclusão
    return render(request, 'produto/deletar_produto.html', {'produto': produto})
