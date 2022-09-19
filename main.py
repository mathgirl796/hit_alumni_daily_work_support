import tkinter as tk
import tkinter.messagebox
import webbrowser

def load():
    ret = []
    with open("links.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            words = line.strip().split()
            if len(words) == 2 and words[1].startswith("http"):
                ret.append(words)
    return ret

class UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.data = load()
        print(self.data)
        self.text = tk.StringVar()
        self.text.set("点击next开始工作")
        self.lb = tk.Label(self, textvariable=self.text)
        self.bt = tk.Button(self, text="next", command=self.on_click)
        self.i = 0
        
        self.lb.pack()
        self.bt.pack()
        self.attributes('-topmost', True)
        self.title("常规任务")
        self.mainloop()

    def on_click(self):
        self.text.set("正在浏览："+self.data[self.i][0]+" "+str(self.i+1)+"/"+str(len(self.data)))
        webbrowser.open(self.data[self.i][1])
        self.i += 1

UI()