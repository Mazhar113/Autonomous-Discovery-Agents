from environment import Environment
from perception import Perception
from decision import Decision
from execution import Execution
from learning import Learning
from visualization import Visualizer
import time

# Initialize modules
env = Environment(size=20, points_of_interest=5)
perception = Perception()
decision = Decision()
execution = Execution()
learning = Learning()
viz = Visualizer(env)

# Simulation loop
for step in range(50):
    print(f"\n--- Step {step+1} ---")
    
    # 1. Scan environment
    sensor_data = env.scan()
    points = perception.detect_novelty(sensor_data)
    
    if len(points) == 0:
        print("No novel points detected this step.")
    else:
        # 2. Plan & decide tasks
        tasks = [decision.select_task(point) for point in points]
        
        # 3. Execute tasks
        results = [execution.execute_task(point, task) for point, task in zip(points, tasks)]
        
        # 4. Learning & adaptation
        learning.update_strategy(points, results)
    
    # 5. Visualization
    viz.update(agent_pos=env.agent_position, points=points)
    
    time.sleep(0.5)
