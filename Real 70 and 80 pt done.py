from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')

enemy = drawpad.create_rectangle(50,50,100,60, fill="red")
rocket = drawpad.create_rectangle(395, 585, 405, 595, fill="green")
direction = 5
player = drawpad.create_oval(390,580,410,600, fill="blue")
rocketFired = False 
rockets = 3
class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        # Enter my text
        self.prompt = "Rockets left :"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()

      
        
        self.rocketsTxt = Label(root, text=str(rockets), width=len(str(rockets)), bg='green')
        self.rocketsTxt.pack()
        
        
        # Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    def animate(self):
        global drawpad
        global enemy
        global direction
        global player
        global rocketFired
        px1,py1,px2,py2 = drawpad.coords(player)
        x1,y1,x2,y2 = drawpad.coords(enemy)
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket)
        if x2 > 800:
            direction = - 5
        elif x1 < 0:
            direction = 5
        drawpad.move(enemy, direction, 0)
        if rocketFired == True:
            drawpad.move(rocket,0,-5)
        if ry1 < 0:
            x = (px1-rx1) + 5
            y = (py1-ry1) - 3
            drawpad.move(rocket, x, y)
            rocketFired = False 
        drawpad.after(5,self.animate)

       
    def key(self,event):
        global player
        global rocketFired
        global rockets
        x1,y1,x2,y2 = drawpad.coords(player)
        if event.char == "w":
            if y1 > 0:
                drawpad.move(player,0,-4)
                drawpad.move(rocket,0,-4)
            else:
                return 
        if event.char == "s":
            if y2 < 600:
                drawpad.move(player,0,4)
                drawpad.move(rocket,0,4)
            else:
                return
        if event.char == "a":
            if x1 > 0:
                drawpad.move(player,-4,0)
                drawpad.move(rocket,-4,0)  
            else:
                return
             
        if event.char == "d":
            if x2 < 800:
                drawpad.move(player,4,0) 
                drawpad.move(rocket,4,0)       
            else:
                return 
        if event.char == " ":
             rocketFired = True
             rockets = rockets - 1
             self.rocketsTxt.configure(text = str(rockets))
             
    def collisionDetect(self,rocket):
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket)
        x1, y1, x2, y2 = drawpad.coords(enemy)
        if (rx1 > x1 and rx2 < x2) and (ry1 > y1 and ry2 < y2):
            drawpad.delete(enemy) 
            
                
                        

app = myApp(root)
root.mainloop()