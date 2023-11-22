from time import sleep

print('~' * 26)
sleep(0.3)
print('BEM VINDO AO MISTER BURGER')
print('~' * 26)
sleep(0.3)
print(' ')
print('=' * 26)
sleep(0.3)
print('VAMOS ANOTAR O SEU PEDIDO!')
sleep(0.3)
print('=' * 26)
sleep(0.3)
print("""    0: Não desejo nenhum item
    1: Cheese Burger - 15.50 reais
    2: Cheese Salada - 18.50 reais
    3: Cheese Bacon  - 21.00 reais
    4: Cheese Picanha - 25.00 reais
""")
sleep(0.3)
lanche = {'Cheese Burger': 15.5, 'Cheese Salada': 18.5, 'Cheese Bacon': 21, 'Cheese Picanha': 25}
cont = 'SN'
total = []

while True:
    while True:
        sleep(0.3)
        opcao = float(input('Escolha a sua opção de Lanche:'))
        if opcao > 4:
            sleep(0.3)
            print('opção inválida, favor digitar novamente:')
        else:
            if opcao == 1:
                total.append(lanche['Cheese Burger'])
                print('cheese burger')
            elif opcao == 2:
                total.append(lanche['Cheese Salada'])
                print('cheese Salada')
            elif opcao == 3:
                total.append(lanche['Cheese Bacon'])
                print('cheese Bacon')
            elif opcao == 4:
                total.append(lanche['Cheese Picanha'])
                print('cheese Picanha')
                sleep(0.3)
            elif opcao == 0:
                print('Não gostaria de nenhum lanche? então vamos aos próximos itens')
                sleep(0.5)
                break
            cont = str(input('Gostaria de acrescentar mais algum lanche?[S/N]')).strip().upper()
        while cont not in 'SN':
            print('opção inválida! favor digitar novamente')
            cont = str(input('Gostaria de acrescentar mais algum lanche?[S/N]')).strip().upper()
        else:
            if cont == 'N':
                sleep(0.3)
                print('Anotado! vamos aos acompanhamentos!')
                break

    break



sleep(0.5)
print("""    0: Não desejo nenhum item
    1: Batata Frita Pequena - 6.00 reais
    2: Batata Frita Grande - 10.00 reais
    3: Nuggets  - 11.00 reais
    4: Mini Salada - 8.00 reais
""")
sleep(0.3)
acomp = {'Batata Frita Pequena': 6,'Batata Frita Grande': 10,'Nuggets': 11,'Mini Salada': 8}
cont = 'SN'
total_a = []

while True:
    while True:
        sleep(0.3)
        opcao = float(input('Escolha a opção seu acompanhamento:'))
        if opcao > 4:
            sleep(0.3)
            print('opção inválida, favor digitar novamente:')
        else:
            if opcao == 1:
                total_a.append(acomp['Batata Frita Pequena'])
            elif opcao == 2:
                total_a.append(acomp['Batata Frita Grande'])
            elif opcao == 3:
                total_a.append(acomp['Nuggets'])
            elif opcao == 4:
                total_a.append(acomp['Mini Salada'])
                sleep(0.3)
            elif opcao == 0:
                print('Não gostaria de nenhum acompanhamento? então vamos aos próximos itens')
                sleep(0.5)
                break
            cont = str(input('Gostaria de acrescentar mais algum acompanhamento?[S/N]')).strip().upper()
            while cont not in 'SN':
                print('opção inválida! favor digitar novamente')
                cont = str(input('Gostaria de acrescentar mais algum acompanhamento?[S/N]')).strip().upper()
            else:
                if cont == 'N':
                    sleep(0.3)
                    print('Anotado! vamos as bebidas!')
                    break

    break


print("""   0: Não desejo nenhum item   
    1: Coca Cola  - 6.00 reais
    2: Fanta Laranja - 5.00 reais
    3: Guaraná  - 7.00 reais
    4: Sprite - 4.00 reais
    5: Suco Laranja - 6.50 reais
""")
sleep(0.3)
bebida = {'Coca Cola': 6.50, 'Fanta Laranja': 5, 'Guaraná': 7, 'Sprite': 4, 'Suco Laranja': 6.5}
cont = 'SN'
total_b = []

