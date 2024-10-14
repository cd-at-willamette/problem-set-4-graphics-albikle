########################################
# Name: Anna Bikle
# Collaborators:
# Estimate time spent (hrs): 2 hrs
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score



def clicky_box():
    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    
    #Square and its starting position
    start_x= (GW_WIDTH- SQUARE_SIZE)/ 2
    start_y= (GW_HEIGHT- SQUARE_SIZE)/ 2
    box= GRect(start_x, start_y, SQUARE_SIZE, SQUARE_SIZE)
    box.set_filled(True)
    box.set_color("Pink")
    gw.add(box)
    
    #Makes score label
    score= 0
    score_label= GLabel(f"Score: {score}", SCORE_DX, GW_HEIGHT- SCORE_DY)
    score_label.set_font(SCORE_FONT)
    gw.add(score_label)

    # Defining the callback function, which you won't need until Part C
    def on_mouse_down(event):
        nonlocal score
        #Checks if click is in the box, if so...
        if event.get_x()>= box.get_x() and event.get_x()<= box.get_x()+ SQUARE_SIZE and event.get_y()>= box.get_y() and event.get_y()<= box.get_y()+ SQUARE_SIZE:
            new_x= random.randint(0, GW_WIDTH- SQUARE_SIZE)
            new_y= random.randint(0, GW_HEIGHT- SQUARE_SIZE)
            # Move the square to the new location
            box.setLocation(new_x, new_y)
            score+= 1
        #Resets score
        else:
            score= 0
        
        #Updates the score
        score_label.setLabel(f"Score: {score}")

    gw.add_event_listener("click", on_mouse_down)


if __name__ == '__main__':
    clicky_box()
