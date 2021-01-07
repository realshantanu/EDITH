import random,tkinter
def shift(c): return list([i for i in c if i>0] + [0]*c.count(0))
def sms(l):
        l=shift(l)
        for i in range(len(l)-1):
                if l[i+1]==l[i]: l[i], l[i+1] = 2*l[i], 0
        return shift(l)
class igra(tkinter.Tk):
        b = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        def __init__(self,parent):
                tkinter.Tk.__init__(self,parent)
                self.parent = parent
                self.grid()
                self.bl = [tkinter.Button(self, height=2, width=4, state=tkinter.DISABLED, font=("Helvetica", 24)) for i in range(16)]
                for i in range(16): self.bl[i].grid(row=i//4, column=i%4)
                self.dodaj_novu()
                self.bind_all('<Key>', self.key)
                self.mainloop()
        def rot(self): self.b = list(map(list, zip(*self.b[::-1])))
        def move(self, n):
                diff = self.b[:]
                for i in range(n): self.rot()
                for i in range(4): self.b[i] = sms(self.b[i])
                for i in range(4-n): self.rot()
                return 1 if self.b != diff else 0
        def dodaj_novu(self):
                k = [(i//4, i%4) for i,j in enumerate(sum(self.b, [])) if j == 0][random.randint(0, sum(self.b, []).count(0)-1)]
                self.b[k[0]][k[1]] = random.randint(1,2)*2
                for i in range(16):
                        d = self.b[i//4][i%4]
                        self.bl[i].config(text=d if d else ' ', bg='#%06x'% ((2**24-1) - (d*1500) ))
        def key(self, event):
                direction={'Left': 0, 'Down': 1, 'Right': 2, 'Up': 3}
                if self.move(direction[event.keysym]): self.dodaj_novu()
                p = self.b[:]
                for i in range(4):
                        self.move(i)
                        if self.b != p:
                                self.b = p[:]
                                return
                for i in range(16): self.bl[i].config(bg='red', text=':(')
a = igra(None)