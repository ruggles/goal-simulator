# Goal Simulator
# By Nicholas Ruggles

# Initial gamestate variables
START_TIME       = 6
START_STRESS     = 20
START_HUNGER     = 20
START_SLEEP      = 80
START_MOTIVATION = 80

# All actions are formatted (hunger, stress, sleep, motivation)
eat_action = (50, -10, -10, 0)
sleep_action = (-10, -10, 50, 0)
tv_action = (-10, -30, -10, 0)
piano_action = (-10, 40, -10, -30)

# action_dict associates each action name with list of modifiers
ACTION_DICT = {'eat'  : eat_action,
               'sleep': sleep_action,
               'piano': piano_action,
               'tv'   : tv_action}

# Simulation ends at 10 O'clock
END_TIME = 10

def main():
    
    run_game()
    
def run_game():

    day_state = game_state(START_TIME, START_HUNGER, START_STRESS, 
                           START_SLEEP, START_MOTIVATION)
    
    while True:
    
        print_state(day_state)

        if day_state.get_stats()[0] >= 10:
            return
        
        action = get_input(ACTION_DICT)
        
        if action != None:
            day_state.run_sim(action)
            
def get_input(action_dict):
    """
    If the player types in a valid action, return action.
    else, return None.
    """
    
    player_input = raw_input("Please choose an action >")
    
    action_names = action_dict.keys()
    
    if player_input in action_names:
        return action_dict[player_input]
    
    return None
   
def print_state(game_state):
    """
    Takes a game_state object as input, prints game state to terminal
    """
    time, hunger, stress, sleep, motivation = game_state.get_stats()
    
    print "The time is %f" % time
    print "Your hunger is %d" % hunger
    print "Your stress level is %d" % stress
    print "Your sleep level is %d" % sleep
    print "Your motivation level is %d" % motivation

class game_state(object):
    
    def __init__(self, time, hunger, stress, sleep, motivation):
    
        self.time = time
        self.hunger = hunger
        self.stress = stress
        self.sleep = sleep
        self.motivation = motivation
    
    def run_sim(self, action):
    
        hunger, stress, sleep, motivation = action
        
        self.hunger     += hunger
        self.stress     += stress
        self.sleep      += sleep
        self.motivation += motivation
        
        self.time += 0.5
        
    def get_stats(self):
    
        return (self.time, self.hunger, self.stress, self.sleep,
                self.motivation)
    
if __name__ == "__main__":
    main()
