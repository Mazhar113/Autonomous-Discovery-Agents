import numpy as np

class Learning:
    def update_strategy(self, points, results):
        rewards = [np.random.rand() for _ in points]  # simulate rewards
        avg_reward = np.mean(rewards) if rewards else 0
        print(f"Average reward: {avg_reward:.2f}")
        if avg_reward > 0.7:
            print("Strategy successful, increasing exploration autonomy.")
