# Autonomous Discovery & Exploration Agents

## Project Overview
Simulated autonomous agents for exploration and discovery on remote environments (space rovers or deep-sea drones).  
Agents detect novel formations, plan experiments, execute tasks, and learn adaptively.

## Features
- Novelty detection using anomaly detection
- Autonomous task selection and execution
- Reward-based learning for adaptive exploration
- Visualization of rover/drone movement and discoveries
- Fully modular and ready-to-run Python simulation

## Requirements
- Python 3.11+
- Packages: see `requirements.txt`

## Installation
```bash
git clone <repo_url>
cd Autonomous-Discovery-Agents
pip install -r requirements.txt
python main.py
```

## File Overview
- `main.py`: Runs the simulation
- `environment.py`: Simulated terrain and points of interest
- `perception.py`: Sensor processing and anomaly detection
- `decision.py`: Task prioritization and planning
- `execution.py`: Executes tasks and logs data
- `learning.py`: Adaptive exploration logic
- `visualization.py`: Real-time plotting of environment and agent

## License
MIT License
