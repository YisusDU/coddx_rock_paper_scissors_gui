"""
Rock Paper Scissors GUI game using Tkinter
"""
import tkinter as tk
from tkinter import messagebox
import random
import json
import os


class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x450")
        self.root.config(bg="#f0f0f0")
        
        # Initialize scores
        self.player_score = 0
        self.computer_score = 0
        self.player_wins = 0
        self.computer_wins = 0
        self.ties = 0
        self.scoreboard_file = os.path.join(os.path.dirname(__file__), "scoreboard.json")
        self.load_scoreboard()
        
        # Title
        title = tk.Label(
            root, 
            text="Rock Paper Scissors", 
            font=("Arial", 24, "bold"),
            bg="#f0f0f0"
        )
        title.pack(pady=20)
        
        # Score display
        self.score_label = tk.Label(
            root,
            text=f"You: {self.player_score}  |  Computer: {self.computer_score}",
            font=("Arial", 14),
            bg="#f0f0f0"
        )
        self.score_label.pack(pady=10)
        
        # Result display
        self.result_label = tk.Label(
            root,
            text="Make your choice!",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#333"
        )
        self.result_label.pack(pady=10)
        
        # Choice display
        self.choice_label = tk.Label(
            root,
            text="",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#666"
        )
        self.choice_label.pack(pady=5)
        
        # Button frame
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        # Buttons for choices
        self.rock_btn = tk.Button(
            button_frame,
            text="🪨 Rock",
            font=("Arial", 12, "bold"),
            width=10,
            bg="#4CAF50",
            fg="white",
            command=lambda: self.play("rock"),
            padx=10,
            pady=10
        )
        self.rock_btn.pack(side=tk.LEFT, padx=5)
        
        self.paper_btn = tk.Button(
            button_frame,
            text="📄 Paper",
            font=("Arial", 12, "bold"),
            width=10,
            bg="#2196F3",
            fg="white",
            command=lambda: self.play("paper"),
            padx=10,
            pady=10
        )
        self.paper_btn.pack(side=tk.LEFT, padx=5)
        
        self.scissors_btn = tk.Button(
            button_frame,
            text="✂️ Scissors",
            font=("Arial", 12, "bold"),
            width=10,
            bg="#FF9800",
            fg="white",
            command=lambda: self.play("scissors"),
            padx=10,
            pady=10
        )
        self.scissors_btn.pack(side=tk.LEFT, padx=5)
        
        # Reset button
        reset_btn = tk.Button(
            root,
            text="Reset Score",
            font=("Arial", 10),
            bg="#f44336",
            fg="white",
            command=self.reset_score,
            padx=20,
            pady=8
        )
        reset_btn.pack(pady=10)
        
        # Scoreboard button
        scoreboard_btn = tk.Button(
            root,
            text="View Scoreboard",
            font=("Arial", 10),
            bg="#00BCD4",
            fg="white",
            command=self.show_scoreboard,
            padx=20,
            pady=8
        )
        scoreboard_btn.pack(pady=5)
    
    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])
    
    def determine_winner(self, player, computer):
        if player == computer:
            return 'tie'
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissors' and computer == 'paper'):
            return 'player'
        else:
            return 'computer'
    
    def play(self, player_choice):
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(player_choice, computer_choice)
        
        # Update scores
        if winner == 'player':
            self.player_score += 1
            self.player_wins += 1
            result_text = "🎉 You win this round!"
            result_color = "#4CAF50"
        elif winner == 'computer':
            self.computer_score += 1
            self.computer_wins += 1
            result_text = "💻 Computer wins this round!"
            result_color = "#f44336"
        else:
            self.ties += 1
            result_text = "🤝 It's a tie!"
            result_color = "#FF9800"
        
        # Update labels
        self.result_label.config(text=result_text, fg=result_color)
        self.choice_label.config(
            text=f"You chose: {player_choice}  |  Computer chose: {computer_choice}"
        )
        self.score_label.config(
            text=f"You: {self.player_score}  |  Computer: {self.computer_score}"
        )
        
        # Save scoreboard
        self.save_scoreboard()
    
    def reset_score(self):
        self.player_score = 0
        self.computer_score = 0
        self.score_label.config(
            text=f"You: {self.player_score}  |  Computer: {self.computer_score}"
        )
        self.result_label.config(text="Score reset! Make your choice!", fg="#333")
        self.choice_label.config(text="")
    
    def load_scoreboard(self):
        if os.path.exists(self.scoreboard_file):
            try:
                with open(self.scoreboard_file, 'r') as f:
                    data = json.load(f)
                    self.player_wins = data.get('player_wins', 0)
                    self.computer_wins = data.get('computer_wins', 0)
                    self.ties = data.get('ties', 0)
            except:
                self.player_wins = 0
                self.computer_wins = 0
                self.ties = 0
    
    def save_scoreboard(self):
        data = {
            'player_wins': self.player_wins,
            'computer_wins': self.computer_wins,
            'ties': self.ties
        }
        with open(self.scoreboard_file, 'w') as f:
            json.dump(data, f)
    
    def show_scoreboard(self):
        scoreboard_window = tk.Toplevel(self.root)
        scoreboard_window.title("Detailed Scoreboard")
        scoreboard_window.geometry("350x450")
        scoreboard_window.config(bg="#f0f0f0")
        
        title = tk.Label(
            scoreboard_window,
            text="📊 Detailed Scoreboard",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0"
        )
        title.pack(pady=20)
        
        # Current session stats
        session_frame = tk.Frame(scoreboard_window, bg="#e3f2fd", highlightthickness=1, highlightbackground="#2196F3")
        session_frame.pack(pady=10, padx=20, fill=tk.BOTH)
        
        session_title = tk.Label(
            session_frame,
            text="Current Session",
            font=("Arial", 12, "bold"),
            bg="#e3f2fd",
            fg="#1976D2"
        )
        session_title.pack(pady=8)
        
        session_stats = [
            f"Your Wins: {self.player_score}",
            f"Computer Wins: {self.computer_score}",
        ]
        for stat in session_stats:
            stat_label = tk.Label(
                session_frame,
                text=stat,
                font=("Arial", 11),
                bg="#e3f2fd",
                fg="#333"
            )
            stat_label.pack(pady=4)
        
        # Overall stats
        overall_frame = tk.Frame(scoreboard_window, bg="#f3e5f5", highlightthickness=1, highlightbackground="#9C27B0")
        overall_frame.pack(pady=10, padx=20, fill=tk.BOTH)
        
        overall_title = tk.Label(
            overall_frame,
            text="Overall Stats (All-Time)",
            font=("Arial", 12, "bold"),
            bg="#f3e5f5",
            fg="#6A1B9A"
        )
        overall_title.pack(pady=8)
        
        total_games = self.player_wins + self.computer_wins + self.ties
        win_rate = (self.player_wins / total_games * 100) if total_games > 0 else 0
        
        overall_stats = [
            f"Your Wins: {self.player_wins}",
            f"Computer Wins: {self.computer_wins}",
            f"Ties: {self.ties}",
            f"Total Games: {total_games}",
            f"Win Rate: {win_rate:.1f}%"
        ]
        for stat in overall_stats:
            stat_label = tk.Label(
                overall_frame,
                text=stat,
                font=("Arial", 11),
                bg="#f3e5f5",
                fg="#333"
            )
            stat_label.pack(pady=4)
        
        # Reset all stats button
        reset_all_btn = tk.Button(
            scoreboard_window,
            text="Reset All Stats",
            font=("Arial", 10),
            bg="#f44336",
            fg="white",
            command=self.reset_all_stats,
            padx=20,
            pady=8
        )
        reset_all_btn.pack(pady=15)
    
    def reset_all_stats(self):
        if messagebox.askyesno("Confirm", "Reset all-time stats? This cannot be undone."):
            self.player_wins = 0
            self.computer_wins = 0
            self.ties = 0
            self.save_scoreboard()
            messagebox.showinfo("Success", "All stats have been reset!")

            
if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()