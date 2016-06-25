import random
import copy

class SpaceNinja:
    def __init__(self, hp, attack, defence, lowestCrit, initiative, styleName):
        self.hp = hp
        self.currHp = hp
        self.att = attack
        self.defence = defence
        self.crit = lowestCrit
        self.initiative = initiative
        self.styleName = styleName

    def resetHp(self):
        self.currHp = self.hp
    
    
#pass 2 SpaceNinjas, returns 0 for draw, 1 if the first wins, 2 if the 2nd wins, easy right?
def fight(First_SpaceNinja, Second_SpaceNinja):
    #so first ini some ninjas
    SpaceNinja_First = First_SpaceNinja
    SpaceNinja_Second = Second_SpaceNinja
    attackeris = 0
    #since attack/defence is a coin flipper-roo
    #coin flip(initiative)
    #winner goes first

    while 1==1:
        first_initiative = random.randint(1,20) + SpaceNinja_First.initiative
        second_initiaitve = random.randint(1,20) + SpaceNinja_Second.initiative
        if first_initiative != second_initiaitve:
            if first_initiative > second_initiaitve:
                SpaceNinja_Attacker = SpaceNinja_First
                SpaceNinja_Defender = SpaceNinja_Second
                attackeris = 1
            else:
                SpaceNinja_Attacker = SpaceNinja_Second
                SpaceNinja_Defender = SpaceNinja_First
                attackeris = 2
            break

    #then fight 'em

    while SpaceNinja_Attacker.currHp > 0 and SpaceNinja_Defender.currHp > 0:
        #attacker rolls to hit
        att_roll = random.randint(1,20)
        #check for crit
        if att_roll >= SpaceNinja_Attacker.crit:
            SpaceNinja_Defender.currHp -= 1
            
        att_roll += SpaceNinja_Attacker.att
        #defender rolls to block
        def_roll = random.randint(1,20)
        #check for crit
        if def_roll >= SpaceNinja_Defender.crit:
            SpaceNinja_Attacker.currHp -= 1
            
        def_roll += SpaceNinja_Defender.defence
        if att_roll > def_roll:
            SpaceNinja_Defender.currHp -= 1

        #break out if a kill as been made
        if SpaceNinja_Attacker.currHp <= 0 or SpaceNinja_Defender.currHp <= 0:
            break
        #defenders turn to fight back, this might get confusing

        #attacker rolls to hit
        att_roll = random.randint(1,20)
        #check for crit
        if att_roll >= SpaceNinja_Defender.crit:
            SpaceNinja_Attacker.currHp -= 1
            
        att_roll += SpaceNinja_Defender.att
        #defender rolls to block
        def_roll = random.randint(1,20)
        #check for crit
        if def_roll >= SpaceNinja_Attacker.crit:
            SpaceNinja_Defender.currHp -= 1
            
        def_roll += SpaceNinja_Attacker.defence
        if att_roll > def_roll:
            SpaceNinja_Attacker.currHp -= 1

    if SpaceNinja_Attacker.currHp <= 0:
        if SpaceNinja_Defender.currHp <= 0:
            #Draw
            return 0
        else:
            #Defender wins
            #return the position of the winner
            if attackeris == 1:
                return 2
            else:
                return 1
    else:
        #Attacker wins
        return attackeris

