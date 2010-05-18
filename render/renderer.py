import math, os
import cairo

class Renderer():
    def __init__(self, surface = None):
        self.WIDTH = 400
        self.HEIGHT = 400
        if surface is not None:
            self.WIDTH = surface.get_width()
            self.HEIGHT = surface.get_height()
            return
        self.surface = surface
        self.setup()

    def setup(self):
        if self.surface is None:
            self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.WIDTH, self.HEIGHT)
        self.context = cairo.Context(self.surface)

    def arrowPath(self, rectStartX, rectStartY, bredth = 40, length = 160):
        self.context.move_to(rectStartX, rectStartY)
        self.context.line_to(rectStartX + length, rectStartY)
        self.context.line_to(rectStartX + length * 1.1, rectStartY + (bredth/2))
        self.context.line_to(rectStartX + length, rectStartY + bredth)
        self.context.line_to(rectStartX, rectStartY+bredth)
        self.context.line_to(rectStartX, rectStartY)
        return self.context.copy_path()
    
    def writeToFile(self, filename):
        self.surface.write_to_png(filename)

if __name__ == "__main__":
    renderer = Renderer()
    renderer.arrowPath(50, 50)
    renderer.context.stroke()
    
    renderer.writeToFile('test.png')
    os.system('test.png')
