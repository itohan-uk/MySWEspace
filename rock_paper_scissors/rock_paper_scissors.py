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
    player_choice = ""
    machine_choice = ""
    winner_statement = ""

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
        return random.choice(self.rps_options) 

    def get_winner(self):
        #self.winner_statement = ""
        player_wins = "Yay!!! you WON"
        machine_wins = "Sorry you lost :("
        tie = "Its a TIE!!! Try again"

        if self.player_choice == self.machine_choice:
            print (tie)
            self.winner_statement = tie

        elif self.player_choice == self.rps_options[0] and self.machine_choice == self.rps_options[2] or \
            self.player_choice == self.rps_options[1] and self.machine_choice == self.rps_options[0] or \
            self.player_choice == self.rps_options[2] and self.machine_choice == self.rps_options[1]:
            print (player_wins)
            self.winner_statement = player_wins
            self.player_score += 1

        else:
            print (machine_wins)
            self.winner_statement = machine_wins
            self.machine_score += 1

        
        result = "Your Choice: {} \nMachines's Choice :{}\n{}\nYour Score :{}\nComputer Score :{} ".format(self.player_choice,
        self.machine_choice, self.winner_statement, self.player_score, self.machine_score)  
        self.text.delete("1.0", tk.END)  
        self.text.insert(tk.END, result)
       
        return

    def rock(self):
        playsound(BUTTON_CLICK_SOUND)
        self.player_choice = self.rps_options[0]
        self.machine_choice = self.computer_choice()
        self.get_winner()

        return
    
    def paper(self):
        playsound(BUTTON_CLICK_SOUND)
        self.player_choice = self.rps_options[1]
        self.machine_choice = self.computer_choice()
        self.get_winner()

        return

    def scissor(self):
        playsound(BUTTON_CLICK_SOUND)
        self.player_choice = self.rps_options[2]
        self.machine_choice = self.computer_choice() 
        self.get_winner()    

        return

    #MAChine the button kink for mac computers
    def buttons(self):
        button1 = tk.Button(text="       Rock       ", bd= "5", highlightbackground = "#8B3C9D", command = self.rock,
        relief = tk.SUNKEN)

        button1.grid(column= 0,row=0, padx=10, pady=10)
        
        
        button2 = tk.Button(text="       Paper      ", bd= "5", highlightbackground = "#FF4105", command = self.paper)
        button2.grid(column=1,row=0, padx=10, pady=10)
        button3 = tk.Button(text="      Scissor     ", bd= "5", highlightbackground = "#FEA636", command = self.scissor)
        button3.grid(column=2,row=0, padx=10, pady=10) 


        return

    def run_app(self):
        self.window.mainloop()

        return

    


if __name__ == "__main__":
    rps_app = RPS()
    rps_app.run_app()







