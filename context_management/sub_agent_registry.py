class SubAgentRegistry:

    def __init__(self):
        # A list to keep track of all active sub-agents.
        self.active_agents = []

    def register(self, sub_agent):
        """
        Add a new sub-agent to the active list.
        """
        self.active_agents.append(sub_agent)

    def deregister(self, sub_agent):
        """
        Remove a sub-agent from the active list.
        """
        self.active_agents.remove(sub_agent)

    def get_active_agents(self):
        """
        Return a list of all active sub-agents.
        """
        return self.active_agents

    def get_agent_status(self, sub_agent):
        """
        Query the status of a specific sub-agent.
        """
        return sub_agent.get_status()

    # ... Additional methods for further sub-agent management and operations ...