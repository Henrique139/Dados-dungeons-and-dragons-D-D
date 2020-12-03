#=============HENRIQUE==============#
#==============CÉSAR================#

#Código

from tkinter import *
import random
#/\importações usadas no script

#\/-Tela
janela=Tk()
janela.title("DADOS")
janela.attributes("-fullscreen",True)
janela["bg"]="white"


#Funções usadas no script    

def escuro():    
    lb["bg"]="black"
    lb2["bg"]="black"
    lb3["bg"]="black"
    lb4["bg"]="black"
    lb5["bg"]="black"
    lb6["bg"]="black"
    lb7["bg"]="black"
    bf["bg"]="black"
    titulo["bg"]="black"
    janela["bg"]="black"
    lb["fg"]="white"
    lb2["fg"]="white"
    lb3["fg"]="white"
    lb4["fg"]="white"
    lb5["fg"]="white"
    lb6["fg"]="white"
    lb7["fg"]="white"    
    bf["fg"]="white"
    titulo["fg"]="white"    
    
def claro():
    lb["bg"]="white"
    lb2["bg"]="white"
    lb3["bg"]="white"
    lb4["bg"]="white"
    lb5["bg"]="white"
    lb6["bg"]="white"
    lb7["bg"]="white"    
    bf["bg"]="white"    
    lb["fg"]="black"
    lb2["fg"]="black"
    lb3["fg"]="black"
    lb4["fg"]="black"
    lb5["fg"]="black"
    lb6["fg"]="black"
    lb7["fg"]="black"  
    bf["fg"]="black"
    titulo["fg"]="black"    
    titulo["bg"]="white"
    janela["bg"]="white"
        
def sair():
    janela.destroy()

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

#tentativa de gerar número customizado 
    try:
        bf["fg"]="black"
        pa1=int(p1.get())
        pa2=int(p2.get())  
        bf["text"]=random.randint(pa1,pa2)

#caso ocorra algum erro               
    except:
        bf["text"]="ERRO!"

#fim das funções
                
#Título
titulo=Label(janela,width=85,text="DADOS"+" \n"+"DUNGEONS AND DRAGONS")
titulo.pack(side=TOP)

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

#Botão do modo claro 

bt6=Button(janela,width=5,text="claro",command=claro)
bt6.place(x=473,y=700)

#Botão do modo escuro

bt7=Button(janela,width=5,text="escuro",command=escuro)
bt7.place(x=473,y=800)

#Botão de sair

sair=Button(janela,width=36,height=2,text="F E C H A R",command=sair)
sair.pack(side=BOTTOM)

#cor padrão

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
