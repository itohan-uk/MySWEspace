import random
import tkinter as tk  
from playsound import playsound

WIDTH = 500
HEIGHT = 250
TITLE = "Rock Paper Scissors Game"
BUTTON_CLICK_SOUND = "clicks.m4a"

class RPS:
    player_score = 0
    machine_score = 0

    def __init__(self):
        self.rps_options = ["rock", "paper", "scissors"]
        self.window = tk.Tk()
        self.window.geometry("{}x{}".format(WIDTH, HEIGHT) )
        self.window.configure(bg="#dfeaf4")
        self.window.title(TITLE)
        self.text = tk.Text(master = self.window, height = 15, width = 40, bg = "#FFE4E1")
        self.text.grid(column=1,row=4)
        self.buttons()

        return

    def computer_choice(self):
        # Select random choice from possibilities
        return random.choice(self.rps_options) 

    def get_winner(self, player_choice, machine_choice):

        player_wins = "Yay!!! you WON"
        machine_wins = "Sorry you lost :("
        tie = "Its a TIE!!! Try again"

        # If both choices are the same, its a time
        if player_choice == machine_choice:
            print (tie)
            winner_statement = tie
 
        # Cases which the player wins
        elif player_choice == self.rps_options[0] and machine_choice == self.rps_options[2] or \
            player_choice == self.rps_options[1] and machine_choice == self.rps_options[0] or \
            player_choice == self.rps_options[2] and machine_choice == self.rps_options[1]:
            print (player_wins)
            winner_statement = player_wins
            self.player_score += 1

        # If all the conditions for player to win are false, computer wins
        else:
            print (machine_wins)
            winner_statement = machine_wins
            self.machine_score += 1

        
        result = "Your Choice: {} \n\nMachines's Choice :{}\n\n{}\n\nYour Score :{}\n\nComputer Score :{} ".format(player_choice,
        machine_choice, winner_statement, self.player_score, self.machine_score)  
        self.text.delete("1.0", tk.END)  
        self.text.insert(tk.END, result)
       
        return

    # Functions to handle different button click options
    def rock(self):
        playsound(BUTTON_CLICK_SOUND)
        player_choice = self.rps_options[0]
        machine_choice = self.computer_choice()
        self.get_winner(player_choice, machine_choice)

        return
    
    def paper(self):
        playsound(BUTTON_CLICK_SOUND)
        player_choice = self.rps_options[1]
        machine_choice = self.computer_choice()
        self.get_winner(player_choice, machine_choice)

        return

    def scissor(self):
        playsound(BUTTON_CLICK_SOUND)
        player_choice = self.rps_options[2]
        machine_choice = self.computer_choice() 
        self.get_winner(player_choice, machine_choice)    

        return

    # Function to create buttons and use the above commands
    def buttons(self):
        button1 = tk.Button(text="Rock" , width = 9, highlightbackground = "#8B3C9D", command = self.rock)
        button1.grid(column= 0,row=0, padx=10, pady=10)
        button2 = tk.Button(text="Paper", width = 9, highlightbackground = "#FF4105", command = self.paper)
        button2.grid(column=1,row=0, padx=10, pady=10)
        button3 = tk.Button(text="Scissor", width = 9, highlightbackground = "#FEA636", command = self.scissor)
        button3.grid(column=2,row=0, padx=10, pady=10) 


        return

    # Function to run the app
    def run_app(self):
        self.window.mainloop()
        return
    

# Create App and run the app
if __name__ == "__main__":
    rps_app = RPS()
    rps_app.run_app()
