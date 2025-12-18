from sklearn.ensemble import IsolationForest
import numpy as np

class Perception:
    def detect_novelty(self, sensor_data):
        model = IsolationForest(contamination=0.2)
        novelty = model.fit_predict(sensor_data)
        points = sensor_data[novelty == -1]
        if len(points) > 0:
            print(f"Novel points detected: {points.shape[0]}")
        return points
