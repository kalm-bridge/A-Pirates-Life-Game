import pygame as pyg


class Element:
    def __init__(self, _variables):
        self.type = _variables[0]
        self.x, self.y = _variables[1]
        return


class Image(Element):
    def __init__(self, _variables):
        Element.__init__(self, _variables)
        self.pic = pyg.image.load(_variables[2])
        self.width, self.height = _variables[3]
        return

    def draw(self, win):
        win.blit(self.pic, (self.x, self.y))
        pyg.display.update()
        return

    def collides(self, x_pos, y_pos):
        if (x_pos > self.x and x_pos < (self.x + self.width)) and\
                (y_pos > self.y and y_pos < (self.y + self.height)):
            return True
        else:
            return False


class Rect(Element):
    def __init__(self, _variables):
        Element.__init__(self, _variables)
        self.height, self.width = _variables[2]
        self.color = _variables[3]
        self.rec = 0
        return

    def draw(self, win):
        pyg.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pyg.display.update()
        return


class TextBox(Element):
    def __init__(self, _variables):
        Element.__init__(self, _variables)
        self.rect = Rect(_variables)
        self.text = _variables[4]
        self.font, self.font_color = _variables[5]
        return

    def draw(self, win):
        self.rect.draw(win)
        text_surface = self.font.render(self.text, False, self.font_color)
        win.blit(text_surface, (self.x + 5, self.y + 10))
        return

