########################################
# Name: Anna Bikle
# Collaborators:
# Estimated time spent (hrs): 1 hr
########################################

from pgl import GWindow, GRect

WIDTH = 400
HEIGHT = 400
BRICK_WIDTH = 10
BRICK_HEIGHT = 10
BRICKS_IN_BASE = 10

def draw_pyramid(BRICKS_IN_BASE):
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """
    gw = GWindow(WIDTH, HEIGHT)

    # You got it from here
    
    #Calculate pyramid height
    pyramid_height= BRICK_HEIGHT* BRICKS_IN_BASE

    #Calculate starting y position
    base_y = (HEIGHT / 2) + (pyramid_height / 2) - BRICK_HEIGHT
    
    #Rectange function
    def my_rect(x, y, w, h):
        rect = GRect(x, y, w, h)
        gw.add(rect)

    #Calculates position and number of bricks in each row
    for row in range(BRICKS_IN_BASE):
        bricks_in_row = BRICKS_IN_BASE - row  #Calculates number of bricks in the row
        base_x = (WIDTH / 2) - (bricks_in_row * BRICK_WIDTH / 2)  #Calculate starting x position

        #Draws each brick in the row
        for brick in range(bricks_in_row):
            x = base_x + brick * BRICK_WIDTH  #x position of the brick
            y = base_y - row * BRICK_HEIGHT   #y position of the brick
            my_rect(x, y, BRICK_WIDTH, BRICK_HEIGHT) #Draws brick
            

if __name__ == '__main__':
    draw_pyramid(BRICKS_IN_BASE)
