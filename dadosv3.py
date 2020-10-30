import sys
import os
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
#/\-comandos para permitir o uso de 'restart program'    
    

#D4,6,8,10,12,20

#Menu
print("\n"+"   1-D4"+"\n"+"   2-D6"+"\n"+"   3-D8"+"\n"+"   4-D10"+"\n"+"   5-D12"+"\n"+"   6-D20"+"\n"+"   7-CUSTOMIZÁVEL")

#Instruções
print("\n"+"  DIGITE '8' PARA CONSULTAR AS INSTRUÇÕES ")

#Variável usada para gerar número aleatório
dado=int(input("\n"+"  DIGITE UMA OPÇÃO: "))
import random        
#/\=importação do comando random(usado para gerar um número aleatório)  

#IF's

#D4
if (dado)==1:
    print("  O número sorteado no D4 foi ", random.randrange(1,5))
         
#D6                                    
if dado==2:
  print("  O número sorteado no D6 foi ",random.randrange(1,7))
    
#D8
if dado==3:
    print("  O número sorteado no D8 foi ",random.randrange(1,9))
      
#D10
if dado==4:
    print("  O número sorteado no D10 foi ",random.randrange(1,11))
      
#D12
if dado==5:
  print("  O número sorteado no D12 foi ",random.randrange(1,13))
   
#D20
if dado==6:
      print("  O número sorteado no D20 foi ",random.randrange(1,21))
      
 
#customização 
if dado==7:
    dado1=int(input("\n"+"   DIGITE O VALOR DO PRIMEIRO NÚMERO: "))
#variável do primeiro número

    dado2=int(input("\n"+"   DIGITE O VALOR DO SEGUNDO NÚMERO: "))
#variável do segundo número

    dado3=dado2+1
#variável usada para equilibrar o segundo número com o 'comando randrange'' 
    print("\n"+"   O NÚMERO SORTEADO ENTRE {} E {} FOI {}".format(dado1,dado2,random.randrange(dado1,dado3)))
    #comando usado para exibir o resultado    
     
#IF das instruções
if dado==8:
    print("\n"+"   Você deve selecionar o número referente ao dado que deseja."+"\n"+"   O número se encontra ao lado esquerdo do nome do dado")
    input("")
    #-input para dividir instruções do reinicio
    restart_program()

#if para reiniciar programa após uso
if dado==1 or 2 or 3 or 4 or 5 or 6 or 7:
     input("")   
     op=int(input("\n"+"   VOCÊ DESEJA CONTINUAR USANDO O PROGRAMA? "+"\n"+"   1-SIM"+"\n"+"   2-NÃO"+"\n"+"   DIGITE UMA OPÇÃO: "))
#variável usada para identificar a escolha do usuário 

#\/caso o programa não drva reiniciar 
if op==2:
    print("\n"+"       PROGRAMA FINALIZADO ")
    (exit())

#caso o usuario queira usar o programa novamente 
if op==1:
    restart_program()

#caso não seja digitada uma opção válida
else:
    print("   Opção inválida ")    
    (exit())

#Fim do programa
  
#==============Henrique===============#
 