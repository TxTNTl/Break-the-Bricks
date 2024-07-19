import tkinter as tk
import pygame
from tkinter import messagebox
from Game import Game


class MapLoader(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x300")

        self.lab = tk.Label(self, text="请输入关卡名称")
        self.lab.pack()

        self.ent = tk.Entry(self)
        self.ent.insert(0, "3")
        self.ent.pack()

        self.button = tk.Button(self, text="打开", command=self.openMap)
        self.button.pack()

    def openMap(self):
        try:
            location = self.ent.get()
            with open(f"{location}.txt", "r") as file:
                lines = file.readlines()
                ls = []
                for line in lines:
                    ls.append(list(map(eval, line.split())))
                self.destroy()
                game = Game(ls)
                game.run()
        except FileNotFoundError:
            print("当前文件不存在")
        except Exception as e:
            print(e)

def main():
    mapLoader = MapLoader()
    mapLoader.mainloop()

if __name__ == "__main__":
    main()