import tkinter as tk
from tkinter import ttk
import re
from tkinter import PhotoImage
import math

class LockForge:
    def __init__(self, root):
        self.root = root
        self.root.title("LockForge - Password Strength Analyzer")
        self.root.geometry("600x500")
        self.root.configure(bg="#1a1a1a")
        
        # Set minimum window size
        self.root.minsize(600, 500)
        
        # Configure styles
        style = ttk.Style()
        style.configure("Custom.TEntry", padding=10, fieldbackground="#2a2a2a", foreground="white")
        style.configure("Custom.TLabel", background="#1a1a1a", foreground="white", font=("Helvetica", 12))
        
        # Main title
        self.title_label = tk.Label(
            root,
            text="LockForge",
            font=("Helvetica", 24, "bold"),
            bg="#1a1a1a",
            fg="#00ff00"
        )
        self.title_label.pack(pady=20)
        
        # Subtitle
        self.subtitle_label = tk.Label(
            root,
            text="Advanced Password Strength Analyzer",
            font=("Helvetica", 14),
            bg="#1a1a1a",
            fg="#cccccc"
        )
        self.subtitle_label.pack(pady=5)
        
        # Password entry frame
        self.entry_frame = tk.Frame(root, bg="#1a1a1a")
        self.entry_frame.pack(pady=30)
        
        # Password entry
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(
            self.entry_frame,
            textvariable=self.password_var,
            font=("Helvetica", 12),
            bg="#2a2a2a",
            fg="white",
            show="●",
            width=30,
            bd=0,
            highlightthickness=1,
            highlightbackground="#00ff00",
            highlightcolor="#00ff00"
        )
        self.password_entry.pack(pady=10, ipady=8)
        self.password_var.trace('w', self.check_password)
        
        # Strength meter canvas
        self.canvas = tk.Canvas(
            root,
            width=400,
            height=20,
            bg="#2a2a2a",
            highlightthickness=0
        )
        self.canvas.pack(pady=20)
        
        # Strength percentage label
        self.strength_label = tk.Label(
            root,
            text="Password Strength: 0%",
            font=("Helvetica", 16, "bold"),
            bg="#1a1a1a",
            fg="#00ff00"
        )
        self.strength_label.pack(pady=10)
        
        # Criteria frame
        self.criteria_frame = tk.Frame(root, bg="#1a1a1a")
        self.criteria_frame.pack(pady=20)
        
        # Criteria labels
        self.criteria_labels = {}
        criteria = [
            "Length (min. 8 characters)",
            "Uppercase letters",
            "Lowercase letters",
            "Numbers",
            "Special characters"
        ]
        
        for criterion in criteria:
            label = tk.Label(
                self.criteria_frame,
                text="❌ " + criterion,
                font=("Helvetica", 10),
                bg="#1a1a1a",
                fg="#ff4444"
            )
            label.pack(pady=2)
            self.criteria_labels[criterion] = label

    def check_password(self, *args):
        password = self.password_var.get()
        strength = 0
        total_criteria = 5
        
        # Check criteria
        criteria_met = {
            "Length (min. 8 characters)": len(password) >= 8,
            "Uppercase letters": bool(re.search(r'[A-Z]', password)),
            "Lowercase letters": bool(re.search(r'[a-z]', password)),
            "Numbers": bool(re.search(r'[0-9]', password)),
            "Special characters": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        }
        
        # Update criteria labels and calculate strength
        for criterion, is_met in criteria_met.items():
            label = self.criteria_labels[criterion]
            if is_met:
                label.config(text="✓ " + criterion, fg="#00ff00")
                strength += 1
            else:
                label.config(text="❌ " + criterion, fg="#ff4444")
        
        # Calculate percentage
        percentage = (strength / total_criteria) * 100
        
        # Update strength meter
        self.canvas.delete("all")
        if percentage > 0:
            width = (percentage / 100) * 400
            color = self.get_color_for_percentage(percentage)
            self.canvas.create_rectangle(0, 0, width, 20, fill=color, outline="")
        
        # Update strength label
        self.strength_label.config(text=f"Password Strength: {int(percentage)}%")
        
    def get_color_for_percentage(self, percentage):
        if percentage < 20:
            return "#ff0000"  # Red
        elif percentage < 40:
            return "#ff4444"  # Light red
        elif percentage < 60:
            return "#ffa500"  # Orange
        elif percentage < 80:
            return "#ffff00"  # Yellow
        else:
            return "#00ff00"  # Green

if __name__ == "__main__":
    root = tk.Tk()
    app = LockForge(root)
    root.mainloop()