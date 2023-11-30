#import os
#os.chdir("posssumGame")
import pygame
from pygame.math import Vector2
from pygame.rect import Rect
pygame.init() 
pygame.mixer.init()

screen = pygame.display.set_mode((800, 800))  # creates game screen



class Possum:

	def __init__(self):

		self.damage = 100
		self.possum1 = pygame.image.load('resources/possumsprite7.png')
		self.possum = pygame.transform.smoothscale_by(self.possum1,0.6)
		 #load your spritesheet
		#self.chirp = pygame.mixer.Sound("resources/chrip.mp3")
		self.frameWidth = 249*0.6
		self.frameHeight = 100*0.6

		#Pos and Vel
		self.pos = Vector2(330,300)
		self.isOnGround = False
		self.vel = Vector2(0,0)
		self.offset = 0

		#action
		self.pressed = [False, False, False, False, False, False]
		self.whatdoing = "stand"
		self.direction = 1
		self.chirping = False
		self.charge = 0
		self.fastfall = 0

		#collison
		self.groundType = "normal"
		self.objPos = Rect(0,0,0,0)
		self.platList = []

		#anim
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
		keys = pygame.key.get_pressed()
		walkspeed = 3.5
		sprintspeed = 12
	#------------------------------------------------------------------------------------------------
		if keys[pygame.K_DOWN]:# or keys[pygame.K_z]:
			self.pressed[3] = True
			if self.isOnGround == True:
				self.whatdoing = "squat"
				self.charge += 1.4
				if self.charge >= 100:
					self.charge = 100
				self.fastfall = 0
			if self.isOnGround == False:
				self.fastfall += 0.1
		else:
			self.pressed[3]=False
			self.fastfall = 0
			if self.isOnGround == True:
				if self.charge > 0:
					self.charge -= 1.7
				if self.charge <= 1:
					self.charge = 1
	#------------------------------------------------------------------------------------------------
		if keys[pygame.K_LEFT]:
			self.pressed[0]=True
			if self.whatdoing != "squat" and self.isOnGround == True:
				self.whatdoing = "walk"
			elif self.whatdoing == "squat":
				self.whatdoing = "crawl"

			if keys[pygame.K_LSHIFT]:
				if self.whatdoing != "jump":
					self.whatdoing = "sprint"
				if self.vel.x > -sprintspeed:
					self.vel.x-=0.6
				else:
					self.vel.x = -sprintspeed
			else:
				if self.vel.x < -walkspeed:
					self.vel.x += 0.5
				else:
					self.vel.x= -walkspeed
			self.direction = 1
		else:
			self.pressed[0]=False
	#------------------------------------------------------------------------------------------------
		if keys[pygame.K_RIGHT]:
			self.pressed[1]=True
			if self.whatdoing != "squat" and self.isOnGround == True:
				self.whatdoing = "walk"
			elif self.whatdoing == "squat":
				self.whatdoing = "crawl"

			if keys[pygame.K_LSHIFT]:
				if self.whatdoing != "jump":
					if self.whatdoing == "squat":
						self.whatdoing = "crawl"
					else:
						self.whatdoing = "sprint"
				if self.vel.x < sprintspeed:
					self.vel.x+=0.6
				else:
					self.vel.x = sprintspeed
			else:
				if self.vel.x > walkspeed:
					self.vel.x -= 0.5
				else:
					self.vel.x= walkspeed
			self.direction = 0

		else:
			self.pressed[1]=False
	#------------------------------------------------------------------------------------------------
		if keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False:
			if self.isOnGround == False:
				if abs(self.vel.x) != 0:
					self.vel.x*=0.98
				if abs(self.vel.x)<=0.2:
					self.vel.x = 0
	#------------------------------------------------------------------------------------------------
		if keys[pygame.K_UP]:# or keys[pygame.K_x]:
			self.pressed[2]=True
			self.whatdoing = "jump"
			if self.isOnGround == True:
				self.hitbox.bottom+=1
		else:
			self.pressed[2]=False
	#------------------------------------------------------------------------------------------------
		if keys[pygame.K_LSHIFT]:
			self.pressed[4] = True
		else:
			self.pressed[4] = False

			
	def ybuydauyed(self):
		#def playerInput(self):
			#walkspeed = 3.5
			#sprintspeed = 12


			# chirp
			#if keys[5] == True:
			#	if self.chirping == False: # only chirps if not already chirping
			#		self.whatdoing = "chirp"
			#elif keys[5] == False:
			#	#if self.isOnGround == True and self.whatdoing != "walk" and self.whatdoing != "land":
			#	#	self.whatdoing = "stand"
			#	self.chirping = False
			#	pygame.mixer.Sound.stop(self.chirp)

			#if self.pressed[3] == True:
			#	if self.isOnGround == True:
			#		self.whatdoing = "squat"
			#		self.charge += 1.4
			#		if self.charge >= 100:
			#			self.charge = 100
			#		self.fastfall = 0
			#	if self.isOnGround == False:
			#		self.fastfall += 0.1
			#elif self.pressed[3] == False:
			#	self.fastfall = 0
			#	if self.isOnGround == True:
			#		if self.charge > 0:
			#			self.charge -= 1.7
			#		if self.charge <= 1:
			#			self.charge = 1




			#if self.pressed[0]==True:
			#	if self.whatdoing != "squat" and self.isOnGround == True:
			#		self.whatdoing = "walk"
			#	elif self.whatdoing == "squat":
			#		self.whatdoing = "crawl"
			#	if self.pressed[4] == True:
			#		if self.whatdoing != "jump":
			#			self.whatdoing = "sprint"
			#		if self.vel.x > -sprintspeed:
			#			self.vel.x-=0.6
			#		else:
			#			self.vel.x = -sprintspeed
			#	else:
			#		if self.vel.x < -walkspeed:
			#			self.vel.x += 0.5
			#		else:
			#			self.vel.x= -walkspeed
			#	self.direction = 1
