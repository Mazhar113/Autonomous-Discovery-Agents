import random

class Decision:
    def __init__(self):
        self.tasks = ['collect_sample', 'analyze_composition', 'measure_temperature']
    
    def select_task(self, point):
        task = random.choice(self.tasks)
        print(f"Task for point {point}: {task}")
        return task
