import arc_agi
import numpy as np
import os 
import random
import csv
from dotenv import load_dotenv
from arcengine import GameState

load_dotenv()
api_key =  os.getenv("API_KEY")
arc = arc_agi.Arcade()
env = arc.make("ls20")

def suggest_action(obs):
    actions = obs.available_actions
    suggested_action = random.choice(actions)
    return suggested_action

def run_game():
    observation = env.reset()
    memory = []
    num_changed = 0
    act = suggest_action(observation)
    while observation.state == GameState.NOT_FINISHED:
        before = observation.frame[0].copy()
        observation = env.step(act)
        after = observation.frame[0].copy()
        changed = np.where(before != after)
        memory.append([before, act,after,changed[0].size,])
        print(changed[0])
        print(changed[0].size)
        if len(changed) > num_changed:
            num_changed = len(changed) 
            act = act
        else:
            act = suggest_action(observation)

    return memory #memory is a list of lists


run_game()
        

"""headers = ["Current observations","action_taken","after","changes"]
data = run_game()

with open('memory.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for i in range(10):
         data = run_game()
         writer.writerows(data)
"""
    

















