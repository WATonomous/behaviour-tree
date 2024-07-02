import py_trees

class Root(py_trees.composites.Sequence):
    def __init__(self):
        """
        Starts blackboard and connects children nodes.
        """
        super(Root, self).__init__(name="root", memory=True)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

        # Blackboards
        self.blackboard = self.attach_blackboard_client(name="Global")
        self.blackboard.register_key(key="current_pos", access=py_trees.common.Access.WRITE)
        self.blackboard.register_key(key="current_pos", access=py_trees.common.Access.READ)

        self.parameters = self.attach_blackboard_client(name="Global Parameters", namespace="parameters")
        self.parameters = self.register_key(key="pos_tolerance", access=py_trees.common.Access.READ)
    
    def setup(self):
        """
        No hardware / external proccesses for now, does nothing.
        """
        print("Called .setup() on root")
    
    def initialise(self):
        # Initialize global blackboard tree params
        pass
    
    def update(self):
        """
        Root doesn't do anything special, just ticks.
        """
        pass
        self.logger.debug("Root updated!")
    
    