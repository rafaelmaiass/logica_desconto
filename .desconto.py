print('Bem vindo a Loja do Rafael Maia de Assis')
valor_unitario = float(input('Digite o valor do produto: '))
quantidade_produto = int(input('Digite a quantidade de produtos: '))
valor_sem_desconto = valor_unitario * quantidade_produto
print(f'O valor sem desconto foi:  R$ {valor_sem_desconto}')

if quantidade_produto <= 9:
    print(f'O valor do produto com desconto foi: R$ {valor_sem_desconto} (0% de desconto)')

elif quantidade_produto <= 99:
    desconto_de_cinco = (5 * valor_sem_desconto) / 100
    desconto = valor_sem_desconto - desconto_de_cinco
    print(f'O valor com desconto foi: R$ {desconto}  (Desconto de 5% = R$ {desconto_de_cinco})')

elif quantidade_produto <= 999:
    desconto_de_dez = (10 * valor_sem_desconto) / 100
    desconto = valor_sem_desconto - desconto_de_dez
    print(f'O valor com desconto foi: R$ {desconto}  (Desconto de 10% = R$ {desconto_de_dez})')

else:
    desconto_de_quinze = (15 * valor_sem_desconto) / 100
    desconto = valor_sem_desconto - desconto_de_quinze
    print(f'O valor com desconto foi: R$ {desconto}  (Desconto de 15% = R$ {desconto_de_quinze})')
