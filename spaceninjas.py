from SpaceNinjaSystems import *
import time
start = time.clock()

#number of fights to simulate
numTrials = 10000

#array containing each of the styles/etc to be faced off
SpaceNinjaArray = [SpaceNinja(3,0,0,20,0,'you'),
                   SpaceNinja(3,0,0,20,0,'him')]

#2d array of win chances, eg pos 1 vs pos 1, pos 1 vs pos 2, pos 2 vs pos 1, pos 2 vs pos 2......to fit the nuber of entries above
NinjaWinChances = [[0 for j in range(len(SpaceNinjaArray))] for i in range(len(SpaceNinjaArray))]
for i in range(len(SpaceNinjaArray)):
    for j in range(len(SpaceNinjaArray)):
        for k in range(numTrials): #for large numTrials this could take a while, because
            SpaceNinjaOne = copy.deepcopy(SpaceNinjaArray[i])
            SpaceNinjaTwo = copy.deepcopy(SpaceNinjaArray[j])
            result = fight(SpaceNinjaOne,SpaceNinjaTwo) #here is where the two space ninjas actually fight
            if result == 1:
                NinjaWinChances[i][j] += 1


end = time.clock()
#purely decrative begins now, if you like formatting, for all means, fix this shitstorm

#top row is the chance that the first spaceNinja will beat each other ninja starting with itself
print('Chances a style(y axis) has of defeating another(x axis)')

print('hp/att/def',)
for i in range(len(SpaceNinjaArray)): #puts the style names across the top
    s = str(SpaceNinjaArray[i].styleName)
    print('{0:<10}'.format(s),)
print()

for i in range(len(NinjaWinChances)):
    s = str(SpaceNinjaArray[i].styleName)
    print('{0:<10}'.format(s),) #starts with the style name
    for j in range(len(NinjaWinChances)):
          print('{0:<10}'.format(str(NinjaWinChances[i][j])),) #then adds all the results for that style(TODO: make percentage)
    print()

print(end - start)























