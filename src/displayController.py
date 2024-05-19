# Writing a driver to print the output of the listener function
# 

# Status flag that gets updated during the listener function

from multiprocessing import Queue
from .zmb2eng import listener

class DisplayController():
    def __init__(self):
        self.results_queue_zombie = Queue()
        self.communication_pipe_zombie = Queue()
        self.listener_zombie = listener(self.results_queue_zombie, self.communication_pipe_zombie)

        self.queue_toronto = Queue()
        self.listener_toronto = listener(self.queue_toronto)
        state = {
            "choice": None
        }

    def intro(self):
        print("The apocalypse is here. The zombies are coming. You are the last hope of humanity.")
        print("You, having perfect pitch have realized that zombies speak in musical grunts.")
        print("Interested in their language, you've created a translator in an attempt to communicate with them.")
        print("")
        print("Welcome, to Zombie Translator")
        print("")
    
    def start_prompt(self) -> str:
        print("Would you like to:")
        print("1. Decode Zombie into Toronto Slang")
        print("2. Encode Toronto Slang into Zombie")
        print("3. Quit")
        print("")
        print("Please enter a number: ")
        choice = input()
        state = {
            "choice": choice
        }
        return choice

    def zombie_to_toronto(self):
        print("You have selected to decode Zombie into Toronto Slang")
        print("Please start grunting into the microphone to begin decoding")
        print("Press any key to stop")
        print("")

        self.listener_zombie.start()
        self.listener_zombie.join()

        print("The sentence is: ", self.queue_zombie)
    
    def toronto_to_zombie(self):
        print("You have selected to encode Toronto Slang into Zombie")
        print("Please start speaking Toronto Slang into the microphone to begin encoding")
        print("Press any key to stop")
        print("")

        self.listener_toronto.start()
        while self.listener_toronto.is_alive():
            print(self.communication_pipe_zombie.get())

        print("The sentence is: ", self.queue_toronto)

    def main(self):
        print("in main")
        self.intro()
        while True:
            print("in main loop")
            choice = self.start_prompt()
            if choice == "1":
                self.zombie_to_toronto()
            elif choice == "2":
                self.toronto_to_zombie()
            elif choice == "3":
                self.quit()
            else:
                print("Invalid choice. Please try again.")
                continue
    
    def quit(self):
        print("Thank you for using Zombie Translator. Goodbye!")
        exit()
    
# if __name__ == "__main__":
print("hi")
display = DisplayController()
display.main()