import pgzrun 
WIDTH = 600
HEIGHT =  600 
player = Actor("player")
player.x = 200
player.y = 200
goalpost = Actor("goalpost")
goalpost.x = 300
goalpost.y = 500
ball = Actor("football")
ball.x = 300
ball.y = 300
def draw():
    screen.fill("Green")
    player.draw()
    ball.draw()
    goalpost.draw()

def update():
    if keyboard.w: 
        player.y-=3
    if keyboard.a:
        player.x-=3 
    if keyboard.s:
        player.y+=3 
    if keyboard.d:
        player.x+=3 


pgzrun.go() 