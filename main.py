import pygame
import time
import threading

# -----------------------------
# SETTINGS
# -----------------------------

SONG_FILE = "song.mp3"

# Format:
# (time_in_seconds, text_to_type)
#
# Replace these examples with your own timestamps and lyrics.
LYRICS = [
    (0.0, "First line goes here"),
    (3.5, "Second line goes here"),
    (7.2, "Third line goes here"),
    (11.0, "Fourth line goes here"),
]

# -----------------------------
# INITIALIZE
# -----------------------------

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(SONG_FILE)

# -----------------------------
# TYPEWRITER EFFECT
# -----------------------------

def type_text(text, duration):
    if not text:
        return

    delay = duration / len(text)

    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)

    print()


# -----------------------------
# MAIN PLAYER
# -----------------------------

def play_lyrics():
    pygame.mixer.music.play()

    start_time = time.perf_counter()

    for i, (timestamp, text) in enumerate(LYRICS):

        # Wait until the timestamp is reached
        while True:
            current_time = time.perf_counter() - start_time

            if current_time >= timestamp:
                break

            time.sleep(0.001)

        # Calculate how much time we have
        # before the next lyric appears.
        if i + 1 < len(LYRICS):
            next_timestamp = LYRICS[i + 1][0]
            duration = next_timestamp - timestamp
        else:
            duration = 3.0

        type_text(text, duration)

    # Wait for the song to finish
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


# -----------------------------
# START
# -----------------------------

print("Starting lyric player...")
print()

play_lyrics()

pygame.mixer.music.stop()
pygame.quit()
