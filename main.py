import numpy as np
from scipy.io.wavfile import write
from scipy import signal
import sounddevice as sd
import time
import pygame
from pygame.locals import *
import asyncio
import threading


pygame.init()

def play_sin_wae(freq,a,sps,duration):
    samples = np.arange(sps * duration)
    sine_wave = (np.sin(2 * np.pi * freq * samples / sps))*a
    sine_wave_int = np.int16(sine_wave * 32767)
    sd.play(sine_wave_int, sps)
    # sd.play(sine_wave_int * 0.03, sps)
def play_cos_wae(freq,a,sps,duration):
    samples = np.arange(sps * duration)
    cos_wave = np.cos(2 * np.pi * freq * samples / sps) * a
    cos_wave_int = np.int16(cos_wave * 32767)
    sd.play(cos_wave_int, sps)
    
def play_sq_wae(freq,a,sps,duration):
    samples = np.arange(0,duration,1/sps)
    print(samples)
    wave =  (np.sin(2 * np.pi * freq/2 * samples) +np.sin(2 * np.pi * (freq*10) * samples/sps))*np.sin( 2*np.pi*freq/2 * samples )
    # wave = (signal.square(0.5 * np.pi * freq * samples)+np.cos(5 * np.pi * freq * (samples*0.5)) +(np.sin(0.5 * np.pi * freq* samples )))
    # wave = a*(np.sin( np.pi * (freq) * samples ))
    sd.play(wave, sps)

def display(str):
    text = font.render(str, True, (255, 255, 255), (159, 182, 205))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery

    screen.blit(text, textRect)
    pygame.display.update()


screen = pygame.display.set_mode( (640,480) )
pygame.display.set_caption('Python numbers')
screen.fill((159, 182, 205))

font = pygame.font.Font(None, 17)
duration = 1
a=1
x=True
k = pygame.key.get_pressed()
while not k[K_ESCAPE] and x:
    pygame.time.delay(100)
    th= threading.Thread()
    sps =44100
    event=pygame.event.wait()
    display('a='+str(a)+', duration='+str(duration))
    if event.type==pygame.KEYDOWN:
        if event.key== pygame.K_ESCAPE:
            x = False
        if event.key== pygame.K_UP:
            a += 0.1

        if event.key== pygame.K_DOWN:
            if a > 0:
                a -= 0.1

        if event.key== pygame.K_q:

            play_sq_wae(1050, a, sps, duration)
        if event.key== pygame.K_2:

            play_sq_wae(1100, a, sps, duration)
        if event.key== pygame.K_w:

            play_sq_wae(1150, a, sps, duration)
        if event.key== pygame.K_3:

            play_sq_wae(1200, a, sps, duration)
        if event.key== pygame.K_e:
            play_sq_wae(1300, a, sps, duration)
        if event.key== pygame.K_r:

            play_sq_wae(1400, a, sps, duration)
        if event.key== pygame.K_5:

            play_sq_wae(1475, a, sps, duration)
        if event.key== pygame.K_t:

            play_sq_wae(1550, a, sps, duration)
        if event.key== pygame.K_6:

            play_sq_wae(1650, a, sps, duration)
        if event.key== pygame.K_y:

            play_sq_wae(1775, a, sps, duration)
        if event.key== pygame.K_7:

            play_sq_wae(1850, a, sps, duration)
        if event.key== pygame.K_u:

            play_sq_wae(1950, a, sps, duration)
        if event.key== pygame.K_i:

            play_sq_wae(2100, a, sps, duration)


sd.stop()
