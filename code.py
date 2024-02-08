#coding=utf-8

# imports
import time
import os
import math

def bf_menu():
    print(r"""
                 @@@@@@@@@@@@@@@@                 
                @@@@@@@@@@@@@@@@@@@@@@            
          @%   :@@@@@@@@@@@@@@@@@@@@@@@@          
          @-   :@@@@@@=:@@@@@@@@@@@@@@@@@@@       
         -@*    @@@@@@@:  =%@@@@@@@@@@@@@@@@      
    @    :@@     @@@@@@@%         @@@@@@@@@@@@    
   @@:   :*@*    :@@@@@@%     =%=  :@@@@@@@@@@@   
  @@@%    :@@-    :@@@@@:             %@@@@@@@@@  
 @@@@@*    :@@%     %@@@       %@@@@@@%@@@@@@@@@@ 
  @@@@@@     =@@:    -@@*     @@@@@@@@@@@@@@@@@@@@
   *@@@@@*     =@@*   :@@      @@@@@@@@@@@@@@@@@@@
     *@@@@@%:      *@* *@*      =@@@@@@@@@@@@@@@@@
       :%@@@@@@*       %@@       *@@@@@@@@@@@@@@@@
::           :%@@*:   %@@         @@@@@@@@@@@@@@@@          F-Tools Project
=::::              :%@@@-   %     @@@@@@@@@@@@@@@@          v0.1p
@@@=:::::::::::-*@@@@@*    @  *   @@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@*     %@  *   @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@=:      =@@- :*   @@@@@@@@@@@@@@@@@@
 @@@@@%*:         %@@@*   @-  *@@@@@@@@@@@@@@@@@@ 
              *@@@@-     @@=@@@@@@@@@@@@@@@@@@@@  
           :@@@@@:  ==   @@@@@@@@@@@@@@@@@@@@@@   
    ::::::=@@@@@   @%:   :@@@@@@@@@@@@@@@@@@*:    
      ::::@@@@@:  @@*::    :%@@@@@@@@@@@*:        
       :::@@@@@: -@@@:::                          
          @@@@@@ :@@@@::::            -*          
            @@@@@*@@@@@%=::::::::-*%@@            
                 @@@@@@@@@@@@@@@@                  Por favor não pressione nenhuma tecla ^-^
                 """)
    time.sleep(3)
    menu()
    
def menu():
    os.system('cls')
    print ('\n\n######################################\n\n     > Opções para ferramentas <     \n\n######################################')
    print ('\n(1) Ferramentas de texto\n(2) Ferramentas de cálculos\n\n[Ainda não terminados: ]\n(3) Conversão de unidades\n(4) Ferramentas de cores\n(5) Ferramentas de randomização')
    opcao_menu = input('\n> ')
    # Opção de ferramentas de texto
    if opcao_menu == '1':
        print ('\n(1) Contador de caracteres\n(2) Repetir textos\n(3) Conversão de caixa de texto\n(4) Inverter texto')
        opc_text_tools = input('\n> ')
        # Contador de caracteres
        if opc_text_tools == '1':
            os.system('cls')
            print('\n\nEscreva seu texto:')
            text = input('\n> ')
            text1 = text.replace(' ', '')
            print(f'\nSeu texto contém {len(text1)} caracteres sem espaços e {len(text)} com espaços')
            input()
            menu()
        # Repetir textos
        elif opc_text_tools == '2':
            os.system('cls')
            print('\nEscreva seu texto:')
            text = input('\n> ')
            print('\nQuantas repetições?')
            repeat = int(input('\n> '))
            print('\nCom espaço ou por linhas?\n\n(1) Espaço\n(2) Linhas')
            space = (input('\n> '))
            if space == '1':
                print(f'\n{text * repeat}')
                input()
                menu()
            elif space == '2':
                print()
                for i in range(repeat):
                    print(text)
                input()
                menu()
        # Conversão de caixa de texto
        elif opc_text_tools == '3':
            os.system('cls')
            print('\nEscreva seu texto:')
            text = input('\n> ')
            print('\nEm maiúsculo ou minúsculo?\n\n(1) Maiúsculo\n(2) Minúsculo')
            text_case = (input('\n> '))
            if text_case == '1':
                text_max = text.upper()
                print(f'\n{text_max}')
                input()
                menu()
            elif text_case == '2':
                text_min = text.lower()
                print(f'\n{text_min}')
                input()
                menu()
        # Inverter texto
        elif opc_text_tools == '4':
            os.system('cls')
            print('\nEscreva seu texto:')
            text = input('\n> ')
            print()
            print(text[::-1])
            input()
            menu()
    # Opção de ferramentas de cálculos
    elif opcao_menu == '2':
        print ('\n(1) Porcentagem\n(2) Média\n(3) Proporção de imagem\n(4) Números primos')
        opc_calc_tools = input('\n> ')
        # Porcentagem
        if opc_calc_tools == '1':
            os.system('cls')
            print('\nPorcentagem (%)')
            porcentagem = input('\n> ')
            print('\nde qual número?')
            num = input('\n> ')
            # Checa se num é inteiro ou flutuante
            if num.isdigit() and num.find(".") == -1:
                num = int(num)
            else:
                num = float(num)
            # Checa se porcentagem é inteiro ou flutuante
            if porcentagem.isdigit() and porcentagem.find(".") == -1:
                porcentagem = int(porcentagem)
            else:
                porcentagem = float(porcentagem)
            res = (num * porcentagem) / 100
            # Checa se res é inteiro
            if res.is_integer():
                res = int(res)
            print(res)
            input()
            menu()
        # Média
        elif opc_calc_tools == '2':
            os.system('cls')
            num = input("Digite números separados por vírgulas (Ex.: 10,20,30): ")
            # Separa o numeros pela virgulas
            lista_numeros = num.split(',')
            # Converte todos os números da lista para inteiros
            lista_numeros = [int(num) for num in lista_numeros]
            # Variáveis
            quantidade = len(lista_numeros)
            soma = sum(lista_numeros)
            media = (soma/quantidade)
            # Resultado
            print (f"\nSoma:{soma}\nMédia aproximadamente: {media:.2f}\nVocê digitou {quantidade} números.")
            input()
            menu()
            # Proporção de imagem
        elif opc_calc_tools == '3':
            os.system('cls')
            print ('\nMe diga a largura')
            h = int(input('\n> '))
            print ('\nMe diga a altura')
            w = int(input('\n> '))

            # Calcula o MDC
            mdc = math.gcd(h, w)

            # Divide a altura e a largura pelo MDC para obter a proporção simplificada
            res1 = h // mdc
            res2 = w // mdc

            # Verifica se a proporção é uma das proporções comuns que são frequentemente arredondadas
            if (res1, res2) in [(64, 27), (43, 18)]:
                res = '21:9'
            elif (res1, res2) == (8, 5):
                res = '16:10 / 8:5'
            else:
                res = f'{res1}:{res2}'

            print (f'\n{res}')
            input()
            menu()
        elif opc_calc_tools == '4':
            os.system('cls')
            print ('\nMe diga um número primo')
            primo = int(input('\n> '))

            if primo > 1:
                for i in range(2, primo):
                    if primo % i == 0:
                        print(f'\n{primo} não é primo')
                        input()
                        menu()
                        break
                else:
                    print(f'\n{primo} é primo')
                    input()
                    menu()
            elif primo == 0:
                print(f'\n{primo} é zero')
                input()
                menu()
            elif primo == 1:
                print(f'\n{primo} é um')
                input()
                menu()
            else:
                print(f'\n{primo} é negativo')
                input()
                menu()
bf_menu()
