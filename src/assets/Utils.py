#Passer un temps en nombre de frame et le niveau de difficulté de 1 à 10
import math
import pygame    
def getMaxTimeForLevel(timeLvlZero, level):
    if timeLvlZero <= 0 or 1 > level :
        raise ValueError
    
    #nbr de frames
    # return (math.pow(1.5, level) / math.pow(1.5, 10)) * base_framerate
    result = (-0.9 * level) + timeLvlZero
    if (result < 1):
        return 1
    return result

def play_sound_effect(sound_effect):
    effect_channel = pygame.mixer.find_channel(True)
    if effect_channel:
        effect_channel.play(sound_effect)