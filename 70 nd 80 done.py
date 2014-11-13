# Lab 16
# 70pt -  Add in movement buttons for up, down, left and right using WASD
# 80pt -  Make sure the player can't go out of bounds to the left, right or down.
# 90pt -  When you hit space, fire a missile straight up! 
#         Subtract from how many missiles you have left
# 100pt - Destroy the target if a missile hits it! 
# Hints: use drawpad.destroy(enemy) in the collision detect function, which you can trigger
# from the key press event... maybe a loop to keep checking until the rocket goes out of bounds?
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')

enemy = drawpad.create_rectangle(50,50,100,60, fill="red")
missle = drawpad.create_rectangle(395, 585, 405, 595, fill="green")
direction = 5
player = drawpad.create_oval(390,580,410,600, fill="blue")
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

        self.rockets = 3
        
        self.rocketsTxt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='green')
        self.rocketsTxt.pack()
        
        
        # Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    def animate(self):
        global drawpad
        global enemy
        global direction
        x1,y1,x2,y2 = drawpad.coords(enemy)
        if x2 > 800:
            direction = - 5
        elif x1 < 0:
            direction = 5
        drawpad.move(enemy, direction, 0)
        drawpad.after(5,self.animate)

    def key(self,event):
        global player
        x1,y1,x2,y2 = drawpad.coords(player)
        if event.char == "w":
            if y1 > 0:
                drawpad.move(player,0,-4)
                drawpad.move(missle,0,-4)
            else:
                return 
        if event.char == "s":
            if y2 < 600:
                drawpad.move(player,0,4)
                drawpade.move(missle,0,4)
            else:
                return
        if event.char == "a":
            if x1 > 0:
                drawpad.move(player,-4,0)
                drawpad.move(missle,-4,0)  
            else:
                return
             
        if event.char == "d":
            if x2 < 800:
                drawpad.move(player,4,0) 
                drawpad.move(missle,4,0)       
            else:
                return 
    def collisionDetect(self,rocket):
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket)
        

app = myApp(root)
root.mainloop()