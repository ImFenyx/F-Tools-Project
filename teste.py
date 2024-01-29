#coding=ansi

# import time

# print ('F-Tools Project')
# print ('Carregando 0%\n')
# time.sleep(1)
# print ('Carregando 100%\n\n')
# time.sleep(1)

print ('######################################\n\n      > Opções para ferramentas < \n\n######################################')
print ('\n(1) Ferramentas de texto\n(2) Ferramentas de cálculos\n(3) Conversão de unidades\n(4) Ferramentas de cores\n(5) Ferramentas de randomização')
opcao_menu = input('\n>')
if opcao_menu == '1':
    opc_textcounter = input('\n(1) Text Counter\n \n>')
    if opc_textcounter == '1':
        print('Escreva seu texto:')
        text = input('\n>')
        text1 = text.replace(' ', '')
        print(f'\nSeu texto contém {len(text1)} caracteres sem espaços e {len(text)} com espaços')
        input()