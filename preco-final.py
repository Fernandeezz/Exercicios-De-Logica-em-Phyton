#Você está criando um aplicativo de entrega de comida e precisa calcular o preço final do pedido do usuário. 
#O usuário escolheu alguns itens do cardápio e é preciso calcular o preço total do pedido.

#Entrada:
#A entrada deve receber os valores abaixo:

#valorHamburguer: o valor unitário de um hambúrguer.
#quantidadeHamburguer: a quantidade de hambúrgueres que o usuário deseja.
#valorBebida: o valor unitário de uma bebida.
#quantidadeBebida: a quantidade de bebidas que o usuário deseja.
#valorPago: o valor pago pelo usuário.

import sys

valorHamburguer = float(sys.stdin.readline());
quantidadeHamburguer = int(sys.stdin.readline());
valorBebida = float(sys.stdin.readline());
quantidadeBebida = int(sys.stdin.readline());
valorPago = float(sys.stdin.readline());
totalPedido = (quantidadeHamburguer * valorHamburguer) + (quantidadeBebida * valorBebida);
trocoNecessario = valorPago - totalPedido;
print(f'O preço final do pedido é R$ {totalPedido:.2f}. Seu troco é R$ {trocoNecessario:.2f}.');
