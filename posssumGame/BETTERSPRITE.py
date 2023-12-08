#import os
#os.chdir("posssumGame")
import pygame
from pygame.math import Vector2
from pygame.rect import Rect

pygame.init() 
pygame.mixer.init()

screen = pygame.display.set_mode((1600, 900))  # creates game screen



class Possum:

	def __init__(self):
		self.size = 0.46
		self.damage = 100
		self.health = 100

		self.possum1 = pygame.image.load('resources/possum9.png')
		self.possum = pygame.transform.smoothscale_by(self.possum1,self.size)
		 #load your spritesheet
		#self.chirp = pygame.mixer.Sound("resources/chrip.mp3")
		self.frameWidth = 249*self.size
		self.frameHeight = 100*self.size



		#Pos and Vel
		self.pos = Vector2(800,450)
		self.isOnGround = False
		self.isOnWall = False
		self.isBonked = False
		self.vel = Vector2(0,0)
		self.maxvel = 25
		self.offset = Vector2(800,-1350)

		#action
		self.pressed = [False, False, False, False, False, False]
		self.whatdoing = "stand"
		self.direction = 1
		self.charge = 0
		self.maxleap = 480
		self.fastfall = 0

		self.walkspeed = 3 * self.size*1.5 
		self.sprintspeed = 12 * self.size*1.5

		#collison
		self.groundType = "normal"
		self.groundPos = Rect(0,0,0,0)
		self.wallPos = Rect(0,0,0,0)
		self.platList = []
		self.wallList = []
		self.wallJumps = 0

		#anim
		self.hurtTick = 0
		self.hurtTimer = 0
		self.landTick = 0
		self.ticker = 0
		
		self.hitbox = Rect(self.pos.x+5, self.pos.y+15, self.frameWidth-5, self.frameHeight-15)
		# left top width height

		#dumb stuff
		self.frameNum = 0
		self.RowNum = 1
		self.walkFrame = [2,1,0,1]
		self.sprintFrame = [2,3,3]
		self.crawlFrame = [0,1]

		self.standFrame = [1,1,1,1,1,1,1,3]
		self.standRow = [self.RowNum,self.RowNum,self.RowNum,self.RowNum+3,self.RowNum,self.RowNum,self.RowNum,self.RowNum+3]



	def getKeyPressed(self):
		keys = pygame.key.get_pressed() #gets pressed keys
	#------------------------------------------------------------------------------------------------ CROUCH AND SUCH
		if keys[pygame.K_DOWN] or keys[pygame.K_s]:
			self.pressed[3] = True 

			if self.isOnGround:
				if keys[pygame.K_a] == False and keys[pygame.K_d] == False: #if not pressing movement keys basically
					self.whatdoing = "squat"

				self.charge += self.maxleap/190 #charges up super jump or "leap"

				if self.charge >= self.maxleap: # if the charge is greater than the max
					self.charge = self.maxleap #sets charge to max

				self.fastfall = 0 # if on ground, sets fastfall to zero to prevent clipping

			if not self.isOnGround: 
				if self.vel.y > 0:
					self.fastfall += 0.1 #allows players to fall faster while holding down mid air
		else:
			self.pressed[3]=False
			self.fastfall = 0 #fast fall is zero if not holding down
			if self.isOnGround:
				if self.charge > 0:
					self.charge -= self.maxleap/160 #decreases charge when not holding, allows for some holding
				if self.charge <= 1:
					self.charge = 1 #sets charge to base value if below minimum
	#------------------------------------------------------------------------------------------------ LEFT
		if keys[pygame.K_a]:
			self.pressed[0]=True
			if keys[pygame.K_DOWN] == False and keys[pygame.K_s] == False and self.isOnGround == True:
				self.whatdoing = "walk"
			if not self.isOnWall:

				if keys[pygame.K_DOWN] or keys[pygame.K_s]:
					if self.isOnGround:
						if abs(self.vel.x) > 3.5 * self.size*1.5:
							self.vel.x *= 0.99
							self.whatdoing = "slide"
						else:
							self.vel.x = -(3.5 * self.size*1.5)
							self.whatdoing = "crawl"
				elif keys[pygame.K_LSHIFT]:
					if self.whatdoing != "jump" and self.whatdoing != "leap" and self.vel.x < -self.walkspeed*1.5:
						self.whatdoing = "sprint"
					if self.vel.x > -self.sprintspeed:
						self.vel.x-=0.6
					else:
						self.vel.x -= 0.01
				else:
					if self.vel.x > -self.walkspeed:
						self.vel.x -= 0.8
					else:
						self.vel.x -= 0.01
			if self.vel.x < 0:
				self.direction = 1
		else:
			self.pressed[0]=False
	#------------------------------------------------------------------------------------------------ RIGHT
		if keys[pygame.K_d]:
			self.pressed[1]=True
			if keys[pygame.K_DOWN] == False and keys[pygame.K_s] == False and self.isOnGround == True:
				self.whatdoing = "walk"
				
			if not self.isOnWall:
				if keys[pygame.K_DOWN] or keys[pygame.K_s]:
					if self.isOnGround:
						if abs(self.vel.x) > 3.5 * self.size*1.5:
							self.vel.x *= 0.99
							self.whatdoing = "slide"
						else:
							self.vel.x = 3.5 * self.size*1.5
							self.whatdoing = "crawl"
				elif keys[pygame.K_LSHIFT]:
					if self.whatdoing != "jump" and self.whatdoing != "leap" and self.vel.x > self.walkspeed*1.5:
						self.whatdoing = "sprint"
					if self.vel.x < self.sprintspeed:
						self.vel.x+=0.6
					else:
						self.vel.x += 0.01
				else:
					if self.vel.x < self.walkspeed:
						self.vel.x += 0.8
					else:
						self.vel.x += 0.01
			if self.vel.x > 0:
				self.direction = 0

		else:
			self.pressed[1]=False
	#------------------------------------------------------------------------------------------------ 
		if keys[pygame.K_a] == False and keys[pygame.K_d] == False:
			if not self.isOnGround:
				if abs(self.vel.x) != 0:
					self.vel.x*=0.98
				if abs(self.vel.x)<=0.2:
					self.vel.x = 0
	#------------------------------------------------------------------------------------------------ JUMP
		if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:# or keys[pygame.K_x]:
			self.pressed[2]=True
			if self.whatdoing != "leap" and self.whatdoing!= "hurt":
				self.whatdoing = "jump"
			if self.isOnGround == True:
				self.hitbox.bottom+=1
		else:
			self.pressed[2]=False
	#------------------------------------------------------------------------------------------------ SPRINT
		if keys[pygame.K_LSHIFT]:
			self.pressed[4] = True
		else:
			self.pressed[4] = False


	def getPlatty(self,num:int):
		for i in range(num):
			self.platList.append(0)
			self.wallList.append(False)

	def getSpawn(self,x,y):
		self.offset.update(x+800-self.frameWidth*2,y-1350+self.frameHeight*2)
	

	def collision(self, objPos:Rect, groundType:str,num:int):

		if self.hitbox.colliderect(objPos) == True:
			self.groundPos = objPos
			self.groundType = groundType

			if self.hitbox.top-7 <= self.groundPos.bottom+self.vel.y and self.hitbox.bottom-7 > self.groundPos.bottom:
				self.platList[num] = 2

			elif self.hitbox.bottom+7 >= self.groundPos.top-self.vel.y and self.hitbox.top-14 <= self.groundPos.top:
				if self.hitbox.centerx+self.hitbox.width*0.3> self.groundPos.left and self.hitbox.centerx-self.hitbox.width*0.3 < self.groundPos.right:
					self.platList[num] = 1

			if self.hitbox.right+7 >= objPos.left-self.vel.x and self.hitbox.centery >= objPos.top and self.hitbox.centery-10 <= objPos.bottom:
				self.wallPos.update(objPos)
				self.wallList[num] = True

			if self.hitbox.left-7 <= objPos.right+self.vel.x and self.hitbox.centery >= objPos.top and self.hitbox.centery-10 <= objPos.bottom:
				self.wallPos.update(objPos)
				self.wallList[num] = True 
		
		else:
			self.platList[num] = 0
			self.wallList[num] = False
	def gouds(self):

		if self.groundType == "normal":
			pass

		if self.groundType == "spike":
			self.vel.y -= 10
			self.whatdoing = "hurt"
			if self.hurtTick >= 45 or self.hurtTick == 0:
				self.health -= 10
				self.hurtTick = 1
		#	pass
		if self.groundType == "trampoline":
			#if self.vel.y >= 0:
			#	if self.pressed[2]:
			#		self.vel.y = -abs(self.vel.y)*1.2
			#	else:
			#		self.vel.y = -self.vel.y*0.8
			self.vel.y= -28
			self.vel.x *= 0.3
		
		if self.groundType == "sideT":
			if self.direction == 0:
				self.vel.x = +8
				self.vel.y = -13
				self.direction = 1
				#self.wallJumps -= 1
			elif self.direction == 1:
				self.vel.x = -8
				self.vel.y = -13
				self.direction = 0
				#self.wallJumps += 1


		if self.groundType == "Ice":
			self.vel.x *= 1.06

		if self.groundType == "Water":
			if self.vel.y<0:
					self.vel.y += 0.1
			self.isOnGround = False
			self.isBonked = False
			self.isOnWall = False

		#if self.groundType == "Goal":
			# pass

		#if self.groundType == "breakblock":
		#	pass

	
	def update(self,type):
		groundNum = 0
		wallNum = 0
		bonknum = 0
		if self.vel.x == 0:
			self.vel.x = 0.001
		if type == 0:
			if self.hurtTick >= 1:
				self.hurtTick += 1

			if self.hurtTick > 120:
				self.hurtTick = 0

			if self.hurtTick == 0 and self.health < 100:
				self.health += 0.334

			for i in range(len(self.platList)):
				if self.platList[i] == 1:
					groundNum += 1
				if self.platList[i] == 2:
					bonknum += 1

				if groundNum > 0:
					self.isOnGround = True
				else:
					self.isOnGround = False
				if bonknum > 0:
					self.isBonked = True
				else:
					self.isBonked = False

			for i in range(len(self.wallList)):
				if self.wallList[i] == True:
					wallNum += 1
				if wallNum > 0:
					self.isOnWall = True
				else:
					self.isOnWall = False
					
			if self.isBonked:
				if self.hitbox.top<self.groundPos.bottom and self.vel.y < 0 and self.isOnWall!=True:
					self.vel.y = 0
					self.offset.y -= self.groundPos.bottom - self.hitbox.top

			if self.isOnWall:

				if self.hitbox.right>self.wallPos.left and self.vel.x>0:
					if not self.isOnGround:
						self.offset.x += int(self.hitbox.right - self.wallPos.left)

					self.vel.x -= 3

					if self.pressed[2] and self.pressed[1] and self.wallJumps < 3:
						self.vel.x = -8
						self.vel.y = -13
						self.direction = 1
						self.wallJumps += 1


				elif self.hitbox.left<self.wallPos.right and self.vel.x<0:
					if not self.isOnGround:
						self.offset.x -= int(self.wallPos.right - self.hitbox.left)

					self.vel.x += 3

					if self.pressed[2] and self.pressed[0] and self.wallJumps < 3:
						self.vel.x = 8
						self.vel.y = -13
						self.direction = 0
						self.wallJumps += 1
				

			if self.isOnGround:

				if self.hitbox.bottom>self.groundPos.top and self.isOnWall != True:
					self.offset.y += self.hitbox.bottom - self.groundPos.top - 1

				if self.vel.y >= 14:
					self.whatdoing = "land"

				elif self.whatdoing != "land" and self.whatdoing != "hurt":
					nothingDoing = 0
					for i in range(len(self.pressed)):
						nothingDoing += 1
					if nothingDoing == len(self.pressed):
						self.whatdoing = "stand"

				if self.groundType != "spike" and self.groundType != "trampoline":
					self.vel.y = 0
				self.fastfall = 0
				self.wallJumps = 0
				

			else:

				if self.whatdoing != "leap" and self.whatdoing != "hurt":
					self.whatdoing = "jump"

				self.vel.y += 0.4
			
			if self.isOnGround and self.isOnWall:
				self.vel.y = -5

			else:
				self.groundType = "air"

		if type == 1:
			if self.vel.y >self.maxvel:
				self.vel.y = self.maxvel
			self.offset.y -= self.vel.y + self.fastfall
			self.offset.x -= self.vel.x
			
		
		if type == 3:
			if self.direction == 1:
				self.hitbox.update(self.pos.x+5, self.pos.y+15, self.frameWidth-45, self.frameHeight-15)
			if self.direction == 0:
				self.hitbox.update(self.pos.x+45, self.pos.y+15, self.frameWidth-45, self.frameHeight-15)

	def actions(self):
		if self.whatdoing == "land":
			self.hitbox.update(self.pos.x+5, self.pos.y+30,self.hitbox.width,self.hitbox.height-15)
			self.landTick += 1
			self.vel.x*=0.96
			if self.landTick == 60:
				self.landTick = 0
				self.whatdoing = "stand"

		if self.whatdoing == "hurt":
			if self.direction == 1:
				self.RowNum = 4
			else:
				self.RowNum = 3
			self.hurtTick += 1
			if self.hurtTick == 60:
				self.hurtTick = 0
				self.whatdoing = "stand"

		# WALK --------------------------------------------------------------------
		if self.whatdoing == "walk":
			if self.direction == 1: #left
				self.RowNum = 1
			if self.direction == 0:
				self.RowNum = 0

			self.ticker+=1
			if self.ticker%15==0:
					self.ticker = 0
					self.frameNum+=1
			if self.frameNum >= 4:
				self.frameNum = 0
		# SPRINT ---------------------------------------------------------------
		if self.whatdoing == "sprint": 
			if self.direction == 1: #left
				self.RowNum = 1
			if self.direction == 0:
				self.RowNum = 0

			self.ticker+=1
			if self.ticker%12==0:
					self.ticker = 0
					self.frameNum+=1
			if self.frameNum >= 3:
				self.frameNum = 0
		# STAND --------------------------------------------------------------------
		if self.whatdoing == "stand":
			if self.direction == 1:
				self.RowNum = 1
			else:
				self.RowNum = 0
			self.ticker+=1
			if self.ticker%15==0:
					self.ticker = 0
					self.frameNum+=1
			if self.frameNum == 7:
				self.RowNum+=3
			if self.frameNum >= 8:
				self.frameNum = 0
			if abs(self.vel.x) != 0:
				self.vel.x*=0.90
			if abs(self.vel.x)<=0.2:
				self.vel.x = 0
		# JUMP --------------------------------------------------------------------
		if self.whatdoing == "jump" or self.whatdoing == "leap":
			if self.direction == 1:
				self.RowNum = 1
			else:
				self.RowNum = 0

			if self.isOnGround and self.isOnWall != True:

				if self.charge >= self.maxleap*0.44:

					if self.groundType != "trampoline":
						self.vel.y-=(22*self.size)

					if self.direction == 0:
						self.vel.x = self.charge/15

					if self.direction == 1:
						self.vel.x = -(self.charge/15)

				elif self.groundType != "trampoline":
					if self.pressed[4]:
						self.vel.y-=(23*self.size)
					else:
						self.vel.y=-(26*self.size)
					
				self.charge = 1
			if self.whatdoing == "leap":
				self.vel.x*=0.6

		if self.whatdoing == "squat":
			self.hitbox.update(self.pos.x+5, self.pos.y+30,self.hitbox.width,self.hitbox.height-15)

			self.vel.x *= 0.7
			if abs(self.vel.x) <0.01:
				self.vel.x = 0
			if self.direction == 1:
				self.RowNum = 4
			else:
				self.RowNum = 3

		if self.whatdoing == "crawl":
			self.hitbox.update(self.pos.x+5, self.pos.y+30,self.hitbox.width,self.hitbox.height-15)
			if self.direction == 1:
				self.RowNum = 4
			else:
				self.RowNum = 3

			self.ticker+=1
			if self.ticker%12==0:
					self.ticker = 0
					self.frameNum+=1
			if self.frameNum >= 2:
				self.frameNum = 0
		
		if self.whatdoing == "slide":
			self.hitbox.update(self.pos.x+5, self.pos.y+30,self.hitbox.width,self.hitbox.height-15)

			self.vel.x*=0.985
			if self.direction == 1:
				self.RowNum = 4
			else:
				self.RowNum = 3

		#if goals are to be added

		#for goal in goals:
        #    if self.pos.x + 10 >= goal.xpos and self.pos.x <= goal.xpos + 20:
        #        if self.pos.y + 30 >= goal.ypos and self.pos.y + 30 <= goal.ypos + 20:
        #            print("goal hit!")
        #            self.xpos = 100
        #            self.ypos = 100
        #            return True  # Change state when player touches a red square



	def draw(self):
		pygame.draw.rect(screen, (50,170,0), self.hitbox)

		if self.whatdoing == "jump" or self.whatdoing == "leap":
			screen.blit(self.possum, self.pos, (self.frameWidth*3, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		elif self.whatdoing == "stand":
			screen.blit(self.possum, self.pos, (self.frameWidth*self.standFrame[self.frameNum], self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		elif self.whatdoing == "walk":
			screen.blit(self.possum, self.pos, (self.frameWidth*self.walkFrame[self.frameNum], self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		elif self.whatdoing == "sprint":
			screen.blit(self.possum, self.pos, (self.frameWidth*self.sprintFrame[self.frameNum], self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		elif self.whatdoing == "land":
			screen.blit(self.possum, self.pos, (self.frameWidth*self.direction, 2*self.frameHeight, self.frameWidth, self.frameHeight))
		elif self.whatdoing == "crawl":
			screen.blit(self.possum, self.pos, (self.frameWidth*self.crawlFrame[self.frameNum], self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		elif self.whatdoing == "squat" or self.whatdoing == "slide":
			screen.blit(self.possum, self.pos, (self.frameWidth, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		elif self.whatdoing == "hurt":
			screen.blit(self.possum, self.pos, (2*self.frameWidth, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		else:
			self.whatdoing = "walk"
		if self.charge<self.maxleap*0.44:
			pygame.draw.line(screen, (255,50,0),(800-self.charge*1.2,880),(800+self.charge*1.2,880),20)
		elif self.charge>=self.maxleap*0.66:
			pygame.draw.line(screen, (255,200,0),(800-self.charge*1.2,880),(800+self.charge*1.2,880),20)
		elif self.charge>=self.maxleap*0.44:
			pygame.draw.line(screen, (50,255,0),(800-self.charge*1.2,880),(800+self.charge*1.2,880),20)
	def damagefun(self):
		return self.damage

	