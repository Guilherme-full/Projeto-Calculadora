import tkinter as tk
import math

botao_config = {
    "bg":"#8B0000",
    "fg":"#FFF8DC",
    "font":("consolas bold", 12),
    "height":"2",
    "width":"7",
    "relief":"raised",
    "activebackground":"#8B0000"
}

digitos = ["√", "x²","Limpar","π","n!","sin","cos","tan","sin-¹","cos-¹","cos-¹","tan-¹"]

deg = 1
inversa_deg = 1
cnt = 0

class Calculadora:
    def __init__(self, master):
        self.calc = master
        self.calc.title("Calculadora Científica - Projeto Guilherme Xavier")
        self.displayFrame = tk.Frame(self.calc)
        self.displayFrame.pack()
        self.buttonsFrame = tk.Frame(self.calc)
        self.buttonsFrame.pack()
        self.output = tk.Entry(self.displayFrame,
                               width=29, relief="raised", bd=3, font=("Nunito", 17), fg="#c9c9c5", bg="#8B0000")
        self.output.grid(row = 0, column = 0)
        self.converte = tk.Button(self.displayFrame,
                                  botao_config, width = 5, height = 0, text = 'DEG', bg = '#e35124', command = self.degreesRadians)
        self.converte.grid(row = 0, column = 1)
        self.criarBotoes()

    def criarBotoes(self):
        self.botoes = [
            ["√", "x²", "**", "(",")","/"],
            ["sin", "cos", "7", "8", "9", "+"],
            ["sin-¹", "cos-¹", "4", "5", "6", "-"],
            ["tan", "tan-¹", "1", "2", "3", "*"],
            ["n!", "π", ".", "0", "=", "Limpar"]
            ]
        for linha in range(len(self.botoes)):
            for coluna in range(len(self.botoes[linha])):
               texto = self.botoes[linha][coluna]

               b = tk.Button(self.buttonsFrame, botao_config, text= texto, command = lambda x = texto: self.acaoBotoes(x))
               b.grid(row = linha, column = coluna)


    def acaoBotoes(self, texto):
        global deg
        global inversa_deg
        if texto != "=":
            if texto not in digitos:
                self.output.insert("end", texto)
            else:
                if texto == "√":
                    self.addValor(math.sqrt(float(self.output.get())))
                else:
                    if texto == "√":
                        self.addValor(math.sqrt(float(self.output.get())))
                    elif texto == "n!":
                        self.addValor(math.factorial(float(self.output.get())))
                    elif texto == "x²":
                        self.addValor(float(self.output.get()) ** 2)
                    elif texto == "Limpar":
                        self.addValor("")
                    elif texto == "π":
                        self.addValor(math.pi)
                    elif texto == "sin":
                        self.addValor(math.sin(float(self.output.get()) * deg))
                    elif texto == "cos":
                        self.addValor(math.cos(float(self.output.get()) * deg))
                    elif texto == "tan":
                        self.addValor(math.tan(float(self.output.get()) * deg))
                    elif texto == "sin-¹":
                        self.addValor(math.asin(float(self.output.get())) * inversa_deg)
                    elif texto == "cos-¹":
                        self.addValor(math.acos(float(self.output.get())) * inversa_deg)
                    elif texto == "tan-¹":
                        self.addValor(math.atan(float(self.output.get())) * inversa_deg)
        else:
            self.addValor(eval(self.output.get()))


    def addValor(self, valor):
        self.output.delete(0, 'end')
        self.output.insert("end", valor)


    def degreesRadians(self):
        global deg
        global inversa_deg
        global cnt

        if (cnt == 0):
            deg = math.pi / 180
            inversa_deg = 180 / math.pi
            self.converte['text'] = 'RAD'
            cnt = 1
        else:
            deg = 1
            inversa_deg = 1
            self.converte["text"] = 'DEG'
            cnt = 0


janela = tk.Tk()
Calculadora(janela)
janela.mainloop()