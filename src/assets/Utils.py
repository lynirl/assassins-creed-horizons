#Passer un temps en nombre de frame et le niveau de difficulté de 1 à 10
import math
def getFramerateForLevel(base_framerate, level):
    if base_framerate <= 0 or (1 > level or level > 10):
        raise ValueError
    
    #nbr de frames
    # return (math.pow(1.5, level) / math.pow(1.5, 10)) * base_framerate
    return ((level + base_framerate) / (10 + base_framerate)) * 60
    
