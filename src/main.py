import py_trees

def create_root():
    """
    Demo single thread BT w/ 2 nodes, just for me to get something to run :)
    """
    # Create a root node
    root = py_trees.composites.Sequence("Sequence", memory=False)

    success = py_trees.behaviours.Success(name="Success")
    failure = py_trees.behaviours.Success(name="Success")

    # Add the success and failure behaviors to the sequence
    root.add_children([success, failure])

    return root

if __name__ == '__main__':
    # Create the root of the tree
    root = create_root()
    tree = py_trees.trees.BehaviourTree(root)

    # some ticks
    for i in range(10):
        tree.tick()

    # Print the tree's final status
    print(f"Tree status: {tree.root.status}")