#	
			#elif self.pressed[1] == True:
			#	if self.whatdoing != "squat" and self.isOnGround == True:
			#		self.whatdoing = "walk"
			#	elif self.whatdoing == "squat":
			#		self.whatdoing = "crawl"
#	
			#	if self.pressed[4] == True:
			#		if self.whatdoing != "jump":
			#			if self.whatdoing == "squat":
			#				self.whatdoing = "crawl"
			#			else:
			#				self.whatdoing = "sprint"
			#		if self.vel.x < sprintspeed:
			#			self.vel.x+=0.6
			#		else:
			#			self.vel.x = sprintspeed
			#	else:
			#		if self.vel.x > walkspeed:
			#			self.vel.x -= 0.5
			#		else:
			#			self.vel.x= walkspeed
			#	self.direction = 0


			#else:
			#	#if self.whatdoing != "land" and self.whatdoing != "squat" and self.isOnGround == True and self.whatdoing!= "chirp":
			#	#	self.whatdoing = "stand"
			#	if self.isOnGround == False:
			#		if abs(self.vel.x) != 0:
			#			self.vel.x*=0.98
			#		if abs(self.vel.x)<=0.2:
			#			self.vel.x = 0

			#if self.pressed[2] == True:
			#	self.whatdoing = "jump"
			##if self.whatdoing != "chirp":
			##	pygame.mixer.Sound.stop(self.chirp)
		pass
	def getPlatty(self,num:int):
		for i in range(num):
			self.platList.append(False)


	def collision(self, objPos:Rect, groundType:str,num:int):

		if self.hitbox.colliderect(objPos):
			if self.hitbox.top >= objPos.bottom:
				self.vel.y = 0.1
			elif self.hitbox.bottom >= objPos.top:
				self.groundType = groundType
				self.objPos.update(objPos.left, objPos.top, objPos.width, objPos.height)
				self.platList[num] = True
			
		else:
			self.platList[num] = False

		#if self.groundType == "normal":
		#	pass
		#if self.groundType == "Ice":
		#	pass
		#elif self.groundType == "trampoline":
		#	self.vel.y -= 10
		#elif self.groundType == "Moveblock":
		#	pass
		#elif self.groundType == "breakblock":
		#	pass

	
	def update(self,type):
		groundNum = 0
		if type == 0:
			for i in range(len(self.platList)):
				if self.platList[i] == True:
						groundNum += 1
				if groundNum > 0:
					self.isOnGround = True
				else:
					self.isOnGround = False
			if self.isOnGround == True:

				self.hitbox.bottom = self.objPos.top

				if self.vel.y >= 14:
					self.whatdoing = "land"
				elif self.whatdoing != "land":
					nothingDoing = 0
					for i in range(len(self.pressed)):
						nothingDoing += 1
					if nothingDoing == len(self.pressed):
						self.whatdoing = "stand"
				self.vel.y = 0
				self.fastfall = 0

			if self.isOnGround == False:
				self.whatdoing = "jump"
				self.vel.y += 0.4
		if type == 1:
			#self.hitbox.left+=int(self.vel.x) 
			#self.hitbox.bottom+=int(self.vel.y+self.fastfall)
			#self.pos.x += self.vel.x
			self.pos.y += self.vel.y+self.fastfall
			self.offset-=self.vel.x
			
		
		if type == 3:
			self.hitbox.update(self.pos.x+5, self.pos.y+15, self.frameWidth-5, self.frameHeight-15)

		

	def actions(self):

		if self.whatdoing == "land":
			self.landTick += 1
			self.vel.x*=0.96
			if self.landTick == 60:
				self.landTick = 0
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
		if self.whatdoing == "jump":
			if self.direction == 1:
				self.RowNum = 1
			else:
				self.RowNum = 0
			if self.isOnGround == True:
				self.vel.y=-(9+(self.charge/10))
				self.charge = 1

		if self.whatdoing == "squat":
			#self.hitbox.top = int(self.hitbox.bottom+40)
			#self.hitbox.height = int(self.frameHeight-40)
			#self.hitbox.inflate_ip(1,0.1)
			self.hitbox.update(self.pos.x+5, self.pos.y+30,self.hitbox.width,self.hitbox.height-15)

			self.vel.x*=0.985
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
			self.vel.x*=(7/12)
			self.ticker+=1
			if self.ticker%12==0:
					self.ticker = 0
					self.frameNum+=1
			if self.frameNum >= 2:
				self.frameNum = 0
		

		#if self.whatdoing == "chirp":
		#	self.vel.x = 0
		#	if self.direction == 1:
		#		self.RowNum = 4
		#	else:
		#		self.RowNum = 3
		#	if self.chirping == False:
		#		self.ticker = 0
		#		pygame.mixer.Sound.play(self.chirp)
		#		self.chirping = True
		#	if self.chirping == True:
		#		self.ticker+=1
		#	if self.ticker >= 300:
		#		self.ticker = 0
		#		pygame.mixer.Sound.stop(self.chirp)


	def draw(self):
		pygame.draw.rect(screen, (50,170,0), self.hitbox)
		#( self.hitbox.left, self.hitbox.top-15)
		#( self.hitbox.left, self.hitbox.top-30)
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
		elif self.whatdoing == "squat":
			screen.blit(self.possum, self.pos, (self.frameWidth, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		#elif self.whatdoing == "chirp":
		#	screen.blit(self.possum, self.pos, (2*self.frameWidth, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		else:
			self.whatdoing = "walk"
		pygame.draw.line(screen, (180,190,0),(400-self.charge*0.7,780),(400+self.charge*0.7,780),20)
	def damagefun(self):
		return self.damage

	
