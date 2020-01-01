import tkinter as tk
import random
import time
import math

e = 100
tagstack = []


def addexp(c):
    for x in range(0, 5000):
        x = x/10
        y = math.exp(x/e - 250/e)
        pad.create_line(x,250-y * e, x+1, 250-y*e+1, fill=c, width=1, tags="exp")
        if "exp" not in tagstack:
            tagstack.append("exp")

def addlog(c):
    for x in range(2501, 5000):
        x = x/10
        y = math.log(x/e - 250/e)
        pad.create_line(x,250-y * e, x+1, 250-y*e+1, fill=c, width=1, tags="log")
        if "log" not in tagstack:
            tagstack.append("log")
        
def poly(c):
    for x in range(0, 5000):
        x = x/10
        y = (x/e - 250/e) * (x/e - 250/e)
        pad.create_line(x,250 - y * e, x+1, 250 - y * e + 1, fill=c, width=1, tags="car")
        if "car" not in tagstack:
            tagstack.append("car")

def racine(c):
    for x in range(2500, 5000):
        x = x/10
        y = math.sqrt(x/e - 250/e)
        pad.create_line(x,250-y * e, x+1, 250-y*e+1, fill=c, width=1, tags="rac")
        if "rac" not in tagstack:
            tagstack.append("rac")

def cube(c):
    for x in range(0, 5000):
        x = x/10
        y = (x/e - 250/e) ** 3
        pad.create_line(x,250 - y * e, x+1, 250 - y * e + 1, fill=c, width=1, tags="cube")
        if "cube" not in tagstack:
            tagstack.append("cube")

def inverse(c):
    for x in range(0, 5000):
        x = x/10
        try:
            y = 1/(x/e - 250/e)
            pad.create_line(x,250 - y * e, x+1, 250 - y * e + 1, fill=c, width=1, tags="inv")
            if "inv" not in tagstack:
                tagstack.append("inv")
        except:
            pass

def init():
    pad.delete("all")
    pad.create_line(250, 0, 250, 500)
    pad.create_line(0,250, 500, 250)

def erase():
    if tagstack != []:
        pad.delete(tagstack[-1])
        del tagstack[-1]

    
root = tk.Tk(className = "Courbes de fonctions connues !")

pad = tk.Canvas(root, bg = "white", height = 500, width = 500)
pad.pack(side = "left")
init()


tk.Button(text = "Quitter", command=root.quit, width = 15).pack(side = "bottom")
tk.Button(text = "Exponentielle exp(x)", command=lambda : addexp("red"), width = 15).pack()
tk.Button(text = "Logarithme log(x)", command=lambda : addlog("green"), width = 15).pack()
tk.Button(text = "Carré x²", command=lambda : poly("grey"), width = 15).pack()
tk.Button(text = "racine", command=lambda : racine("purple"), width = 15).pack()
tk.Button(text = "cube x*x*x", command=lambda : cube("blue"), width = 15).pack()
tk.Button(text = "inverse 1/x", command=lambda : inverse("#789900"), width = 15).pack()
tk.Button(text = "Effacer", command=lambda : erase(), width = 15, pady = 10).pack()

root.mainloop()
try:
    root.destroy()
except:
    pass


