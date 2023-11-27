import pygame
from pygame.math import Vector2
from pygame.rect import Rect
pygame.init() 
pygame.mixer.init()
pygame.display.set_caption("platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop
global ground
ground = Vector2(0,700)

class Possum:

	def __init__(self):
		self.possum1 = pygame.image.load('possumsprite7.png')
		self.possum = pygame.transform.smoothscale_by(self.possum1,0.8)
		 #load your spritesheet
		self.chirp = pygame.mixer.Sound("chrip.mp3")


		self.pos = Vector2(0,0)
		self.isOnGround = False
		self.vel = Vector2(0,0)
		self.keys = [False, False, False, False, False, False]
		self.whatdoing = "stand"
		self.direction = 1
		self.frameNum = 0
		self.RowNum = 1

		self.chirping = False
		self.charge = 0
		self.fastfall = 0

		self.landTick = 0
		self.ticker = 0

		self.frameWidth = 249*0.8
		self.frameHeight = 100*0.8

		#self.hitbox = {"top":self.pos.y+15, "left":self.pos.x, "bottom":self.pos.y+self.frameHeight, "right":self.pos.x+self.frameWidth}
		self.hitbox = Rect(self.pos.x+5, self.pos.y+18, self.frameWidth, self.frameHeight)
		# left top width height
		self.walkFrame = [2,1,0,1]
		self.sprintFrame = [2,3,3]
		self.crawlFrame = [0,1]

		self.standFrame = [1,1,1,1,1,1,1,3]
		self.standRow = [self.RowNum,self.RowNum,self.RowNum,self.RowNum+3,self.RowNum,self.RowNum,self.RowNum,self.RowNum+3]


	def getKeyPressed(self):

		for event in pygame.event.get(): 
			
			if event.type == pygame.QUIT:
				global gameover 
				gameover = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.keys[0]=True
				if event.key == pygame.K_RIGHT:
					self.keys[1]=True
				if event.key == pygame.K_UP or event.key == pygame.K_x or event.key == pygame.K_k or event.key == pygame.K_w:
					self.keys[2]=True
				if event.key == pygame.K_DOWN or event.key == pygame.K_z or event.key == pygame.K_l or event.key == pygame.K_s:
					self.keys[3] = True
				if event.key == pygame.K_LSHIFT or event.key == pygame.K_c or event.key == pygame.K_j:
					self.keys[4] = True
				if event.key == pygame.K_v:
					self.keys[5] = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.keys[0]=False
				if event.key == pygame.K_RIGHT:
					self.keys[1]=False
				if event.key == pygame.K_UP or event.key == pygame.K_x or event.key == pygame.K_k or event.key == pygame.K_w:
					self.keys[2]=False
				if event.key == pygame.K_DOWN or event.key == pygame.K_z or event.key == pygame.K_l or event.key == pygame.K_s:
					self.keys[3] = False
				if event.key == pygame.K_LSHIFT or event.key == pygame.K_c or event.key == pygame.K_j:
					self.keys[4] = False
				if event.key == pygame.K_v:
					self.keys[5] = False

	def playerInput(self):
		walkspeed = 3.5
		sprintspeed = 12
		


		if self.keys[5] == True:
			if self.chirping == False:
				self.whatdoing = "chirp"
		elif self.keys[5] == False:
			if self.isOnGround == True and self.whatdoing != "walk" and self.whatdoing != "land":
				self.whatdoing = "stand"
			self.chirping = False
			pygame.mixer.Sound.stop(self.chirp)

		if self.keys[3] == True:
			if self.isOnGround == True:
				self.whatdoing = "squat"
				self.charge += 1.4
				if self.charge >= 100:
					self.charge = 100
				self.fastfall = 0
			if self.isOnGround == False:
				self.fastfall += 0.1

		elif self.keys[3] == False:
			if self.isOnGround == True and self.whatdoing != "walk" and self.whatdoing != "land" and self.whatdoing != "chirp":
				self.whatdoing = "stand"
				self.charge = 1
			self.fastfall = 0


		if self.keys[0]==True:
			if self.whatdoing != "squat" and self.isOnGround == True:
				self.whatdoing = "walk"
			elif self.whatdoing == "squat":
				self.whatdoing = "crawl"
			if self.keys[4] == True:
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

		elif self.keys[1] == True:
			if self.whatdoing != "squat" and self.isOnGround == True:
				self.whatdoing = "walk"
			elif self.whatdoing == "squat":
				self.whatdoing = "crawl"

			if self.keys[4] == True:
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
			if self.whatdoing != "land" and self.whatdoing != "squat" and self.isOnGround == True and self.whatdoing!= "chirp":
				self.whatdoing = "stand"
			if self.isOnGround == False:
				if abs(self.vel.x) != 0:
					self.vel.x*=0.98
				if abs(self.vel.x)<=0.2:
					self.vel.x = 0

		if self.keys[2] == True:
			self.whatdoing = "jump"
		if self.whatdoing != "chirp":
			pygame.mixer.Sound.stop(self.chirp)

	def collision(self, objPos:Vector2):
		if self.hitbox.bottom >= objPos.y:
			self.isOnGround = True
		else:
			self.isOnGround = False

	def update(self,type):
		if type == 0:
			print(self.vel.x)
			if self.isOnGround == True:
				if self.vel.y >= 14:
					self.whatdoing = "land"
				elif self.keys[4] == True:
					self.whatdoing = "sprint"
				elif self.keys[3] == True:
					self.whatdoing = "squat"
				self.vel.y = 0
			elif self.isOnGround == False:
				if self.whatdoing != "chirp":
					self.whatdoing = "jump"
				self.vel.y += 0.4

		if type == 1:
			self.pos.x+=self.vel.x 
			self.pos.y+=self.vel.y+self.fastfall
		
		if type == 3:
			self.hitbox.topleft = (int(self.pos.x), int(self.pos.y))

	def actions(self):

		if self.whatdoing == "land":
			self.landTick += 1
			self.vel.x*=0.96
			if self.landTick == 60:
				self.landTick = 0
				self.whatdoing = "stand"
			#adbayuvduywiytfvayttttttttttttttttttttteasfgwiuyefvukywaefiwvfi7uawfuy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			#self.pos.y = ground.y
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
				#self.pos.y = 499
				self.vel.y=-(8+(self.charge/10))
				self.charge = 1

		if self.whatdoing == "squat":
			self.hitbox.top = int(self.pos.y+40)
			
			if self.keys[4] == True:
				self.vel.x*=0.985
			else:
				self.vel.x*=0.96
			if self.direction == 1:
				self.RowNum = 4
			else:
				self.RowNum = 3

		if self.whatdoing == "crawl":
			#self.hitbox.top = int(self.pos.y+40)
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
		#else:
			#self.hitbox.top = int(self.pos.y+18)

		if self.whatdoing == "chirp":
			self.vel.x = 0
			if self.direction == 1:
				self.RowNum = 4
			else:
				self.RowNum = 3
			if self.chirping == False:
				self.ticker = 0
				pygame.mixer.Sound.play(self.chirp)
				self.chirping = True
			if self.chirping == True:
				self.ticker+=1
			if self.ticker >= 300:
				self.ticker = 0
				pygame.mixer.Sound.stop(self.chirp)

	def draw(self):
		#print(f"HEIGHT: {self.frameHeight}        WIDTH: {self.frameWidth}")
		pygame.draw.rect(screen, (50,170,0), self.hitbox)
		if self.whatdoing == "jump" or self.whatdoing == "leap":
			screen.blit(self.possum, (self.pos.x, self.pos.y), (self.frameWidth*3, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		elif self.whatdoing == "stand":
			screen.blit(self.possum, (self.pos.x, self.pos.y), (self.frameWidth*self.standFrame[self.frameNum], self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		elif self.whatdoing == "walk":
			screen.blit(self.possum, (self.pos.x, self.pos.y), (self.frameWidth*self.walkFrame[self.frameNum], self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		elif self.whatdoing == "sprint":
			screen.blit(self.possum, (self.pos.x, self.pos.y), (self.frameWidth*self.sprintFrame[self.frameNum], self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		elif self.whatdoing == "land":
			screen.blit(self.possum, (self.pos.x, self.pos.y), (self.frameWidth*self.direction, 2*self.frameHeight, self.frameWidth, self.frameHeight))
		elif self.whatdoing == "crawl":
			screen.blit(self.possum, (self.pos.x, self.pos.y), (self.frameWidth*self.crawlFrame[self.frameNum], self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		elif self.whatdoing == "squat":
			screen.blit(self.possum, (self.pos.x, self.pos.y), (self.frameWidth, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		elif self.whatdoing == "chirp":
			screen.blit(self.possum, (self.pos.x, self.pos.y), (2*self.frameWidth, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
		else:
			self.whatdoing = "walk"

		
character = Possum()

while not gameover:

	clock.tick(60)

	character.update(3)

	character.collision(ground)

	character.update(0)

	character.getKeyPressed()

	character.playerInput()

	character.actions()

	character.update(1)
	

	screen.fill((200,210,200))
	character.draw()
	pygame.draw.line(screen, (180,190,180),(0,ground.y),(800,ground.y),1)
	pygame.display.flip()

pygame.quit()

	
