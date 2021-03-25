import pygame
import time

class Display_graph:

    color_red = (255, 0, 0)
    color_blue = (0, 255, 0)
    color_green = (0, 0, 255)
    color_black = (0, 0, 0)
    color_white = (255, 255, 255)

    def __init__(self, title, width, height, pause_t, swap_t):
        self.resetInd()
        pygame.init()
        window_resolution = (width, height)
        self.width = width
        self.height = height
        self.pause_time = pause_t
        self.swap_time = swap_t

        pygame.display.set_caption(title)
        self.window_surface = pygame.display.set_mode(window_resolution)

    def drawGraph(self, l, forSwap=False):
        n = len(l)
        recWidth = self.width / n
        ratioHeigt = self.height / max(l)
        self.window_surface.fill(self.color_white)

        indx = 0
        for i in range(n):
            if i in  self.swapInd:
                myColor = self.color_blue
            else:
                myColor = self.color_green
            pygame.draw.rect(self.window_surface, myColor, pygame.Rect(indx, self.height, recWidth, -l[i] * ratioHeigt))
            indx += recWidth

        pygame.display.flip()
        if forSwap:
            time.sleep(self.swap_time)
        else:
            time.sleep(self.pause_time)

    def displaySwap(self, l, ind1, ind2):
        if ind1 != ind2:
            self.setSwapInd([ind1,ind2])
            self.drawGraph(l, True)
            l[ind1], l[ind2] = l[ind2], l[ind1]
            self.drawGraph(l, True)
        self.resetInd()
        self.drawGraph(l)

    def resetInd(self):
        self.swapInd = []

    def setSwapInd(self, indS):
        self.swapInd = indS

    def waitQuit(self):
        launched = True
        while launched:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False
