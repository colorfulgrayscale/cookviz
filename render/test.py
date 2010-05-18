import math
import cairo

WIDTH, HEIGHT = 400, 400
    
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

context.set_source_rgb(255,255,255)

context.set_line_width(2)

context.set_source_rgb(0,0,0)

context.rectangle(0, 0, 400, 400)
context.stroke()

context.rectangle(50, 50, 300, 300)
context.stroke()

context.move_to( 125, 225 )
context.line_to( 275, 225 )
context.line_to( 200, 125 )
context.line_to( 125, 225 )
context.line_to( 200, 325 )
context.line_to( 275, 225 )
context.stroke()

if __name__ == "__main__":
    import os
    surface.write_to_png("test.png")
    os.system("test.png")
