#Passer un temps en nombre de frame et le niveau de difficulté de 1 à 10
import math
def getTimeForLevel(tempLvl1, level):
    if tempLvl1 <= 0 or (0 > level or level < 10):
        raise ValueError
    
    #nbr de frames
    return abs(math.pow(level, -1) * tempLvl1)
    
