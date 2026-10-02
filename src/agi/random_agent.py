import arc_agi
import numpy as np
import os 
import random
import json
from dotenv import load_dotenv
from arcengine import GameState

load_dotenv()
api_key =  os.getenv("API_KEY")
arc = arc_agi.Arcade()
env = arc.make("ls20")

def suggest_action(obs):
    actions = obs.available_actions
    action = random.choice(actions)
    return action


final_report = {}
for i in range(50):
    observation = env.reset()
    num_changed = 0
    action = suggest_action(observation)
    actions_trajectory = []
    report = {}
    while observation.state == GameState.NOT_FINISHED:
        actions_trajectory.append(action)
        before = observation.frame[0].copy()
        observation = env.step(action)
        after = observation.frame[0].copy()
        changed = np.where(before != after)
        if len(changed) > num_changed:
             num_changed = len(changed) 
             action = action
        else:
            action = suggest_action(observation)

    report['final game state'] = observation.state
    report['actions trajectory'] = actions_trajectory
    report['num_actions'] = len(actions_trajectory)

    final_report[i] = report
 
    
with open("results/random_results.json",'w') as file:
    json.dump(final_report,file,indent=4)

max_actions = 0
min_actions = 1000
total_actions = 0
no_losses = 0
for i in range(len(final_report)):
    no_actions = final_report[i]["num_actions"]
    total_actions += no_actions
    if  no_actions > max_actions:
        max_actions = no_actions
    if no_actions < min_actions:
        min_actions = no_actions
    if final_report[i]["final game state"] != GameState.WIN:
         no_losses += 1

        
print("Longest Episode: ", max_actions)
print("Shortest Episode: ", min_actions)
print("Average Episode: ", total_actions/50)
print("Number of losses: ", no_losses)



















