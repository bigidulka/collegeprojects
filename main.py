import customtkinter as CTtk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Style
from math import *

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as pts
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class App(CTtk.CTk):
    def __init__(self):
        matplotlib.use("TkAgg")
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.title("График функции")
        self.geometry("250x150")
        self.resizable(width=False, height=False)
        CTtk.set_appearance_mode("dark")
        
        self.columnconfigure(0)
        CTtk.CTkLabel(text="Введите пределы интегрирования").grid(row=0,column=1, sticky=W)
        CTtk.CTkLabel(text="до", width=0).grid(row=1,column=0, sticky=W)   
        CTtk.CTkLabel(text="и от", width=0).grid(row=2,column=0, sticky=W)        
        CTtk.CTkLabel(text="шаг", width=0).grid(row=3,column=0, sticky=W)

        self.graphInA = CTtk.CTkEntry(width=100)
        self.graphInA.grid(row=1, column=1, padx=25)
        
        self.graphInB = CTtk.CTkEntry(width=100)
        self.graphInB.grid(row=2, column=1, padx=25)

        self.graphInSG = CTtk.CTkEntry(width=100)
        self.graphInSG.grid(row=3, column=1, padx=25)

        self.bind('<Return>', lambda event: self.calBut())
        but = CTtk.CTkButton(text="Рассчитать", fg_color="black", width=200, command=self.calBut)
        but.grid(row=4, column=1, pady=5)

        self.graphOutIntg =  CTtk.CTkLabel(width=0)
        self.graphOutLeftRectIntg =  CTtk.CTkLabel(width=0)
        self.graphOutShag =  CTtk.CTkLabel(width=0)
        self.graphOutPG = CTtk.CTkLabel(width=0)
    
    
    def update(self):
        INTG = self.intg(float(self.graphInA.get()),float(self.graphInB.get()))
        LRINTG, SH = self.utoch(float(self.graphInA.get()),float(self.graphInB.get()))
        self.graphOutIntg.configure(text="Точный интеграл: " + str(round(INTG, 3)))
        self.graphOutLeftRectIntg.configure(text="Методом левых прямоугольников: " + str(round(LRINTG,3)))
        self.graphOutShag.configure(text="Шаг: " + str(SH))
        #self.graphOutShag.configure(text="Шаг: " + str(self.graphInSG.get()))
        self.graphOutPG.configure(text="Погрешность: " + str(round(self.pogr(INTG, LRINTG), 2)))
        
        self.graphOutIntg.place(x=0,y=150)
        self.graphOutLeftRectIntg.place(x=0,y=175)
        self.graphOutShag.place(x=0,y=200)
        self.graphOutPG.place(x=0,y=225)
        
        self.geometry("940x500")
        self.graph()
        
    def graph(self):
        fig, ax = plt.subplots()
        plt.axis([-100, 100, -100, 100])
        plt.title('$f(x)= x^3 + x^2 + 17 $')
        plt.minorticks_on()
        plt.grid()
        plt.xlabel('x')
        plt.ylabel('y')

        x = np.arange(-100, 100, 0.01)
        y = lambda x: x ** 3 + x ** 2 + 17

        ax.fill_between(x,y(x),color="green", alpha= 0.3, label='Область определения',
                          where=(x>=float(self.graphInB.get())) & (x<=float(self.graphInA.get())))

        ax.plot(x, y(x), label='f(x)', color='blue')

        for xf in range(int(self.graphInB.get()), int(self.graphInA.get()), int(self.graphInSG.get())):
            ax.add_patch(
                pts.Rectangle(
                    (xf, 0),
                    int(self.graphInSG.get()),
                    y(xf) if (xf != -3) else 5,
                    edgecolor='black',
                    fill=False,
                ))

        plt.legend(loc='lower right')
            
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().place(x=350, y=0)
        
        toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
        toolbar.update()
        toolbar.place(x=350, y=0)
        
    def calBut(self):
        if len(self.graphInA.get()) > 0 and len(self.graphInB.get()) > 0 and len(self.graphInSG.get()) > 0:
            try:
                float(self.graphInA.get())
                float(self.graphInB.get())
                int(self.graphInSG.get())
            except ValueError:
                messagebox.showinfo("Ошибка", "Одно или два значения не или шаг не целый")
            else: self.update()
        else: 
            messagebox.showinfo("Ошибка", "Введите значение")
            
    def utoch(self, a,b):
        eps = 0.001
        diff = 0
        k = 10
        i = 0
        i += 1
        def Diff():
            return fabs(self.leftRectIntg(b,a, k * i) - self.leftRectIntg(b,a, k * (i + 1)))
        diff = Diff()
        while diff > eps:
            i += 1
            diff = Diff()
        return self.leftRectIntg(b,a, k * (i + 1)), k * (i + 1)
        
    def intg(self, a,b):
        A = (a ** 4 /4) + (a ** 3/3) + 17 * a
        B = (b ** 4 /4) + (b ** 3/3) + 17 * b
        return A - B

    def func(self, x):
        return x**3 + x**2 + 17

    def leftRectIntg(self, a,b,n):
        h = (b - a) / n 
        sum = 0.0
        for i in range(0, n-1): 
            x = a + i * h 
            sum += h * self.func(x) 
        return sum

    def pogr(self, a, b):
        if b > a:
            return (b/a-1)*100
        elif a > b:
            return (a / b - 1) * 100
        
app = App()
app.mainloop()