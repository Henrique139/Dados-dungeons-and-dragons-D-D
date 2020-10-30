#=============HENRIQUE==============#
#==============CÉSAR================#

#Código

from tkinter import *
import random
import sys
import os
#/\importações usadas no script

#\/-Tela
janela=Tk()
janela.title("DADOS D&D")
janela.attributes("-fullscreen",True)



#Funções usadas no script    

def sair():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def D4():
    lb["text"]=random.randint(1,4)

def D6():
    lb2["text"]=random.randint(1,6)
    
def D8():
   lb3["text"]=random.randint(1,8)

def D10():
    lb4["text"]=random.randint(1,10)
    
def D12():
   lb5["text"]=random.randint(1,12)
    
def D20():
    lb6["text"]=random.randint(1,20)
    
def custom():    
    pa1=int(p1.get())
    pa2=int(p2.get())  
    bf["text"]=random.randint(pa1,pa2)
    
        
#Título
titulo=Label(janela,width=85,text="DADOS D&D")
titulo.place(x=-450,y=45)

#Botão D4
bt=Button(janela,width=5,text="D4",command=D4)
bt.place(x=30,y=290)

#Número exibido pelo do D4
lb=Label(janela,text="0")
lb.place(x=230,y=290)

#Botão D6
bt2=Button(janela,width=5,text="D6",command=D6)
bt2.place(x=30,y=370)

#Número exibido pelo D6
lb2=Label(janela,text="0")
lb2.place(x=230,y=370)

#Botão D8
bt3=Button(janela,width=5,text="D8",command=D8)
bt3.place(x=30,y=450)

#Número exibido pelo D8
lb3=Label(janela,text="0")
lb3.place(x=230,y=450)

#Botão D10
bt4=Button(janela,width=5,text="D10",command=D10)
bt4.place(x=30,y=530)

#Número exibido pelo D10
lb4=Label(janela,text="0")
lb4.place(x=230,y=530)

#Botão D12
bt5=Button(janela,width=5,text="D12",command=D12)
bt5.place(x=30,y=610)

#Número exibido pelo D12
lb5=Label(janela,text="0")
lb5.place(x=230,y=610)

#Botão D20
bt6=Button(janela,width=5,text="D20",command=D20)
bt6.place(x=30,y=690)

#Número exibido pelo D20
lb6=Label(janela,text="0")
lb6.place(x=230,y=690)


#PARTE CUSTOMIZÁVEL

#Título da parte customizável
lb7=Label(janela,text="Customize")
lb7.place(x=470,y=240)

#Parâmetro 1
p1=Entry(janela,width=10)
p1.place(x=460,y=290)

#Parâmetro 2
p2=Entry(janela,width=10)
p2.place(x=460,y=370)

#Botão para Executar o dado customizado
bc=Button(janela,width=5,text="JOGAR",command=custom)
bc.place(x=473,y=430)

#Número exibido pelo dado customizado
bf=Label(janela,width=5,text="0")
bf.place(x=500,y=530)

#FIM DA PARTE CUSTOMIZÁVEL

#Botão de sair
sair=Button(janela,width=5,text="SAIR",command=sair)
sair.place(x=30,y=870)

#cores

p1["bg"]="light gray"
p2["bg"]="light gray"
lb["bg"]="white"
lb2["bg"]="white"
lb3["bg"]="white"
lb4["bg"]="white"
lb5["bg"]="white"
lb6["bg"]="white"
lb7["bg"]="white"
bf["bg"]="white"
titulo["bg"]="white"
janela["bg"]="white"


janela.mainloop()


#===============FIM==================#
