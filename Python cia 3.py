#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import tkinter as tk

class Player:
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = int(skill_level)
        self.biometric_data = {}
        self.runs_scored = 0
        self.matches_played = 0
        self.balls_faced = 0
        self.average = 0
        self.strike_rate = 0

    def train(self, runs_scored, balls_faced, matches_played):
        try:
            skill_gain = random.uniform(0.1, 0.5)
            self.skill_level += skill_gain

            self.matches_played += int(matches_played)
            self.runs_scored += int(runs_scored)
            self.balls_faced += int(balls_faced)
            self.average = self.runs_scored / self.matches_played
            self.strike_rate = (self.runs_scored / self.balls_faced) * 100

            output_text.insert(tk.END, f"{self.name} has trained. New skill level: {self.skill_level}\n")
            output_text.insert(tk.END, f"Total runs scored: {self.runs_scored}, Average: {self.average}\n")
            output_text.insert(tk.END, f"Strike rate: {self.strike_rate}%\n")
        except Exception as e:
            print("An error occurred during training:", e)

    def collect_biometric_data(self, heart_rate, oxygen_level, flexibility, strength, weight, height):
        try:
            self.biometric_data = {"heart_rate": heart_rate, "oxygen_level": oxygen_level,
                                   "flexibility": flexibility, "strength": strength,
                                   "weight": weight, "height": height}
        except Exception as e:
            print("An error occurred while collecting biometric data:", e)

class TrainingSystem:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def train_players(self):
        try:
            for player in self.players:
                runs_scored = random.randint(0, 100)  # Generate a random number of runs scored
                balls_faced = random.randint(0, 100)  # Generate a random number of balls faced
                matches_played = random.randint(0, 20)  # Generate a random number of matches played
                player.train(runs_scored, balls_faced, matches_played)
        except Exception as e:
            print("An error occurred during training players:", e)

class BiometricAnalyzer:
    def analyze_data(self, player):
        try:
            if player.biometric_data:
                if int(player.biometric_data['heart_rate']) > 150:
                    output_text.insert(tk.END, f"{player.name} is fatigued. Rest recommended.\n")
                else:
                    output_text.insert(tk.END, f"{player.name} is ready for training or match.\n")
        except Exception as e:
            print("An error occurred during biometric data analysis:", e)

class VirtualAssistant:
    @staticmethod
    def provide_real_time_facts():
        try:
            facts = [
                "Did you know? The highest individual score in Test cricket is 400 not out, scored by Brian Lara.",
                "The fastest delivery in cricket history was bowled by Shoaib Akhtar at 161.3 km/h (100.23 mph).",
                "Sachin Tendulkar is the only player to have scored one hundred international centuries.",
                "Cricket is a bat-and-ball game played between two teams of eleven players.",
                "The batting side scores runs by striking the ball bowled at the wicket with the bat.",
                "The match is adjudicated by two umpires, aided by a third umpire and match referee in international matches.",
                "In professional cricket, the length of a game ranges from 20 overs of six bowling deliveries per side to Test cricket played over five days.",
                "The Laws of Cricket were established in England by the Marylebone Cricket Club (MCC) in 1788.",
                "Cricket is the second most popular sport in the world after football.",
                "A cricket field consists of a large grassy ground on which the game of cricket is played.",
                "Cricket has a number of formats including Test matches, One Day Internationals (ODIs), and Twenty20 (T20) matches.",
                "The wickets are made of wood and placed at each end of the pitch.",
                "Bowling is the action of propelling the ball toward the wicket defended by a batsman.",
                "Fielding is the action of fielders collecting the ball after it is struck by the batsman to limit the number of runs scored."
            ]
            return random.choice(facts)
        except Exception as e:
            print("An error occurred while providing facts:", e)

    @staticmethod
    def interact():
        try:
            fact = VirtualAssistant.provide_real_time_facts()
            output_text.insert(tk.END, "Here's an interesting cricket fact: {}\n".format(fact))
        except Exception as e:
            print("An error occurred during interaction:", e)

class HandCricketGame:
    @staticmethod
    def play_game(output_text, runs_chosen_entry):
        try:
            player_score = 0
            computer_score = random.randint(1, 6)
            while True:
                try:
                    player_input = int(runs_chosen_entry.get())
                    if player_input == 0:
                        break
                    elif 1 <= player_input <= 6:
                        computer_play = random.randint(1, 6)
                        if player_input != computer_play:
                            player_score += player_input
                            output_text.insert(tk.END, f"Computer played: {computer_play}, Your score: {player_score}\n")
                        else:
                            output_text.insert(tk.END, f"Computer played: {computer_play}. You're out!\n")
                            break
                    else:
                        output_text.insert(tk.END, "Invalid input! Please enter a number between 1 and 6.\n")
                except ValueError:
                    output_text.insert(tk.END, "Invalid input! Please enter a number.\n")
            output_text.insert(tk.END, f"Your final score: {player_score}. Computer's score: {computer_score}\n")
            if player_score > computer_score:
                output_text.insert(tk.END, "Congratulations! You won!\n")
            elif player_score < computer_score:
                output_text.insert(tk.END, "You lost! Better luck next time!\n")
            else:
                output_text.insert(tk.END, "It's a tie!\n")
        except Exception as e:
            print("An error occurred during the hand cricket game:", e)

