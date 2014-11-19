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
player = drawpad.create_oval(300,0,320,20, fill="purple")
direction = 1
direction2 = 5 

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

					
		# "Bind" an action to the first button												

                self.button5.bind("<Button-1>", self.button5Click)
		self.button2.bind("<Button-1>", self.button2Click)
		
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()

		

               
        
        def button2Click(self, event):  
                global oval
		global drawpad
		x1,y1,x2,y2 = drawpad.coords(player)
		if x2+1 < 480 :
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
            targetx1,targety1,targetx2,targety2 = drawpad.coords(target)
            if targetx2 > 600:
                    direction = -1
            elif targetx1 < 0: 
                    direction = 1
            drawpad.move(target,direction,0)

  
            global enemy2
            global direction
            e2x1, e2y1, e2x2, e2y1 = drawpad.coords(enemy2)
            if e2x2 > 600:
                direction2 = -5
            elif e2x1 < 0: 
                direction2 = 5
            drawpad.move(enemy2,direction2,0)
           
            drawpad.after(1,self.animate)
            

	def collisionDetect(self):
            global target
            global drawpad
            global player
            e2x1, e2y1, e2x2, e2y1 = drawpad.coords(target)

            x1,y1,x2,y2 = drawpad.coords(player)    
            if x1 > e2x1 and x2 < e2x2 :
                if y1 > e2y1 and y2 < e2y1 :
                    return True
            return False
            targetx1,targety1,targetx2,targety2 = drawpad.coords(target)
            x1,y1,x2,y2 = drawpad.coords(player)    
            if x1 > targetx1 and x2 < targetx2 :
                if y1 > targety1 and y2 < targety2 :
                    return True
            return False
                    
                

direction = 1
direction2 = 5 


               
		
		
myapp = MyApp(root)

root.mainloop()