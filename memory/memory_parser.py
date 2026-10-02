import csv
import json

memory = {}
with open("memory/memory.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        action = int(row["action_taken"])
        magnitude = int(row["changes"])

        before = row["Current observations"]
        after = row["after"]

        # Create the action level if it doesn't exist
        if action not in memory:
            memory[action] = {}

        # Create the magnitude level if it doesn't exist
        if magnitude not in memory[action]:
            memory[action][magnitude] = []

        # Add this experience
        memory[action][magnitude].append({
            "before": before,
            "after": after
        })

with open("memory/sorted_memory.json","w")as file:
    json.dump(memory,file,indent=4)