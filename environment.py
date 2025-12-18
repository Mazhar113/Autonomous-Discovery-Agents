import numpy as np

class Environment:
    def __init__(self, size=20, points_of_interest=5):
        self.size = size
        self.agent_position = [size//2, size//2]
        self.points_of_interest = self._generate_points(points_of_interest)
    
    def _generate_points(self, n):
        return np.random.randint(0, self.size, size=(n,2))
    
    def scan(self):
        # Return simulated sensor readings around the agent
        data = np.random.rand(10,5)
        return data
