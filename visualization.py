import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    def __init__(self, env):
        self.env = env
        plt.ion()
        self.fig, self.ax = plt.subplots()
    
    def update(self, agent_pos, points):
        self.ax.clear()
        self.ax.set_xlim(0, self.env.size)
        self.ax.set_ylim(0, self.env.size)
        self.ax.plot(agent_pos[0], agent_pos[1], 'bo', label='Agent')
        if len(points) > 0:
            pts = np.array(points)
            self.ax.scatter(pts[:,0], pts[:,1], c='r', marker='x', label='Novel Points')
        self.ax.legend()
        plt.draw()
        plt.pause(0.01)
