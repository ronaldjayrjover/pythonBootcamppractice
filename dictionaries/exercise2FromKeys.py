'''
Use dict.fromkeys to generate a new dictionary using the provided game_properties list. Initialize all values to 0
Same the result in a variable cales initial_game_state


'''

#DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives",
                   "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills",
                   "enemy_kill_streaks", "minutes_played", "notifications", "achievements"
]

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
value = 0
initial_game_state = dict.fromkeys(game_properties, value)
print(initial_game_state)

###or####
initial_game_state = dict.fromkeys(game_properties, 0)
print(initial_game_state)