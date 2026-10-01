import time

def get_agent_count(prompt="How many steps should the agent run?: "):
    while True:
        try:
            # Attempt to convert the string input into an integer
            return int(input(prompt))
        except ValueError:
            # Catch invalid formats (letters, symbols, decimals)
            print("Invalid input! That is not a valid integer. Try again.")

class Agent:
    def __init__(self, rooms):
        self.rooms = rooms
        self.current_room_index = 0

    def get_current_room(self):
        return self.rooms[self.current_room_index]

    def move_to_next_room(self):
        self.current_room_index = (self.current_room_index + 1) % len(self.rooms)
    
    def is_room_dirty(self):
        if self.get_current_room()['state'] == 'dirty':
            return True
        else:
            return False

    def clean_room(self):
        self.get_current_room()['state'] = 'clean'
        print(f"Room {self.get_current_room()['name']} has been cleaned.")

    def perceive_and_act(self):
        if self.is_room_dirty():
          self.clean_room()
        else:
          time.sleep(1)
          self.move_to_next_room()
          print("Moving...")

# Initialize rooms
room_a = {
    'name': 'Room A',
    'state': None
}
room_b = {
    'name': 'Room B',
    'state': None
}

rooms = (room_a, room_b)

# Main Display

# Get room states. Limit to only 'dirty' or 'clean' texts.
for room in rooms:
    while room['state'] not in ['dirty', 'clean']:
      room['state'] = input(f"{room['name']} is dirty or clean?: ")
      room['state'] = room['state'].lower()
      if room['state'] not in ['dirty', 'clean']:
        print("Invalid input! Please enter 'dirty' or 'clean'.")

# Print room states
for room in rooms:
    print(f"{room['name']} is {room['state']}")

agent_run = get_agent_count()
step_counter = 0
agent = Agent(rooms)
print("\n")
while agent_run > 0:
    step_counter += 1

    print("Step " + str(step_counter) + ": Agent is in " + agent.get_current_room()['name'])
    for room in rooms:
      print("Environment state: " + room['name'] + "-" + room['state'])
    agent.perceive_and_act()
    print("\n")
    agent_run -= 1

time.sleep(1)
print("Agent has finished running")