import pygame
import random
import math
from player import Player
#ehh I'll import player later. I think I'm just gonna play this easy.
pygame.init

screenX = 1800
screenY = 900

#creates game screen and caption
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("leaves")

#game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game speed
ticker = 0

#Constants because Tess is gonna give me an aneurysm
X = 0
Y = 1
DELTA_X = 2
DELTA_Y = 3
SPEED = 4

leafBlowers = []

def updateTicker():
	global ticker
	if ticker < 60:
		ticker += 1
	else:
		ticker = 0

#a better function for telling the angle between two points
#input (y1 - y2, x1 - x2) in order to get two points working.

# def atan2(y, x):
#     def adjustAngle(angle):
#         if angle + 90 > 360:
#             return angle - 270 # + 90 - 360
#         else:
#             return angle + 90
#     num = math.atan2(y, x) * (180/math.pi)
#     if num > 0:
#         #print("atan2 = ", adjustAngle(num), end= ", ")
#         return adjustAngle(num)
#     else:
#         #print("atan2 = ", adjustAngle(180 + (180 - abs(num))), end= ", ")
#         return adjustAngle(180 + (180 - abs(num)))


def tpd(num):
	return math.floor(num*100)/100

#temporary player class containing positions because player class doesn't work right now.
class temp:
	def __init__(self, xpos, ypos):
		self.xpos = xpos
		self.ypos = ypos

#adds the temp class to the leafBlowers (entities) list.
leafBlowers.append(temp(screenX/2, screenY/2))
guy = Player()
class leafSpawner:
	STARTING_SPEED = 0.1
	def __init__(self, leaves):
		self.leaves = [] #this list contains information regarding every single leaf in the game.
		for i in range(leaves): #creates a 2d list containing each leaf.
			tempX = 0
			tempY = 10
			self.leaves.append([ random.randint(0,screenX) + tempX, random.randint(0,screenY)+ tempY, 0, 0, self.STARTING_SPEED]) #random.randint(0, screenX), random.randint(0, screenY), 0, 0]) #xpos, ypos, xvelo, yvelo

	def draw(self, i):
		if i == 1:
			pygame.draw.circle(screen, (255, 0, 0), (self.leaves[i][X], self.leaves[i][Y]), 1)
		else:
			pygame.draw.circle(screen, (0, 255, 0), (self.leaves[i][X], self.leaves[i][Y]), 1)

	def update(self):
		for i in range(len(self.leaves)): #goes through each leaf in the leaves list.
			self.applyPhysics(i)
			self.draw(i)
			# for i in range(len(self.leaves[0])):
				#print(math.floor(self.leaves[0][i] * 100)/100, end = ", ")
			#print()

	def applyPhysics(self, i):
		size = 900
		for j in range(len(leafBlowers)):
			leafDistance = abs(math.sqrt((guy.centerpos.x - self.leaves[i][X]) ** 2 + abs(guy.centerpos.y - self.leaves[i][Y]) ** 2))
			#leafDistance = abs(math.sqrt((leafBlowers[j].xpos - self.leaves[i][X]) ** 2 + abs(leafBlowers[j].ypos - self.leaves[i][Y]) ** 2))
			# leafDistance = abs(math.sqrt((guy.centerpos.x - self.leaves[i][X]) ** 2 + abs(guy.centerpos.y - self.leaves[i][Y]) ** 2))
			if leafDistance == 0:
				leafDistance = .01
				self.leaves[i][X] += 0.01
			if leafDistance <= size: #checks if the leaf is in the range of the current leafblower

				#Finds the angle between leaf & leafblower
				angle = math.atan2(float(self.leaves[i][Y] - guy.centerpos.y), float(self.leaves[i][X] - guy.centerpos.x))
				# angle = math.atan2(float(self.leaves[i][Y] - leafBlowers[j].ypos), float(self.leaves[i][X] - leafBlowers[j].xpos))
				# angle = math.degrees(math.atan2(guy.centerpos.x - self.leaves[i][X], guy.centerpos.y - self.leaves[i][Y]))

				#Convert that angle to coordinates, extend to the correct size so that it picks a point along the leafblower's bounds
				endX = int((math.cos(angle) * size) + guy.centerpos.x)
				endY = int((math.sin(angle) * size) + guy.centerpos.y)

				#Linear algebra stuff, takes the distance between the current and end position, converts that to a ratio that can be used to make leaves move at a constant speed
				xDistance = endX - self.leaves[i][X]
				yDistance = endY - self.leaves[i][Y]
				magnitude = math.sqrt((xDistance)**2 + (yDistance)**2)
				if magnitude == 0:
					#Prevent divide by zero error
					magnitude = 0.01
				yDir = yDistance/magnitude
				xDir = xDistance/magnitude

				self.leaves[i][SPEED] += 0.5

				#sets the velocities
				self.leaves[i][DELTA_X] = xDir * self.leaves[i][SPEED]
				self.leaves[i][DELTA_Y] = yDir * self.leaves[i][SPEED]
			   # pygame.draw.line(screen, (255, 0, 0), (leafBlowers[j].xpos, leafBlowers[j].ypos), (self.))
			else:
				#resets speed
				self.leaves[i][SPEED] = self.STARTING_SPEED
				
				#applies drag
				self.drag(i)

		#moves the leaf
		self.leaves[i][X] += self.leaves[i][DELTA_X] / 4
		self.leaves[i][Y] += self.leaves[i][DELTA_Y] / 4

		if self.leaves[i][X] < 0:
			self.leaves[i][X] += screenX
		elif self.leaves[i][X] > screenX:
			self.leaves[i][X] -= screenX

		if self.leaves[i][Y] < 0:
			self.leaves[i][Y] += screenY
		elif self.leaves[i][Y] > screenY:
			self.leaves[i][Y] -= screenY

	def drag(self, i):
		dragVal = .4

		if abs(self.leaves[i][DELTA_X]) <= dragVal:
			self.leaves[i][DELTA_X] = 0
		elif self.leaves[i][DELTA_X] > 0:
			self.leaves[i][DELTA_X] -= dragVal
		elif self.leaves[i][DELTA_X] < 0:
			self.leaves[i][DELTA_X] += dragVal


		if abs(self.leaves[i][DELTA_Y]) <= dragVal:
			self.leaves[i][DELTA_Y] = 0
		elif self.leaves[i][DELTA_Y] > 0:
			self.leaves[i][DELTA_Y] -= dragVal
		elif self.leaves[i][DELTA_Y] < 0:
			self.leaves[i][DELTA_Y] += dragVal

#SEBASTIAN WILL FIX THIS LATER
def draw():
	angle = math.degrees(math.atan2(-guy.vel.y,guy.vel.x)) - guy.correctionangle
		
	if abs(guy.vel.x) > 1 and abs(guy.vel.y) > 1:
		guy.transformed_image = pygame.transform.rotate(guy.image, angle)
		
	#screen.blit(guy.transformed_image, (guy.newMousePos.x-64,guy.newMousePos.y-64))

leeevs = leafSpawner(2000)

#BEGIN GAME LOOP######################################################
while not doExit:
	
	delta = clock.tick(60) / 1000 #FPS (frames per second)
	updateTicker()
	screen.fill((0,0,0))

	pygame.draw.circle(screen, (255, 255, 255), (screenX/2, screenY/2), 1)

	#pygame's way of listening for events (key presses, mouse clicks, etc)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			doExit = True #lets you quit program

	leeevs.update()
	guy.update(delta)

	draw()


	pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()