from django.urls import path
from app_cad_usuario import views

urlpatterns = [
    #rota, views responsáveis, nome da referência
    #127.0.0.1/
    path('',views.home, name='home'),

    #Rota 127.0.0.1/produtos/
    path('produto/', views.produto, name='listar_items'),

    #Rota atualizar e deletar produto.
    path('atualizar/<int:id>/', name='atualizar_produto'),
    path('deletar/<int:id>/', name='deletar_produto')

]
