import tkinter as tk
from tkinter import messagebox


class MapEditor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("打篮球地图编辑器")
        self.geometry("640x480")  # 32 * 20 格子，每个格子 20x20 像素

        self.grid = [[1 for _ in range(32)]] + [[1] + [0 for _ in range(30)] + [1]for _ in range(19)]

        self.canvas = tk.Canvas(self, width=640, height=400)
        self.canvas.pack()

        self.draw_grid()
        self.canvas.bind("<Button-1>", self.handle_left_click)
        self.canvas.bind("<Button-3>", self.handle_right_click)

        self.entry_line = tk.Entry(self)
        self.entry_line.pack()

        self.save_button = tk.Button(self, text="Save", command=self.save_grid)
        self.save_button.pack()

        self.load_button = tk.Button(self, text="Load", command=self.load_grid)
        self.load_button.pack()

        self.label_line = tk.Label(self, text="白色代表空，灰色代表屏障，蓝色代表可消除方块")

    def draw_grid(self):
        for y in range(20):
            for x in range(32):
                color = self.get_color(self.grid[y][x])
                self.canvas.create_rectangle(x*20, y*20, x*20+20, y*20+20, fill=color, outline="black")

    def handle_left_click(self, event):
        x, y = event.x // 20, event.y // 20
        self.grid[y][x] = (self.grid[y][x] + 1) % 3
        color = self.get_color(self.grid[y][x])
        self.canvas.create_rectangle(x*20, y*20, x*20+20, y*20+20, fill=color, outline="black")

    def handle_right_click(self, event):
        x, y = event.x // 20, event.y // 20
        self.grid[y][x] = self.grid[y][x] - 1
        if self.grid[y][x] < 0:
            self.grid[y][x] = self.grid[y][x] + 3
        color = self.get_color(self.grid[y][x])
        self.canvas.create_rectangle(x*20, y*20, x*20+20, y*20+20, fill=color, outline="black")

    def get_color(self, state):
        if state == 0:
            return "white"
        elif state == 1:
            return "gray"
        elif state == 2:
            return "blue"

    def save_grid(self):
        text = self.entry_line.get()
        ls = [1] + [0 for _ in range(30)] + [1]
        for i in range(4):
            self.grid.append(ls)
        with open(f"{text}.txt", "w") as file:
            for row in self.grid:
                file.write(" ".join(map(str, row)) + "\n")
        messagebox.showinfo("Info", "Map saved successfully!")
        self.quit()

    def load_grid(self):
        text = self.entry_line.get()
        self.entry_line.delete(0, "end")
        try:
            with open(f"{text}.txt", "r") as file:
                lines = file.readlines()
                ls = []
                for line in lines:
                    ls.append(list(map(eval, line.split())))
                self.grid = ls
                self.draw_grid()
                messagebox.showinfo("提示", "读取完毕")
        except FileNotFoundError:
            messagebox.showinfo("提示", "文件不存在")
        except Exception as e:
            messagebox.showinfo("提示", f"出现如下错误{e}")


app = MapEditor()
app.mainloop()
