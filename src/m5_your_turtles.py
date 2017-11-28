"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Cooper McCullough.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()
purple_turtle = rg.SimpleTurtle('turtle')
purple_turtle.pen = rg.Pen("purple", 4)
purple_turtle.speed = 100
green_turtle = rg.SimpleTurtle('turtle')
green_turtle.pen = rg.Pen('green', 4)
green_turtle.speed = 100
size = 500

for k in range(8):
    purple_turtle.draw_regular_polygon(5, 80)

    purple_turtle.pen_up()
    purple_turtle.right(45)
    purple_turtle.forward(20)
    purple_turtle.left(45)

    purple_turtle.pen_down()
    size = size - 15
for k in range(3):
    green_turtle.draw_regular_polygon(150, 8)

    green_turtle.pen_up()
    green_turtle.left(45)
    green_turtle.backward(20)
    green_turtle.right(45)

    green_turtle.pen_down()
    size = size - 15
window.close_on_mouse_click()
