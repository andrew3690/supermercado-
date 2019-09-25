from tkinter import *
from tkinter import font  as tkfont # python 3
import tkinter as tk

class Aplicativo(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)


        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Supermercado,Compras,Pagamento):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Supermercado)

    def show_frame(self, cont):
        frame = self.frames[cont]		
        frame.tkraise()
       	frame["bg"] ="black"  ## Cor de background das telas 
 
class Supermercado(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self,bg = "Blue",text="Supermercado")
		label.place(y=100,x=600)

		button = tk.Button(self, text="Compras",bg = "blue", command=lambda: controller.show_frame(Compras))
		button.place(x = 600 , y = 200)
		

compras = []

dicionario = {"Banana": 2,
"Leite":2,
"Chocolate":5,
"Monster":7,
"Queijo":6,
"Danoninho Ice": 5,
"Pao":1,
"Carne":10}

def Compra(x):
	compras.append(x)


class Compras(tk.Frame):
	def __init__(self, parent, controller):
		self._Produtos = []
		self._precoTotal = 0


		tk.Frame.__init__(self, parent)
		label = tk.Label(self,bg = "Blue",text="Compras")
		label.place(y=0,x=650)


		button1 = tk.Button(self,bg = "Blue",text="VOLTAR",command=lambda: controller.show_frame(Supermercado)) ## Botao para voltar para o menu principal
		button1.place(x= 0 , y = 0)

		## Botoes para seleçao de itens 

		##Comidas 
		Com = tk.Label(self,bg="Brown",text="Comidas")
		Com.place(x = 500,y = 60)

		Pao = tk.Button(self,bg ="Brown",text="Pao",command = lambda:Compra("Pao"))
		Pao.place(x=500,y=100) 

		Carne =tk .Button(self,bg="Red",text="Carne",command= lambda:Compra("Carne"))
		Carne.place(x=500,y=150)

		##Frutas 
		Fruta = tk.Label(self,bg="yellow",text="Frutas")
		Fruta.place(x = 100,y = 60)

		Banana = tk.Button(self,bg = "yellow",text = "Banana", command = lambda:Compra("Banana")) 
		Banana.place(x=100,y=100)

		## Liquidos
		Refr = tk.Label(self,bg="Green",text="Refrigerantes/Bebidas")
		Refr.place(x = 300,y = 60)

		Monster = tk.Button(self,bg="Green",text="Monster",command = lambda:Compra("Monster"))
		Monster.place(x=300,y=100)

		## Laticinios
		Lat = tk.Label(self,bg="orange",text="Laticinios")
		Lat.place(x = 100,y = 260)

		Danoninho = tk.Button(self,bg="Pink",text="Danoninho Ice",command = lambda:Compra("Danoninho Ice"))
		Danoninho.place(x =100,y=350)

		Chocolate = tk.Button(self,bg = "Brown",text = "Chocolate", command = lambda:Compra("Chocolate")) 
		Chocolate.place(x=100,y=400)

		Queijo = tk.Button(self,bg="orange",text="Queijo",command = lambda:Compra("Queijo"))
		Queijo.place(x=100,y=300)

		Leite = tk.Button(self,bg = "white",text = "Leite", command = lambda:Compra("Leite")) 
		Leite.place(x=100,y=450)

		## Preço final 
		def comprar():
			for i in range(len(compras)):
				self._precoTotal += dicionario[compras[i]]

		Label = tk.Label(self,bg="Purple",text="PRECO FINAL:")
		Label["text"] = "PRECO FINAL: " + str(comprar()) ## Falta Atualizar o valor a cada valor somado
		Label.place(x=100,y=600)

		button = tk.Button(self, text="PAGAR",bg = "blue", command=lambda: controller.show_frame(Pagamento))
		button.place(x = 250 , y = 600)

class Pagamento(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Pagamento")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self,bg="blue",text="VOLTAR",command=lambda: controller.show_frame(Compras))
       	button1.place(x=0,y=0)	

       	Pag = tk.Label(self,bg="Blue",text="ESCOLHA A OPÇAO DE PAGAMENTO")
       	Pag.place(x=100,y=100)

       	Cartao = tk.Label(self,bg="orange",text="VISA/MASTERCAD",) ## Inserir pagamento via cartao 
       	Cartao.place(x = 100 , y = 150)							   ## se o tamanho da senha menor ou maior que 4 ,mostrar mensagem invalida  
       	

       	Dinheiro = tk.Label(self,bg="Green",text="Dinheiro") ## Inserir valor em reais maior ou igual ao preco total 
       	Dinheiro.place(x=250,y=150)							 ## Se valor menor que o preço total mostrar mensagem invalida 


app = Aplicativo()
app.mainloop()