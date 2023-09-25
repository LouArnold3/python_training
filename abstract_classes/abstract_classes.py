import random
# A class that should not be instanciated
#Acts as a base / or super class 
#Contains common implentation details 

#Can have all methods >> abstract methods 

class AbstractGame:

    def start(self):
        while True:
            start = input("Would you like to play? ")
            if start.lower() == 'yes':
                break
        self.play()
    
    def end(self):
        print("The game has ended")
        self.reset()

    #Abstract methods should be implemented by ANY class that inherits the abstract class 

    def play(self):
        raise NotImplementedError("You must provide an implentation for play")
    
    def reset(self):
        raise NotImplementedError("You must provide an implentation for reset")
    

class RandomGuesser(AbstractGame):

    def __init__(self, rounds) -> None:
        self.rounds = rounds
        self.round = 0
        
    
    def reset(self):
 
        self.round = 0

    def play(self):
        
        while self.round < self.rounds:
            self.round += 1
            print(f"Welcome to round {self.round}")
            random_num = random.randint(0, 5)

            while True:
                guess = input("Enter a number between 1 and 5: ")
                if int(guess) == random_num:
                    print("You got it!")
                    break
        self.end()

number_of_rounds = input("How many rounds would you like to play? ")
game = RandomGuesser(int(number_of_rounds))

game.start()




       

    


    