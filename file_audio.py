print("***********FILE AUDIO**********")

import pygame
import time

pygame.init()
pygame.mixer.music.load("trapano.wav")
pygame.mixer.music.play()

time.sleep(10)
print("fatto!")