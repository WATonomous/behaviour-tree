import py_trees

# Action Node: Drive straight at the node
class CarDriveStraightAtNode(py_trees.behaviour.Behaviour):
    def __init__(self):
        super(CarDriveStraightAtNode, self).__init__(name="Car Drive Straight At Node")
    
    def update(self):
        print("Car is driving straight towards the node.")
        # Implement the driving straight logic 
        return py_trees.common.Status.SUCCESS

# Action Node: Make the car go to the next node in the route list
class MakeCarGoToNextNodeInRouteList(py_trees.behaviour.Behaviour):
    def __init__(self):
        super(MakeCarGoToNextNodeInRouteList, self).__init__(name="Make Car Go To Next Node In Route List")

    def update(self):
        print("Making the car go to the next node in the route list.")
        # Logic to move the car to the next node
        return py_trees.common.Status.SUCCESS

# Action Node: Make the car turn to reach the desired road
class MakeTurnToReachRoad(py_trees.behaviour.Behaviour):
    def __init__(self):
        super(MakeTurnToReachRoad, self).__init__(name="Make Turn To Reach Road")

    def update(self):
        print("Making a turn to reach the desired road.")
        # Logic for turning
        return py_trees.common.Status.SUCCESS

# Action Node: Swap to the node lane
class SwapToNodeLane(py_trees.behaviour.Behaviour):
    def __init__(self):
        super(SwapToNodeLane, self).__init__(name="Swap To Node Lane")

    def update(self):
        print("Swapping to the node lane.")
        # Implement lane swapping logic here
        return py_trees.common.Status.SUCCESS

# Action Node: Mark node as completed and remove from the route
class RemoveNodeFromRoute(py_trees.behaviour.Behaviour):
    def __init__(self):
        super(RemoveNodeFromRoute, self).__init__(name="Remove Node From Route")

    def update(self):
        print("Removing node from the route list after reaching it.")
        # Logic to remove the node
        return py_trees.common.Status.SUCCESS

# Action Node: Mark the current node as completed
class MarkNodeAsCompleted(py_trees.behaviour.Behaviour):
    def __init__(self):
        super(MarkNodeAsCompleted, self).__init__(name="Mark Node As Completed")

    def update(self):
        print("Marking the current node as completed.")
        # Logic for marking the node
        return py_trees.common.Status.SUCCESS