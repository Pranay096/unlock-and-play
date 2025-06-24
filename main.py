import subprocess
import sys
from face_data import start_face_detection

if __name__ == "__main__":
    access = start_face_detection()
    if access:
        subprocess.Popen([sys.executable, "mood_song_suggester.py"])
