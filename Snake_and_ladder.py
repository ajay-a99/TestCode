import random

class Dice:

    def create_num(self):
        roll_dice = random.randrange(1,7)
        return roll_dice

class Player1(Dice):

    def __init__(self,player_name):
        self.player_name = player_name
        self.pos = 0

    def SetPos(self,position):
        self.pos = position

    def GetPos(self):
        return self.pos

    def GetPlayerName(self):
        return self.player_name
    
class UpdatePosition(Player1):

    def __init__(self,current_pos,dice):
        self.dice = dice
        self.update_pos = current_pos
    
    def move(self):
        class_obj = Player1(self.dice)
        updated_pos =  self.update_pos + self.dice
        return updated_pos
    
def run():
    p1 = Player1('Ajay')
    
    def bite_or_lift(position):
        snake_list = [9,12,17,19]
        ladder_list = [2,5,8,15]
        if position in snake_list:
            print('!!!!!Bit by the snake!!!!!!')
            if position==9:
                position=3
            elif position==12:
                position=6
            elif position==17:
                position=10
            elif position==19:
                position=7

        if position in ladder_list:
            if position in ladder_list:
                print('.....Lifted by the Ladder......')
                if position==2:
                    position=16
                elif position==5:
                    position=14
                elif position==8:
                    position=11
                elif position==15:
                    position=18
        return position

    def player_details():
        current_pos = p1.GetPos()
        print(current_pos,'<----current pos of player')
        input('Press enter to roll the dice.....')
        dice = Dice()
        mov_player = dice.create_num()
        print(mov_player,'<----dice')
        play = UpdatePosition(current_pos,mov_player)
        updated_position = play.move()
        current_position = bite_or_lift(updated_position)
        p1.SetPos(current_position)
        print(p1.GetPos(),'<--- After dice roll')
        if p1.GetPos()>20:
            print('Give it another try..{0}'.format(p1.GetPos()))
            
    while (p1.GetPos()<=20):
        player_details()
        if p1.GetPos() == 20:
            print('You won...!!!!')
        
run()
