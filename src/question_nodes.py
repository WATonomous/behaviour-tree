import py_trees
import condition_nodes
import action_nodes

# Question Node: Check if the car is at the goal
class EnsureCarAtGoal(py_trees.composites.Selector):
    def __init__(self):
        super(EnsureCarAtGoal, self).__init__(name="Ensure Car At Goal")
        self.add_children([condition_nodes.AtGoalLocation(), condition_nodes.LastNodeInRoute()])

    def update(self):
        print("Checking if the car is at the goal.")
        return super(EnsureCarAtGoal, self).tick()

# Question Node: Check if the car is at the next node in the route
class EnsureCarAtNextNode(py_trees.composites.Selector):
    def __init__(self):
        super(EnsureCarAtNextNode, self).__init__(name="Ensure Car At Next Node")
        self.add_children([condition_nodes.AtNextNode(), action_nodes.RemoveNodeFromRoute()])

    def update(self):
        print("Checking if the car is at the next node in the route.")
        return super(EnsureCarAtNextNode, self).tick()

# Question Node: Check if the car is on the correct road
class EnsureCarOnCorrectRoad(py_trees.composites.Selector):
    def __init__(self):
        super(EnsureCarOnCorrectRoad, self).__init__(name="Ensure Car On Correct Road")
        self.add_children([condition_nodes.CheckCarOnDesiredRoad(), action_nodes.MakeTurnToReachRoad()])

    def update(self):
        print("Checking if the car is on the correct road.")
        return super(EnsureCarOnCorrectRoad, self).tick()

# Question Node: Check if the car is in the correct lane
class EnsureCarOnCorrectLane(py_trees.composites.Selector):
    def __init__(self):
        super(EnsureCarOnCorrectLane, self).__init__(name="Ensure Car On Correct Lane")
        self.add_children([condition_nodes.CheckCarOnCorrectLane(), action_nodes.SwapToNodeLane()])

    def update(self):
        print("Checking if the car is in the correct lane.")
        return super(EnsureCarOnCorrectLane, self).tick()