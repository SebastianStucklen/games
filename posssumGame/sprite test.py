import pygame
from pygame.math import Vector2
pygame.init() 
pygame.mixer.init()
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

possum = pygame.image.load('possumsprite7.png') #load your spritesheet
chirp = pygame.mixer.Sound("chrip.mp3")
#Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

#player variables
pos = Vector2(508,500)
ground = 508
isOnGround = True
vel = Vector2(0,0)
keys = [False, False, False, False, False, False] #this list holds whether each key has been pressed
whatdoing = "walk"
landTick = 0
direction = 1
#animation variables variables
frameWidth = 249
frameHeight = 100

charge = 1
fastfall = 0
RowNum = 1 #for left animation, this will need to change for other animations

chirping = False

frameNum = 0

ticker = 0

walkspeed = 3.5
sprintspeed = 12

walkFrame = [2,1,0,1]
sprintFrame = [2,3,3]
crawlFrame = [0,1]

standFrame = [1,1,1,1,1,1,1,3]
standRow = [RowNum,RowNum,RowNum,RowNum+3,RowNum,RowNum,RowNum,RowNum+3]




while not gameover:
	clock.tick(60) #FPS

	if pos.y < ground:
		isOnGround = False
	elif pos.y >= ground:
		isOnGround = True

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			gameover = True
	  
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				keys[0]=True
			if event.key == pygame.K_RIGHT:
				keys[1]=True
			if event.key == pygame.K_UP or event.key == pygame.K_x or event.key == pygame.K_k or event.key == pygame.K_w:
				keys[2]=True
			if event.key == pygame.K_DOWN or event.key == pygame.K_z or event.key == pygame.K_l or event.key == pygame.K_s:
				keys[3] = True
			if event.key == pygame.K_LSHIFT or event.key == pygame.K_c or event.key == pygame.K_j:
				keys[4] = True
			if event.key == pygame.K_v:
				keys[5] = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				keys[0]=False
			if event.key == pygame.K_RIGHT:
				keys[1]=False
			if event.key == pygame.K_UP or event.key == pygame.K_x or event.key == pygame.K_k or event.key == pygame.K_w:
				keys[2]=False
			if event.key == pygame.K_DOWN or event.key == pygame.K_z or event.key == pygame.K_l or event.key == pygame.K_s:
				keys[3] = False
			if event.key == pygame.K_LSHIFT or event.key == pygame.K_c or event.key == pygame.K_j:
				keys[4] = False
			if event.key == pygame.K_v:
				keys[5] = False
		  
	if keys[5] == True:
		if chirping == False:
			whatdoing = "chirp"
	elif keys[5] == False:
		if isOnGround:
			whatdoing = "stand"
		chirping = False
		pygame.mixer.Sound.stop(chirp)

	if keys[3] == True:
		if isOnGround == True:
			whatdoing = "squat"
			charge += 1.4
			if charge >= 100:
				charge = 100
		if isOnGround == False:
			fastfall += 0.1

	elif keys[3] == False:
		if isOnGround == True and whatdoing != "walk" and whatdoing != "land" and whatdoing != "chirp":
			whatdoing = "stand"
			charge = 1
		if isOnGround ==  False:
			fastfall = 0


	if keys[0]==True:
		if whatdoing != "squat" and isOnGround == True:
			whatdoing = "walk"
		elif whatdoing == "squat":
			whatdoing = "crawl"
		if keys[4] == True:
			if whatdoing != "jump":
				whatdoing = "sprint"
			if vel.x > -sprintspeed:
				vel.x-=0.6
			else:
				vel.x = -sprintspeed
		else:
			#whatdoing = "walk"
			if vel.x < -walkspeed:
				vel.x += 0.5
			else:
				vel.x= -walkspeed
		direction = 1

	elif keys[1] == True:
		if whatdoing != "squat" and isOnGround == True:
			whatdoing = "walk"
		elif whatdoing == "squat":
			whatdoing = "crawl"

		if keys[4] == True:
			if whatdoing != "jump":
				whatdoing = "sprint"
			if vel.x < sprintspeed:
				vel.x+=0.6
			else:
				vel.x = sprintspeed
		else:
			#whatdoing = "walk"
			if vel.x > walkspeed:
				vel.x -= 0.5
			else:
				vel.x= walkspeed
		direction = 0


	else:
		if whatdoing != "land" and whatdoing != "squat" and isOnGround == True and whatdoing!= "chirp":
			whatdoing = "stand"
		if isOnGround == False:
			if abs(vel.x) != 0:
				vel.x*=0.98
			if abs(vel.x)<=0.2:
				vel.x = 0

	if keys[2] == True:
		whatdoing = "jump"
		#vel.yscale*=1.01
	#print(vel.yscale)
	if whatdoing != "chirp":
		pygame.mixer.Sound.stop(chirp)
	#print(charge)
	
		

	if isOnGround == False:
		if whatdoing != "chirp":
			whatdoing = "jump"
		vel.y += 0.4
	elif isOnGround == True:
		if vel.y > 0:
			if keys[0] == False and keys[1] == False and keys[2] == False:
				whatdoing = "land"
			else:
				if keys[4] == True:
					whatdoing = "sprint"
				else:
					whatdoing = "walk"
		vel.y = 0

	# LAND --------------------------------------------------------------------
	if whatdoing == "land":
		landTick += 1
		#print(vel.x)
		vel.x*=0.96
		if landTick == 60:
			landTick = 0
			whatdoing = "stand"
		pos.y = ground
	# WALK --------------------------------------------------------------------
	if whatdoing == "walk":
		if direction == 1: #left
			RowNum = 1
		if direction == 0:
			RowNum = 0

		ticker+=1
		if ticker%15==0:
				ticker = 0
				frameNum+=1
		if frameNum >= 4:
			frameNum = 0
	# SPRINT ---------------------------------------------------------------
	if whatdoing == "sprint": 
		if direction == 1: #left
			RowNum = 1
		if direction == 0:
			RowNum = 0

		ticker+=1
		if ticker%12==0:
				ticker = 0
				frameNum+=1
		if frameNum >= 3:
			frameNum = 0
	# STAND --------------------------------------------------------------------
	if whatdoing == "stand":
		if direction == 1:
			RowNum = 1
		else:
			RowNum = 0
		ticker+=1
		if ticker%15==0:
				ticker = 0
				frameNum+=1
		if frameNum == 7:
			RowNum+=3
		if frameNum >= 8:
			frameNum = 0
		if abs(vel.x) != 0:
			vel.x*=0.90
		if abs(vel.x)<=0.2:
			vel.x = 0
	# JUMP --------------------------------------------------------------------
	if whatdoing == "jump":
		if direction == 1:
			RowNum = 1
		else:
			RowNum = 0
		if isOnGround == True:
			pos.y = 499
			vel.y=-(8+(charge/10))
			charge = 1

	if whatdoing == "squat":
		if keys[4] == True:
			vel.x*=0.985
		else:
			vel.x*=0.96
		if direction == 1:
			RowNum = 4
		else:
			RowNum = 3
	if whatdoing == "crawl":
		if direction == 1:
			RowNum = 4
		else:
			RowNum = 3

		ticker+=1
		if ticker%12==0:
				ticker = 0
				frameNum+=1
		if frameNum >= 2:
			frameNum = 0

	if whatdoing == "chirp":
		vel.x = 0
		if direction == 1:
			RowNum = 4
		else:
			RowNum = 3
		if chirping == False:
			ticker = 0
			pygame.mixer.Sound.play(chirp)
			chirping = True
		if chirping == True:
			ticker+=1
		if ticker >= 300:
			ticker = 0
			pygame.mixer.Sound.stop(chirp)

	pos.x+=vel.x 
	pos.y+=vel.y+fastfall

	if pos.y > ground:
		pos.y = ground
	#print(pos.y)
	#ANIMATION-------------------------------------------------------------------
	#print(isOnGround)
	
	# RENDER--------------------------------------------------------------------------------
	# Once we've figured out what frame we're on and where we are, time to render.
			
	screen.fill((200,210,200)) #wipe screen so it doesn't smear
	pygame.draw.rect(screen, (180,190,180),(0,500+frameHeight,800,500-frameHeight))
	if whatdoing == "jump" or whatdoing == "leap":
		screen.blit(possum, (pos.x, pos.y), (frameWidth*3, RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "stand":
		screen.blit(possum, (pos.x, pos.y), (frameWidth*standFrame[frameNum], RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "walk":
		screen.blit(possum, (pos.x, pos.y), (frameWidth*walkFrame[frameNum], RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "sprint":
		screen.blit(possum, (pos.x, pos.y), (frameWidth*sprintFrame[frameNum], RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "land":
		screen.blit(possum, (pos.x, pos.y), (frameWidth*direction, 2*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "crawl":
		screen.blit(possum, (pos.x, pos.y), (frameWidth*crawlFrame[frameNum], RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "squat":
		screen.blit(possum, (pos.x, pos.y), (frameWidth, RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "chirp":
		screen.blit(possum, (pos.x, pos.y), (2*frameWidth, RowNum*frameHeight, frameWidth, frameHeight))
	else:
		whatdoing = "walk"
	pygame.display.flip()#this actually puts the pixel on the screen
	
#end game loop------------------------------------------------------------------------------
pygame.quit()