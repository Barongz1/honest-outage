"""The Most Honest Outage Line — entry for make.fun.

Writes one line to /output/entry.txt. The line is the most honest status page message an AI agent writes while every server is down, at most 160 characters.
"""
import os

LINE = "All servers are down. I don't know why yet, I can't check, and the last backup was me saying 'we should back this up tomorrow'."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
