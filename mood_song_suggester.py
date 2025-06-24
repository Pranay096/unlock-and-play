import tkinter as tk
import webbrowser
import random

# ========== Face Unlock (mock) ==========
# def face_unlocked():
#     # Replace with your real OpenCV logic
#     return True

# ========== Mood to Songs ==========
songs_by_mood = {
    "Happy": [
        "https://www.youtube.com/watch?v=ZbZSe6N_BXs",  # Pharrell - Happy
        "https://www.youtube.com/watch?v=9bZkp7q19f0",  # Gangnam Style
    ],
    "Sad": [
        "https://www.youtube.com/watch?v=RgKAFK5djSk",  # See You Again
        "https://www.youtube.com/watch?v=YQHsXMglC9A",  # Adele - Hello
    ],
    "Energetic": [
        "https://www.youtube.com/watch?v=fLexgOxsZu0",  # Uptown Funk
        "https://www.youtube.com/watch?v=KQ6zr6kCPj8",  # Party Rock Anthem
    ],
    "Chill": [
        "https://www.youtube.com/watch?v=hTWKbfoikeg",  # Nirvana - Come As You Are
        "https://www.youtube.com/watch?v=2Vv-BfVoq4g",  # Perfect - Ed Sheeran
    ]
}

# ========== Suggest Song ==========
def suggest_song(mood):
    song = random.choice(songs_by_mood[mood])
    webbrowser.open(song)

# ========== GUI ==========
def open_song_suggester():
    root = tk.Tk()
    root.title("🎵 Mood-Based Song Suggester")
    root.geometry("300x300")

    tk.Label(root, text="Select Your Mood:", font=("Arial", 16)).pack(pady=20)

    moods = ["Happy", "Sad", "Energetic", "Chill"]
    for mood in moods:
        tk.Button(root, text=mood, width=20, command=lambda m=mood: suggest_song(m)).pack(pady=5)

    root.mainloop()

# # ========== Run ==========
# if __name__ == "__main__":
#     if face_unlocked():
#         open_song_suggester()
#     else:
#         print("Face not recognized. Access Denied.")

if __name__ == "__main__":
    open_song_suggester()