from pytree import Node

# action ndoe
class MakeTurnToReachRoad(Node):
    def __init__(self):
        super().__init__()

    def execute(self):
        print("Making turn to reach the desired road.")
        # replace with the action to make the turn

# condition node
class CheckCarIsOnDesiredRoad(Node):
    def __init__(self):
        super().__init__()

    def execute(self):
        print("Checking if car is on the desired road.")
        return True # replace with conditional check

# Define the question node
class EnsureCarIsOnCorrectRoad(Node):
    def __init__(self):
        super().__init__()
        self.left_child = CheckCarIsOnDesiredRoad()
        self.right_child = MakeTurnToReachRoad()

    def execute(self):
        print("Ensuring car is on the correct road.")
        is_correct_road = self.left_child.execute()
        if is_correct_road:
            return self.right_child.execute()

root = EnsureCarIsOnCorrectRoad()

root.execute()
