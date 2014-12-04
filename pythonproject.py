from Tkinter import *
root = Tk()
# creating the obejects; enemies, player, drawpad
drawpad = Canvas(root, width=600,height=600, background='white')
targetx1 = 200
targety1 = 40
targetx2 = 280
targety2 = 60
#enemies 
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
#start area pattern
drawpad.create_rectangle(300,0,305,5, fill ="black")
drawpad.create_rectangle(310,0,315,5, fill ="black")
drawpad.create_rectangle(305,5,310,10, fill ="black")
drawpad.create_rectangle(315,5,320,10, fill ="black")
drawpad.create_rectangle(300,10,305,15, fill ="black")
drawpad.create_rectangle(310,10,315,15, fill ="black")
drawpad.create_rectangle(305,15,310,20, fill ="black")
drawpad.create_rectangle(315,15,320,20, fill ="black")



player = drawpad.create_oval(300,0,320,20, fill="magenta")
#directions for enemies 
direction = -1
direction2 = 2 
direction3 = -3
direction4 = 4
direction5 = -5
direction6 = 6
direction7 = -7
direction8 = 8
direction9 = -9
#go button control
gopressed = False

#creating buttons to move left and right 
class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		

		#making the buttons
		self.button5 = Button(self.myContainer1)
		self.button5.configure(text="Left", background= "pink")
		self.button5.grid(row=2,column=0)
		
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Right", background= "pink")
		self.button2.grid(row=2,column=3)
		
		self.gobutton = Button(self.myContainer1)
		self.gobutton.configure(text="press to start", background= "green")
		self.gobutton.grid(row=1,column=2)

					
		# binding the buttons												

                self.button5.bind("<Button-1>", self.button5Click)
		self.button2.bind("<Button-1>", self.button2Click)
		self.gobutton.bind("<Button-1>", self.gobuttonclick)
		
		
		
		  
		#creates the drawpad 
		drawpad.pack()
		self.animate()
	#go button 

	def gobuttonclick(self,event) :
	       global gopressed
	       gopressed = True
	       
	# left and right controls           
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
	    #enemies animation
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
           
            global enemy4
            global direction4
            e4x1, e4y1, e4x2, e4y2 = drawpad.coords(enemy4)
            if e4x2 > 600:
                direction4 = -4
            elif e4x1 < 0: 
                direction4 = 4
            drawpad.move(enemy4,direction4,0)
            
            global enemy5
            global direction5
            e5x1, e5y1, e5x2, e5y2 = drawpad.coords(enemy5)
            if e5x2 > 600:
                direction5 = -5
            elif e5x1 < 0: 
                direction5 = 5
            drawpad.move(enemy5,direction5,0)
            
            global enemy6
            global direction6
            e6x1, e6y1, e6x2, e6y2 = drawpad.coords(enemy6)
            if e6x2 > 600:
                direction6 = -6
            elif e6x1 < 0: 
                direction6 = 6
            drawpad.move(enemy6,direction6,0)
            
            global enemy7
            global direction7
            e7x1, e7y1, e7x2, e7y2 = drawpad.coords(enemy7)
            if e7x2 > 600:
                direction7 = -7
            elif e7x1 < 0: 
                direction7 = 7
            drawpad.move(enemy7,direction7,0)
            
            global enemy8
            global direction8
            e8x1, e8y1, e8x2, e8y2 = drawpad.coords(enemy8)
            if e8x2 > 600:
                direction8 = -8
            elif e8x1 < 0: 
                direction8 = 8
            drawpad.move(enemy8,direction8,0)
            
            global enemy9
            global direction9
            e9x1, e9y1, e9x2, e9y2 = drawpad.coords(enemy9)
            if e9x2 > 600:
                direction9 = -9
            elif e9x1 < 0: 
                direction9 = 9
            drawpad.move(enemy9,direction9,0)
            
            #player animation
            global player 
            x1,y1,x2,y2 = drawpad.coords(player)
            if gopressed == True :
                drawpad.move(player, 0, 1)
            if y2 > 600 :
                drawpad.delete(player)
            sx1, sy1, sx2, sy2 = drawpad.coords(startarea)
            
            # enemy1 collision detect
            if y2 > targety1 and y2 < targety2 and x1 > targetx1 and x2 < targetx2 :
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x1 < targetx2 and x1 > targetx1 and y2 > targety1 and y2 < targety2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x2 > targetx1 and x2 < targetx2 and y2 > targety1 and  y2 < targety2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            #enemy2  collision detect  
            if y2 > e2y1 and y2 < e2y2 and x1 > e2x1 and x2 < e2x2 :
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x1 < e2x2 and x1 > e2x1 and y2 > e2y1 and y2 < e2y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x2 > e2x1 and x2 < e2x2 and y2 > e2y1 and y2 < e2y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            #enemy3  collision detect  
            if y2 > e3y1 and y2 < e3y2 and x1 > e3x1 and x2 < e3x2 :
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x1 < e3x2 and x1 > e3x1 and y2 > e3y1 and y2 < e3y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x2 > e3x1 and x2 < e3x2 and y2 > e3y1 and y2 < e3y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            #enemy4 collision detect
            if y2 > e4y1 and y2 < e4y2 and x1 > e4x1 and x2 < e4x2 :
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x1 < e4x2 and x1 > e4x1 and y2 > e4y1 and y2 < e4y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x2 > e4x1 and x2 < e4x2 and y2 > e4y1 and y2 < e4y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            #enemy5   collision detect 
            if y2 > e5y1 and y2 < e5y2 and x1 > e5x1 and x2 < e5x2 :
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x1 < e5x2 and x1 > e5x1 and y2 > e5y1 and y2 < e5y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x2 > e5x1 and x2 < e5x2 and y2 > e5y1 and y2 < e5y2:
                drawpad.move(player, sx1 - x1, sy2 - y2) 
            #enemy6 collision detect
            if y2 > e6y1 and y2 < e6y2 and x1 > e6x1 and x2 < e6x2 :
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x1 < e6x2 and x1 > e6x1 and y2 > e6y1 and y2 < e6y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x2 > e6x1 and x2 < e6x2 and y2 > e6y1 and y2 < e6y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            #enemy7 collision detect
            if y2 > e7y1 and y2 < e7y2 and x1 > e7x1 and x2 < e7x2 :
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x1 < e7x2 and x1 > e7x1 and y2 > e7y1 and y2 < e7y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x2 > e7x1 and x2 < e7x2 and y2 > e7y1 and y2 < e7y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            #enemy8 collision detect
            if y2 > e8y1 and y2 < e8y2 and x1 > e8x1 and x2 < e8x2 :
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x1 < e8x2 and x1 > e8x1 and y2 > e8y1 and y2 < e8y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x2 > e8x1 and x2 < e8x2 and y2 > e8y1 and y2 < e8y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            #enemy9 collision detect
            if y2 > e9y1 and y2 < e9y2 and x1 > e9x1 and x2 < e9x2 :
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x1 < e9x2 and x1 > e9x1 and y2 > e9y1 and y2 < e9y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)
            if x2 > e9x1 and x2 < e9x2 and y2 > e9y1 and y2 < e9y2:
                drawpad.move(player, sx1 - x1, sy2 - y2)

            
            
            
            drawpad.after(5,self.animate)
            


            

                    
                



               
		
		
myapp = MyApp(root)

root.mainloop()