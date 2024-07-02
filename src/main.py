import py_trees

class Root(py_trees.composites.Sequence):
    def __init__(self):
        """
        Starts blackboard and connects children nodes.
        """
        super(Root, self).__init__(name="root", memory=True)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

        # Blackboard
        self.blackboard = self.attach_blackboard_client(name="Global")
        self.blackboard.register_key(key="global_read", access=py_trees)
        self.blackboard.register_key(key="global_write", access=py_trees)

        self.parameters = self.attach_blackboard_client(name="Global Parameters", namespace="parameters")
        self.parameters = self.register_key()
    
    def setup(self):
        """
        No hardware / external proccesses for now, does nothing.
        """
        print("Called .setup()")
    
    def initialise(self):
        # Initialize global blackboard tree params
        pass

    
    def update(self):
        """
        Root doesn't do anything special, just ticks.
        """
        pass
        self.logger.debug("Root updated!")
    
    