while True:
    while True:
        sleep(0.3)
        opcao = float(input('Escolha a opção sua bebida:'))
        if opcao > 5:
            sleep(0.3)
            print('opção inválida, favor digitar novamente:')
        else:
            if opcao == 1:
                total_b.append(bebida['Coca Cola'])
            elif opcao == 2:
                total_b.append(bebida['Fanta Laranja'])
            elif opcao == 3:
                total_b.append(bebida['Guaraná'])
            elif opcao == 4:
                total_b.append(bebida['Sprite'])
                sleep(0.3)
            elif opcao == 5:
                total_b.append(bebida['Suco Laranja'])
                sleep(0.3)
            elif opcao == 0:
                print('Não gostaria de nenhuma bebida? então vamos aos próximos itens')
                sleep(0.5)
                break
            cont = str(input('Gostaria de acrescentar mais alguma bebida?[S/N]')).strip().upper()
            while cont not in 'SN':
                print('opção inválida! favor digitar novamente')
                cont = str(input('Gostaria de acrescentar mais alguma bebida?[S/N]')).strip().upper()
            else:
                if cont == 'N':
                    sleep(0.3)
                    print('Anotado! vamos a sobremesa!')
                    break

    break


print("""    0: Não desejo nenhum item
    1: Sundae  - 10.00 reais
    2: Açai - 8.00 reais
    3: Sorvete  - 5.00 reais
    4: Mousse - 9.00 reais
""")

sleep(0.3)
sobremesa = {'Sundae': 10, 'Açai': 8, 'Sorvete': 5, 'Mousse': 9}
cont = 'SN'
total_c = []

while True:
    while True:
        sleep(0.3)
        opcao = float(input('Escolha a opção sua sobremesa:'))
        if opcao > 4:
            sleep(0.3)
            print('opção inválida, favor digitar novamente:')
        else:
            if opcao == 1:
                total_c.append(sobremesa['Sundae'])
            elif opcao == 2:
                total_c.append(sobremesa['Açai'])
            elif opcao == 3:
                total_c.append(sobremesa['Sorvete'])
            elif opcao == 4:
                total_c.append(sobremesa['Mousse'])
                sleep(0.3)
            elif opcao == 0:
                print('Não gostaria de nenhuma sobremesa? então vamos aos próximos itens')
                sleep(0.5)
                break
            cont = str(input('Gostaria de acrescentar mais alguma sobremesa?[S/N]')).strip().upper()
            while cont not in 'SN':
                print('opção inválida! favor digitar novamente')
                cont = str(input('Gostaria de acrescentar mais alguma sobremesa?[S/N]')).strip().upper()
            else:
                if cont == 'N':
                    sleep(0.3)
                    print('Anotado! vamos aos molhos!')
                    break

    break


print("""    0: Não desejo nenhum item
    1: Molho BBQ  - 2.00 reais
    2: Catchup - 1.50 reais
    3: Maionese Temperada  - 3.00 reais
    4: Mostarda especial - 2.00 reais
""")

sleep(0.3)
molho = {'Molho BBQ': 2.5, 'Catchup': 1.5, 'Maionese Temperada': 3, 'Mostarda especial': 2}
cont = 'SN'
total_d = []

while True:
    while True:
        sleep(0.3)
        opcao = float(input('Escolha a opção seu molho favorito:'))
        if opcao > 4:
            sleep(0.3)
            print('opção inválida, favor digitar novamente:')
        else:
            if opcao == 1:
                total_d.append(molho['Molho BBQ'])
            elif opcao == 2:
                total_d.append(molho['Catchup'])
            elif opcao == 3:
                total_d.append(molho['Maionese Temperada'])
            elif opcao == 4:
                total_d.append(molho['Mostarda especial'])
                sleep(0.3)
            elif opcao == 0:
                print('Não gostaria de nenhum molho? então vamos aos próximos itens')
                sleep(0.5)
                break
            cont = str(input('Gostaria de acrescentar mais algum molho?[S/N]')).strip().upper()
            while cont not in 'SN':
                print('opção inválida! favor digitar novamente')
                cont = str(input('Gostaria de acrescentar mais algum molho?[S/N]')).strip().upper()
            else:
                if cont == 'N':
                    sleep(0.3)
                    print('Anotado! vamos ao pagamento!')
                    break

    break



print(total, total_a, total_b, total_c, total_d)

tot = total
tot_a = total_a
tot_b = total_b
tot_c = total_c
tot_d = total_d

conta = (tot + tot_c + tot_b + tot_a + tot_d)
print(f'O total da conta deu: {sum(conta)} reais')

