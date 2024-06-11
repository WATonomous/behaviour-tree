import py_trees

def create_root():
    """
    Create a simple behavior tree.

    The tree will have a single sequence node with two child behaviors:
    - A 'Success' behavior that always returns SUCCESS.
    - A 'Failure' behavior that always returns FAILURE.
    """
    # Create a root node (Sequence)
    root = py_trees.composites.Sequence("Sequence", memory=False)

    # Create a success behavior
    success = py_trees.behaviours.Success(name="Success")

    # Create a failure behavior
    failure = py_trees.behaviours.Success(name="Success")

    # Add the success and failure behaviors to the sequence
    root.add_children([success, failure])

    return root

if __name__ == '__main__':
    # Create the root of the tree
    root = create_root()

    # Create a behavior tree with the root
    tree = py_trees.trees.BehaviourTree(root)

    # Run the tree (tick once)
    for i in range(10):
        tree.tick()

    # Print the tree's status
    print(f"Tree status: {tree.root.status}")