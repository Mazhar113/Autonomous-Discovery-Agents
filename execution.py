import numpy as np

class Execution:
    def execute_task(self, point, task):
        print(f"Executing {task} at {point}")
        # Simulate data collection
        data = np.random.rand(1,5)
        print(f"Data collected: {data}")
        return data
