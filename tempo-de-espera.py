#Imagine que você está criando um aplicativo de entrega de comida e precisa informar ao usuário o tempo estimado de entrega de um restaurante. 
#A mensagem deve conter o nome do restaurante e o tempo estimado de entrega em minutos.

#Entrada:
#A entrada deverá receber os valores abaixo:

#nomeRestaurante (string): o nome do restaurante desejado.
#tempoEstimadoEntrega (number): o tempo estimado de entrega em minutos.

import sys
nomeRestaurante = str(sys.stdin.readline().rstrip('\n'));
tempoEstimadoEntrega = int(sys.stdin.readline());
print('O restaurante %s entrega em %s minutos.'%(nomeRestaurante,tempoEstimadoEntrega));
