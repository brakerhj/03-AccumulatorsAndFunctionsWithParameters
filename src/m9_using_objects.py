"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Haley Braker.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()
    center_point1 = rg.Point(200, 200)
    center_point2 = rg.Point(80, 60)
    circle1 = rg.Circle(center_point1, 90)
    circle2 = rg.Circle(center_point2, 50)
    circle1.fill_color = 'green'
    #circle2.blue
    circle2.attach_to(window)
    circle1.attach_to(window)
    window.render()
    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()
    circle_center = rg.Point(300, 170)
    circle = rg.Circle(circle_center, 40)
    corner1 = rg.Point(50,50)
    corner2 = rg.Point(100,100)
    rectangle = rg.Rectangle(corner1, corner2)
    rectangle.attach_to(window)
    circle.attach_to(window)
    circle.fill_color = 'blue'
    window.render()
    window.close_on_mouse_click()
    print("Outline Thickness: ", circle.outline_thickness)
    print("Fill Color: ", circle.fill_color)
    print("Center: ", circle_center)
    print("X-Coordinate: ", circle_center.x)
    print("Y-Coordinate: ", circle_center.y)
    print("Outline Thickness: ", rectangle.outline_thickness)
    print("Fill Color: ", rectangle.fill_color)
    print("Center: ", corner1, "and", corner2)
    print("X-Coordinate: ", corner1.x, "and", corner2.x)
    print("Y-Coordinate: ", corner1.y, "and", corner2.y)



def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # TODO: 4. Implement and test this function.
    window = rg.RoseWindow()
    line1 = rg.Line(rg.Point(50,50) , rg.Point(150,170))
    line2 = rg.Line(rg.Point(160,160) , rg.Point(50,200))
    line2.thickness = 8
    line2.get_midpoint()
    line1.attach_to(window)
    line2.attach_to(window)
    window.render()
    window.close_on_mouse_click()
    print("Midpoint: ")
    print("X-Coordinate: ", line2.get_midpoint().x)
    print("Y-Coordinate: ", line2.get_midpoint().y)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
