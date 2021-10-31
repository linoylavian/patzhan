import pygame
import random
import threading
import time
from function_sound_file import function_sound

global done
window_x = 300
window_y = 200

def performance():
    function_sound()

def getRandColor():
    colorR = random.randint(0,255)
    colorG = random.randint(0,255)
    colorB = random.randint(0,255)
    return (colorR ,colorG,colorB)


def leaveFlash(seconds):
    global done
    time.sleep(seconds)
    done = True

def main():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Rainbow!")
    clock = pygame.time.Clock()

    global done
    done = False
    counter = 0
    colour = getRandColor()

    threading.Thread(target=performance).start()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        threading.Thread(target=leaveFlash, args=(10,)).start()

        counter += 1
        if counter > 3:
            colour = getRandColor()
            counter = 0

        screen.fill(colour)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

