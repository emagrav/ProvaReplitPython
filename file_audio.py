import pygame
import time

print("***********FILE AUDIO**********")

pygame.init()
pygame.mixer.music.load("Files/trapano.mp3")
pygame.mixer.music.play()

time.sleep(10)
print("fatto!")
