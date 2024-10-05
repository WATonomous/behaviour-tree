import py_trees
from condition_nodes import AtGoalLocation, LastNodeInRoute
from question_nodes import EnsureCarAtNextNode
from action_nodes import RemoveNodeFromRoute

"""_summary_
Metadrive, map the highlevel to lowlevel
"""


class Root(py_trees.composites.Sequence):
    def __init__(self):
        super(Root, self).__init__(name="Root", memory=True)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

        self.add_children([
            AtGoalLocation(),           # Check if car is at the goal
            LastNodeInRoute(),          # Check if the last node in the route is reached
            EnsureCarAtNextNode(),      # Ensure car moves to the next node in the route
            RemoveNodeFromRoute()       # Remove the node from the list after reaching it
        ])

    def setup(self):
        """
        Set up the root node. No hardware or external processes at the moment.
        """
        print("setting up the root node and blackboard")
        # Initialize the blackboard
        blackboard = py_trees.blackboard.Blackboard()
        blackboard.current_pos = [0, 0]   # Starting position of the car
        blackboard.goal_pos = [10, 10]    # Goal position for the car
        blackboard.route_list = [[0, 0], [5, 5], [10, 10]]  # Example route with 3 nodes
        blackboard.next_node = blackboard.route_list[0]
        blackboard.desired_road = blackboard.route_list[1]
        blackboard.current_lane = blackboard.route_list[2]
        blackboard.last_node = blackboard.route_list[-1]

        py_trees.blackboard.Blackboard.enable_activity_stream(maximum_size=100)
        print("blackboard setup complete")
        return py_trees.common.Status.SUCCESS

    def update(self):
        """
        Executes the sequence of actions by ticking the behavior tree.
        """
        self.logger.debug("Root is updating.")
        return super(Root, self).tick()

# In the main execution file
if __name__ == "__main__":
    root = Root()
    root.setup()           
    py_trees.logging.level = py_trees.logging.Level.DEBUG
    py_trees.blackboard.Blackboard.enable_activity_stream(maximum_size=100)  
    py_trees.display.render_dot_tree(root)  
    py_trees.trees.BehaviourTree(root).tick_tock(5000)  