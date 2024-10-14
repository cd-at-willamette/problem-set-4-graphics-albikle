############################################################
# Name: Anna Bikle
# Name(s) of anyone worked with:
# Est time spent (hr): 30 mins
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600
w = WIDTH
h = HEIGHT

def draw_image():
    """ Creates a window and draws a student's creation"""
    # Creating the window
    gw = GWindow(w, h)

    # And now it is your turn! Add your code below! Make sure you meet all the requirements!

#Head
    big_circle= GOval(175,175, 240,240)
    big_circle.set_filled(True)
    big_circle.set_color("Orange")
    gw.add(big_circle)

#Whiskers
    #Left
    w_1=GLine(200,300,140,280)
    gw.add(w_1)
    w_2=GLine(200,320,140,340)
    gw.add(w_2)
    #Right
    w_3=GLine(380,300,420,280)
    gw.add(w_3)
    w_4=GLine(380,320,420,340)
    gw.add(w_4)

#Eyes
    l_eye=GOval(230,250,20,20)
    l_eye.set_filled(True)
    gw.add(l_eye)

    r_eye=GOval(330,250,20,20)
    r_eye.set_filled(True)
    gw.add(r_eye)

#Nose
    nose=GRect(280,300,15,10)
    nose.set_filled(True)
    nose.set_color("Pink")
    gw.add(nose)

#Ears
    l_ear=GRect(190,190,50,50)
    l_ear.set_filled(True)
    l_ear.set_color("Orange")
    gw.add(l_ear)

    r_ear=GRect(350,190,50,50)
    r_ear.set_filled(True)
    r_ear.set_color("Orange")
    gw.add(r_ear)

#Label
    meow=GLabel("Meow",430,310)
    gw.add(meow)


if __name__ == '__main__':
    draw_image()
