#Você foi contratado para desenvolver um sistema que armazena informações dos pedidos de comida online realizados por um cliente. 
#O sistema deve permitir ao cliente inserir novos pedidos, escolher um cupom de desconto (10% ou 20%) e exibir o valor total de todos os pedidos realizados até o momento, com o desconto aplicado.

#Entrada:
#A entrada é composta por:
#Uma linha com um número inteiro n representando a quantidade de pedidos que o usuário deseja inserir;
#n linhas, cada uma contendo uma string com o nome do pedido e um valor em ponto flutuante separados por espaço. O nome do pedido não contém espaços em branco;
#Uma linha contendo o cupom de desconto escolhido (10% ou 20%).

def main():
    n = int(input())
    total = 0

    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
    cupomDesconto = float(input().rstrip('%'))
    cupomDesconto /= 100

    if cupomDesconto == 0.1:  # 10% de desconto
        total *= (1 - cupomDesconto)
    elif cupomDesconto == 0.2:  # 20% de desconto
        total *= (1 - cupomDesconto)

    print("Valor total: {:.2f}".format(total))

if __name__ == "__main__":
    main()
