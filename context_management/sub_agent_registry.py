class SubAgentRegistry:

    def __init__(self):
        # Initialize the active_entities list to keep track of both agents and sub-agents
        self.active_entities = []

    def register(self, entity, entity_type):
        self.active_entities.append({"entity": entity, "type": entity_type})
        
    def deregister(self, entity, entity_type):
        """
        Remove an entity (agent or sub-agent) from the active list.
        """
        self.active_entities = [e for e in self.active_entities if e['entity'] != entity or e['type'] != entity_type]
        print(f"Entity deregistered: {self.active_entities}")  # Debugging line

    def get_active_agents(self, entity_type=None):
        """
        Return a list of all active entities of the given type.
        If entity_type is None, return all active entities.
        """
        if entity_type:
            return [entity for entity in self.active_entities if entity['type'] == entity_type]
        else:
            return self.active_entities

    def get_agent_status(self, entity, entity_type):
        """
        Query the status of a specific entity (could be an agent or a sub-agent).
        For this example, we're just returning a placeholder as the actual implementation may vary.
        """
        # Placeholder for actual implementation
        return "Active"

    # ..