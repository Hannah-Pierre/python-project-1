from Tkinter import *
root = Tk()
# creating the obejects; enemies, player, drawpad
drawpad = Canvas(root, width=600,height=600, background='white')
targetx1 = 200
targety1 = 40
targetx2 = 280
targety2 = 60
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="red")
enemy2 = drawpad.create_rectangle(200, 100, 280, 120, fill="red")
enemy3 = drawpad.create_rectangle(200, 160, 280, 180, fill="red")
enemy4 = drawpad.create_rectangle(200, 220, 280, 240, fill="red")
enemy5 = drawpad.create_rectangle(200, 280, 280, 300, fill="red")
enemy6 = drawpad.create_rectangle(200, 340, 280, 360, fill="red")
enemy7 = drawpad.create_rectangle(200, 400, 280, 420, fill="red")
enemy8 = drawpad.create_rectangle(200, 460, 280, 480, fill="red")
enemy9 = drawpad.create_rectangle(200, 520, 280, 540, fill="red")
startarea = drawpad.create_rectangle(300,0,320,20, fill="white")
player = drawpad.create_oval(300,0,320,20, fill="purple")

direction = -1
direction2 = 2 
direction3 = -3 
gopressed = False

#creating buttons to move left and right 
class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		

		
		self.button5 = Button(self.myContainer1)
		self.button5.configure(text="Left", background= "pink")
		self.button5.grid(row=0,column=1)
		
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Right", background= "pink")
		self.button2.grid(row=0,column=2)
		
		self.gobutton = Button(self.myContainer1)
		self.gobutton.configure(text="press to start", background= "green")
		self.gobutton.grid(row=1,column=0)

					
		# "Bind" an action to the first button												

                self.button5.bind("<Button-1>", self.button5Click)
		self.button2.bind("<Button-1>", self.button2Click)
		self.gobutton.bind("<Button-1>", self.gobuttonclick)
		
		
		
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()

	def gobuttonclick(self,event) :
	       global gopressed
	       gopressed = True
	       
	           
        def button2Click(self, event):  
                global oval
		global drawpad
		x1,y1,x2,y2 = drawpad.coords(player)
		if x2+1 < 600 :
                    drawpad.move(player, 20, 0)
	
	def button5Click(self, event):   
                global oval
		global drawpad
		x1,y1,x2,y2 = drawpad.coords(player)
		if x1-1 > 0 :
		    drawpad.move(player, -20, 0)

	def animate(self):
            global target
            global direction
            global gopressed
            targetx1,targety1,targetx2,targety2 = drawpad.coords(target)
            if targetx2 > 600:
                    direction = -1
            elif targetx1 < 0: 
                    direction = 1
            drawpad.move(target,direction,0)

  
            global enemy2
            global direction2
            e2x1, e2y1, e2x2, e2y2 = drawpad.coords(enemy2)
            if e2x2 > 600:
                direction2 = -2
            elif e2x1 < 0: 
                direction2 = 2
            drawpad.move(enemy2,direction2,0)
            
            global enemy3
            global direction3
            e3x1, e3y1, e3x2, e3y2 = drawpad.coords(enemy3)
            if e3x2 > 600:
                direction3 = -3
            elif e3x1 < 0: 
                direction3 = 3
            drawpad.move(enemy3,direction3,0)
            
            global player 
            x1,y1,x2,y2 = drawpad.coords(player)
            if gopressed == True :
                drawpad.move(player, 0, 1)
            if y2 > 600 :
                drawpad.delete(player)
            sx1, sy1, sx2, sy2 = drawpad.coords(startarea)
            if y2 > targety1 and y2 < targety2 and x1 > targetx1 and x2 < targetx2 :
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if y2 > e2y1 and y2 < e2y2 and x1 > e2x1 and x2 < e2x2 :
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if y2 > e3y1 and y2 < e3y2 and x1 > e3x1 and x2 < e3x2 :
                drawpad.move(player, sx1 - x1, sy2 - y2)
            
            
            
            drawpad.after(1,self.animate)
            

	def collisionDetect(self):
            global target
            global enemy2
            global drawpad
            global player
            x1,y1,x2,y2 = drawpad.coords(player)
            targetx1,targety1,targetx2,targety2 = drawpad.coords(target)
            e2x1, e2y1, e2x2, e2y2 = drawpad.coords(enemy2)
            if y2 > targety1 and y2 < targety2 :
                drawpad.delete(player)
            

                    
                

direction = 1
direction2 = 2


               
		
		
myapp = MyApp(root)

root.mainloop()