#simple calculater
import tkinter
root=tkinter.Tk()
root.title('Calculater')
#creat fuction
expresion=""
def add(value):
    global expresion
    expresion +=value
    result.config(text=expresion)

def clear():
    global expresion
    expresion=""
    result.config(text=expresion)

def calculate():
    global expresion
    r=""
    if expresion !="":
        try:
            r=eval(expresion)
        except:
            r="error"
            expresion=""
    result.config(text=r)        
            



    
#create GUI
result=tkinter.Label(root,text='result',height=2)
result.grid(row=0,column=0,columnspan=4)

butten_1=tkinter.Button(root,text="1",width=12,height=2,command=lambda: add("1"))
butten_1.grid(row=1,column=0)


butten_2=tkinter.Button(root,text="2",width=12,height=2,command=lambda: add("2"))
butten_2.grid(row=1,column=1)

butten_3=tkinter.Button(root,text="3",width=12,height=2,command=lambda: add("3"))
butten_3.grid(row=1,column=2)

butten_divide=tkinter.Button(root,text="/",width=12,height=2,command=lambda: add("/"))
butten_divide.grid(row=1,column=3)
#--------------------
butten_4=tkinter.Button(root,text="4",width=12,height=2,command=lambda: add("4"))
butten_4.grid(row=2,column=0)

butten_5=tkinter.Button(root,text="5",width=12,height=2,command=lambda: add("5"))
butten_5.grid(row=2,column=1)

butten_6=tkinter.Button(root,text="6",width=12,height=2,command=lambda: add("6"))
butten_6.grid(row=2,column=2)

butten_mul=tkinter.Button(root,text="X",width=12,height=2,command=lambda: add("*"))
butten_mul.grid(row=2,column=3)

#-----------------------------------

butten_7=tkinter.Button(root,text="7",width=12,height=2,command=lambda: add("7"))
butten_7.grid(row=3,column=0)

butten_8=tkinter.Button(root,text="8",width=12,height=2,command=lambda: add("8"))
butten_8.grid(row=3,column=1)

butten_9=tkinter.Button(root,text="9",width=12,height=2,command=lambda: add("9"))
butten_9.grid(row=3,column=2)

butten_sub=tkinter.Button(root,text="-",width=12,height=2,command=lambda: add("-"))
butten_sub.grid(row=3,column=3)

#---------------------------------------
butten_clear=tkinter.Button(root,text="C",width=12,height=2,command=lambda: clear())
butten_clear.grid(row=4,column=0)

butten_dot=tkinter.Button(root,text=".",width=12,height=2,command=lambda: add("."))
butten_dot.grid(row=4,column=1)

butten_0=tkinter.Button(root,text="0",width=12,height=2,command=lambda: add("0"))
butten_0.grid(row=4,column=2)

butten_add=tkinter.Button(root,text="+",width=12,height=2,command=lambda: add("+"))
butten_add.grid(row=4,column=3)


butten_equal=tkinter.Button(root,text="=",width=12,height=2,command=lambda: calculate())
butten_equal.grid(row=5,column=0,columnspan=4)


#-----------------------------------

root.mainloop()
