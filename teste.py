#coding=ansi

# import time

# print ('F-Tools Project')
# print ('Carregando 0%\n')
# time.sleep(1)
# print ('Carregando 100%\n\n')
# time.sleep(1)

print ('######################################\n\n      > Op��es para ferramentas < \n\n######################################')
print ('\n(1) Ferramentas de texto\n(2) Ferramentas de c�lculos\n(3) Convers�o de unidades\n(4) Ferramentas de cores\n(5) Ferramentas de randomiza��o')
opcao_menu = input('\n>')
if opcao_menu == '1':
    opc_textcounter = input('\n(1) Text Counter\n \n>')
    if opc_textcounter == '1':
        print('Escreva seu texto:')
        text = input('\n>')
        text1 = text.replace(' ', '')
        print(f'\nSeu texto cont�m {len(text1)} caracteres sem espa�os e {len(text)} com espa�os')
        input()