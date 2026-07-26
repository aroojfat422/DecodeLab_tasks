import tkinter as tk
from tkinter import ttk, messagebox

# Recommendation Data
recommendations = {
    "Action": [
        "John Wick",
        "Mission Impossible",
        "Mad Max: Fury Road",
        "Extraction",
        "The Dark Knight"
    ],
    "Comedy": [
        "Mr. Bean",
        "The Mask",
        "Free Guy",
        "Jumanji",
        "Central Intelligence"
    ],
    "Horror": [
        "The Conjuring",
        "Insidious",
        "Annabelle",
        "Smile",
        "The Nun"
    ],
    "Science Fiction": [
        "Interstellar",
        "Inception",
        "The Matrix",
        "Avatar",
        "Dune"
    ],
    "Romance": [
        "Titanic",
        "The Notebook",
        "Me Before You",
        "La La Land",
        "A Walk to Remember"
    ],
    "Adventure": [
        "Pirates of the Caribbean",
        "Jungle Cruise",
        "The Hobbit",
        "King Kong",
        "Uncharted"
    ],
    "Animation": [
        "Frozen",
        "Moana",
        "Toy Story",
        "Finding Nemo",
        "Coco"
    ],
    "Fantasy": [
        "Harry Potter",
        "The Lord of the Rings",
        "Doctor Strange",
        "Fantastic Beasts",
        "Percy Jackson"
    ]
}

# Function
def recommend():
    category = combo.get()

    if category == "":
        messagebox.showwarning("Warning", "Please select a category.")
        return

    output.delete("1.0", tk.END)
    output.insert(tk.END, f"Top Recommendations for {category}\n\n")

    for movie in recommendations[category]:
        output.insert(tk.END, "🎬 " + movie + "\n")


# Window
root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("600x500")
root.configure(bg="#2C3E50")

# Heading
title = tk.Label(
    root,
    text="🎥 Movie Recommendation System",
    font=("Arial", 20, "bold"),
    bg="#2C3E50",
    fg="white"
)
title.pack(pady=15)

# Label
label = tk.Label(
    root,
    text="Select Your Favorite Category",
    font=("Arial", 13),
    bg="#2C3E50",
    fg="white"
)
label.pack()

# Dropdown
combo = ttk.Combobox(
    root,
    values=list(recommendations.keys()),
    font=("Arial", 12),
    width=30
)
combo.pack(pady=10)

# Button
btn = tk.Button(
    root,
    text="Show Recommendations",
    font=("Arial", 12, "bold"),
    bg="#27AE60",
    fg="white",
    command=recommend
)
btn.pack(pady=10)

# Output Box

output = tk.Text(
    root,
    width=50,
    height=15,
    font=("Arial", 11)
)
output.pack(pady=10)

root.mainloop()

