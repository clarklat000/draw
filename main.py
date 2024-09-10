import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

display_surface.fill(BLACK)
top = (500,100)
radius = 100
pygame.draw.circle(display_surface, WHITE,top,radius )


Top_left_X = 100
top_left_Y =400
width =300
height = 200
Data = (Top_left_X, top_left_Y, width, height)
pygame.draw.rect(display_surface, YELLOW, Data)

start = (100,100)
end = (500,500)
pygame.draw.line(display_surface,RED,start,end, 5)

start = (400,300)
end = (500,500)
pygame.draw.line(display_surface,RED,start,end, 5)





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()