def train_players():
    try:
        player_name = player_name_entry.get()
        player_skill_level = player_skill_level_entry.get()
        heart_rate = heart_rate_entry.get()
        oxygen_level = oxygen_level_entry.get()
        flexibility = flexibility_entry.get()
        strength = strength_entry.get()
        weight = weight_entry.get()
        height = height_entry.get()

        runs_scored = runs_scored_entry.get()
        balls_faced = balls_faced_entry.get()
        matches_played = matches_played_entry.get()

        player1 = Player(player_name, int(player_skill_level))
        player1.collect_biometric_data(heart_rate, oxygen_level, flexibility, strength, weight, height)

        training_system = TrainingSystem()
        training_system.add_player(player1)
        training_system.train_players()

        analyzer = BiometricAnalyzer()
        analyzer.analyze_data(player1)
    except Exception as e:
        print("An error occurred in the training process:", e)

def get_cricket_fact():
    try:
        VirtualAssistant.interact()
    except Exception as e:
        print("An error occurred while getting a cricket fact:", e)

def play_hand_cricket():
    try:
        HandCricketGame.play_game(output_text, runs_chosen_entry)
    except Exception as e:
        print("An error occurred while playing hand cricket:", e)

# GUI Setup
root = tk.Tk()
root.title("Cricket-Learn, Train, Play")

# Player Info
player_name_label = tk.Label(root, text="Player's Name:")
player_name_label.grid(row=0, column=0, sticky="e")
player_name_entry = tk.Entry(root)
player_name_entry.grid(row=0, column=1)

player_skill_level_label = tk.Label(root, text="Player's Skill Level (50-100):")
player_skill_level_label.grid(row=1, column=0, sticky="e")
player_skill_level_entry = tk.Entry(root)
player_skill_level_entry.grid(row=1, column=1)

# Biometric Data
heart_rate_label = tk.Label(root, text="Heart Rate:")
heart_rate_label.grid(row=2, column=0, sticky="e")
heart_rate_entry = tk.Entry(root)
heart_rate_entry.grid(row=2, column=1)

oxygen_level_label = tk.Label(root, text="Oxygen Level:")
oxygen_level_label.grid(row=3, column=0, sticky="e")
oxygen_level_entry = tk.Entry(root)
oxygen_level_entry.grid(row=3, column=1)

flexibility_label = tk.Label(root, text="Flexibility (60-100):")
flexibility_label.grid(row=4, column=0, sticky="e")
flexibility_entry = tk.Entry(root)
flexibility_entry.grid(row=4, column=1)

strength_label = tk.Label(root, text="Strength (50-100):")
strength_label.grid(row=5, column=0, sticky="e")
strength_entry = tk.Entry(root)
strength_entry.grid(row=5, column=1)

weight_label = tk.Label(root, text="Weight (50-100):")
weight_label.grid(row=6, column=0, sticky="e")
weight_entry = tk.Entry(root)
weight_entry.grid(row=6, column=1)

height_label = tk.Label(root, text="Height (150-200):")
height_label.grid(row=7, column=0, sticky="e")
height_entry = tk.Entry(root)
height_entry.grid(row=7, column=1)

# Runs, Balls Faced, Matches Played
runs_scored_label = tk.Label(root, text="Runs Scored:")
runs_scored_label.grid(row=8, column=0, sticky="e")
runs_scored_entry = tk.Entry(root)
runs_scored_entry.grid(row=8, column=1)

balls_faced_label = tk.Label(root, text="Balls Faced:")
balls_faced_label.grid(row=9, column=0, sticky="e")
balls_faced_entry = tk.Entry(root)
balls_faced_entry.grid(row=9, column=1)

matches_played_label = tk.Label(root, text="Matches Played:")
matches_played_label.grid(row=10, column=0, sticky="e")
matches_played_entry = tk.Entry(root)
matches_played_entry.grid(row=10, column=1)

# Runs Chosen for Hand Cricket
runs_chosen_label = tk.Label(root, text="Runs Chosen:")
runs_chosen_label.grid(row=11, column=0, sticky="e")
runs_chosen_entry = tk.Entry(root)
runs_chosen_entry.grid(row=11, column=1)

# Buttons
train_button = tk.Button(root, text="Train", command=train_players)
train_button.grid(row=12, column=0, columnspan=2, pady=10)

fact_button = tk.Button(root, text="Get Cricket Fact", command=get_cricket_fact)
fact_button.grid(row=13, column=0, columnspan=2, pady=10)

hand_cricket_button = tk.Button(root, text="Play Hand Cricket", command=play_hand_cricket)
hand_cricket_button.grid(row=14, column=0, columnspan=2, pady=10)

# Output Text
output_text = tk.Text(root, height=15, width=60)
output_text.grid(row=15, column=0, columnspan=2)

root.mainloop()


# In[ ]:





# In[ ]:




