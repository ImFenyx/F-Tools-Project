#coding=utf-8

"""
TODO: Migrate Aleph-0 features to F-Tools / Migrar funções do Aleph-0 para F-Tools
"""
# imports
import time
import os
import random
import math

# initial menu / menu inicial

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
    time.sleep(2)
    menu()

# Clear Screen / Limpa tela
def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear') 

# Tools Menu / Menu de ferramentas
def menu():
    clear()
    print ('\n\n######################################\n\n     > Opções para ferramentas <     \n\n######################################')
    print ('\n(1) Ferramentas de texto\n(2) Ferramentas de cálculos\n\n[Em progresso: ]\n(3) Conversão de unidades\n(4) Ferramentas de cores\n(5) Ferramentas de randomização')
    opcao_menu = input('\n> ')
    
    # Text Tools / Ferramentas de texto
    if not opcao_menu: # Para não crashar
        menu()
    if opcao_menu == '1':
        print ('\n(1) Contador de caracteres\n(2) Repetir textos\n(3) Conversão de caixa de texto\n(4) Inverter texto')
        opc_text_tools = input('\n> ')
        
        if not opc_text_tools: # Para não crashar
            menu()
        # Character Counter / Contador de caracteres
        if opc_text_tools == '1':
            clear()
            print('\n\nEscreva seu texto:')
            text = input('\n> ')
            if not text:
                menu()
            text1 = text.replace(' ', '')
            print(f'\nSeu texto contém {len(text1)} caracteres sem espaços e {len(text)} com espaços')
            input("Pressione qualquer tecla para continuar...")
            menu()
            
        # Text repeat / Repetir textos
        elif opc_text_tools == '2':
            clear()
            print('\nEscreva seu texto:')
            text = input('\n> ')
            if not text:
                menu()
            print('\nQuantas repetições?')
            repeat = int(input('\n> '))
            if not repeat:
                menu()
            print('\nCom espaço ou por linhas?\n\n(1) Espaço\n(2) Linhas')
            space = (input('\n> '))
            if not space:
                menu()
            if space == '1':
                print(f'\n{text * repeat}')
                input("Pressione qualquer tecla para continuar...")
                menu()
            elif space == '2':
                print()
                for i in range(repeat):
                    print(text)
                input("Pressione qualquer tecla para continuar...")
                menu()
                
        # Textcase Converter / Conversão de caixa de texto
        elif opc_text_tools == '3':
            clear()
            print('\nEscreva seu texto:')
            text = input('\n> ')
            if not text:
                menu()
            print('\nEm maiúsculo ou minúsculo?\n\n(1) Maiúsculo\n(2) Minúsculo')
            text_case = (input('\n> '))
            if not text_case:
                menu()
            if text_case == '1':
                text_max = text.upper()
                print(f'\n{text_max}')
                input("Pressione qualquer tecla para continuar...")
                menu()
            elif text_case == '2':
                text_min = text.lower()
                print(f'\n{text_min}')
                input("Pressione qualquer tecla para continuar...")
                menu()
                
        # Text Invert / Inverter texto
        elif opc_text_tools == '4':
            clear()
            print('\nEscreva seu texto:')
            text = input('\n> ')
            if not text:
                menu()
            print()
            print(text[::-1])
            input("Pressione qualquer tecla para continuar...")
            menu()
            
    # Calc Tools / Ferramentas de cálculos
    elif opcao_menu == '2':
        print ('\n(1) Porcentagem\n(2) Média\n(3) Proporção de imagem\n(4) Números primos\n(5) Números aleatórios\n(6) Potenciação\n(7) Velocidade média\n(8) Equação do primeiro grau\n(9) Equação do segundo grau')
        opc_calc_tools = input('\n> ')
        if not opc_calc_tools:
            menu()
        
        # Porcentage / Porcentagem
        if opc_calc_tools == '1':
            clear()
            print('\nPorcentagem (%)')
            porcentagem = input('\n> ')
            if not porcentagem:
                menu()
            print('\nde qual número?')
            num = input('\n> ')
            if not num:
                menu()
            # Check if num is integer or float /Checa se num é inteiro ou flutuante
            if num.isdigit() and num.find(".") == -1:
                num = int(num)
            else:
                num = float(num)
            # Check if porcentage is integer or float / Checa se porcentagem é inteiro ou flutuante
            if porcentagem.isdigit() and porcentagem.find(".") == -1:
                porcentagem = int(porcentagem)
            else:
                porcentagem = float(porcentagem)
            res = (num * porcentagem) / 100
            # Check if res is integer / Checa se res é inteiro
            if res.is_integer():
                res = int(res)
            print(res)
            input("Pressione qualquer tecla para continuar...")
            menu()
            
        # Average / Média
        elif opc_calc_tools == '2':
            clear()
            num = input("Digite números separados por vírgulas (Ex.: 10,20,30): ")
            if not num:
                menu()
            # Split the numbers by commas / Separa o numeros pela virgulas
            lista_numeros = num.split(',')
            # Convert all list numbers to integers / Converte todos os números da lista para inteiros
            lista_numeros = [int(num) for num in lista_numeros]
            quantidade = len(lista_numeros)
            soma = sum(lista_numeros)
            media = (soma/quantidade)
            print (f"\nSoma:{soma}\nMédia aproximadamente: {media:.2f}\nVocê digitou {quantidade} números.")
            input("Pressione qualquer tecla para continuar...")
            menu()
            
        # Aspect Ratio / Proporção de imagem
        elif opc_calc_tools == '3':
            clear()
            print ('\nMe diga a largura')
            h = int(input('\n> '))
            if not h:
                menu()
            print ('\nMe diga a altura')
            w = int(input('\n> '))
            if not w:
                menu()
            # GCD Calc / Calcula o MDC
            mdc = math.gcd(h, w)
            # Divide the width and height by GCD to get a simplified aspect ratio / Divide a altura e a largura pelo MDC para obter a proporção simplificada
            res1 = h // mdc
            res2 = w // mdc
            # Verify if the aspect ratio is usualy rounded / Verifica se a proporção é uma das proporções comuns que são frequentemente arredondadas
            if (res1, res2) in [(64, 27), (43, 18)]:
                res = '21:9'
            elif (res1, res2) == (8, 5):
                res = '16:10 / 8:5'
            else:
                res = f'{res1}:{res2}'
            print (f'\n{res}')
            input("Pressione qualquer tecla para continuar...")
            menu()
        # Prime numbers / Números primos
        elif opc_calc_tools == '4':
            clear()
            print ('\nMe diga um número primo')
            primo = int(input('\n> '))
            if primo > 1:
                for i in range(2, primo):
                    if primo % i == 0:
                        print(f'\n{primo} não é primo')
                        input("Pressione qualquer tecla para continuar...")
                        menu()
                        break
                else:
                    print(f'\n{primo} é primo')
                    input("Pressione qualquer tecla para continuar...")
                    menu()
            elif primo == 0:
                print(f'\n{primo} é zero')
                input("Pressione qualquer tecla para continuar...")
                menu()
            elif primo == 1:
                print(f'\n{primo} é um')
                input("Pressione qualquer tecla para continuar...")
                menu()
            else:
                print(f'\n{primo} é negativo')
                input("Pressione qualquer tecla para continuar...")
                menu()
        # Random numbers / Numeros aleatórios
        elif opc_calc_tools == '5':
            rm1 = int(input("\n\nQual número mínimo para escolher?\n\n> "))
            if not rm1:
                menu()
            rm2 = int(input("\n\nQual número máximo para escolher?\n\n> "))
            if not rm2:
                menu()
            print(f"\n\nEu escolho:\n-> {random.randint(rm1, rm2)}")
            input("Pressione qualquer tecla para continuar...")
            menu()
        # Potentiation / Potenciação
        elif opc_calc_tools == '6':
            ptcbase = float(input("\nqual o número base?\n\n-> "))
            if not ptcbase:
                menu()
            ptcexp = float(input("\nqual o expoente?\n\n-> "))
            if not ptcexp:
                menu()
            ptcbase_exp = (ptcbase ** ptcexp)
            print (f"\n\nA resposta é: {ptcbase_exp}")
        # Average speed, time, distance / Velocidade, tempo e distância média 
        elif opc_calc_tools == '7':
            grandeza = input("Você quer descobrir qual grandeza?:\n\n(1) Velocidade\n\n(2) Tempo\n\n(3) Distância\n\n> ")
            if not grandeza:
                menu()
            elif grandeza == '1':
                clear()
                velocidade_distancia = float(input("Qual o tempo em segundos?\n\n-> "))
                tempo_distancia = float(input("Qual a distancia em metros?\n\n-> "))
                t_resultado_m = (velocidade_distancia / tempo_distancia)
                t_resultado_km = (t_resultado_m * 3.6)
                print ("A resposta em m/s é:", t_resultado_m,"\nAgora em Km/h é:", t_resultado_km)
                input("Pressione qualquer tecla para continuar...")
                menu()
            elif grandeza == '2':
                clear()
                velocidade_tempo = float(input("Qual a velocidade em m/s?\n\n-> "))
                distancia_tempo = float(input("Qual a distancia em metros?\n\n-> "))
                t_resultado_segundos = (distancia_tempo / velocidade_tempo)
                t_resultado_minutos = (t_resultado_segundos / 60)
                t_resultado_horas = (t_resultado_segundos / 3600)
                print (f"A resposta em segundos é: {t_resultado_segundos}\nEm minutos é: {t_resultado_minutos}\nAgora em horas é: {t_resultado_horas}")
                input("Pressione qualquer tecla para continuar...")
                menu()
            elif grandeza == '3':
                clear()
                velocidade_distancia = float(input("Qual a velocidade em m/s?\n\n-> "))
                tempo_distancia = float(input("Qual o tempo em segundos?\n\n-> "))
                t_resultado_m = (velocidade_distancia * tempo_distancia)
                t_resultado_km = (t_resultado_m / 1000)
                print ("A resposta em metros é:", t_resultado_m,"\nAgora em km é:", t_resultado_km)
                input("Pressione qualquer tecla para continuar...")
                menu()
        # Linear equation / equação linear
        elif opc_calc_tools == '8':
            co_a = float(input("digite o coeficiente A: "))
            co_b = float(input("digite o coeficiente B: "))
            r = (-co_b) / co_a
            print (f"A raiz é: {r}")
            input("Pressione qualquer tecla para continuar...")
            menu()
        # Quadratic equation / Equação quadrática
        elif opc_calc_tools == '9':
            co_a = float(input("digite o coeficiente A: "))
            co_b = float(input("digite o coeficiente B: "))
            co_c = float(input("digite o coeficiente C: "))

            delta = (co_b ** 2) - (4 * co_a * co_c)
            if delta < 0:
                print ("\n\nA equação não tem raizes reais")
                input("Pressione qualquer tecla para continuar...")
                menu()
            elif delta == 0:
                x0 = (-co_b) / (2 * co_a)
                print (f'\n\nA única raiz é essa: {x0}')
                input("Pressione qualquer tecla para continuar...")
                menu()
        else:
            x1 = ((-co_b) + math.sqrt(delta)) / (2 * co_a)
            x2 = ((-co_b) - math.sqrt(delta)) / (2 * co_a)
            print (f"\n\nPrimeira raiz é {x1} e a Segunda raiz é {x2}")
            input("Pressione qualquer tecla para continuar...")
            menu()


    else:
        print("Opção errada")
        input("Pressione qualquer tecla para continuar...")
        menu()
bf_menu()