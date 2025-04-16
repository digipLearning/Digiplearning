import pandas as pd
import numpy as np

# Load your trained Merlin model
# This could be a TorchScript model or TF SavedModel depending on training pipeline
# Placeholder function below assumes a dummy recommender for illustration

def get_recommendations(learner_data):
    """
    learner_data: dict containing learner performance metrics (e.g., scores, time spent)
    Returns: List of recommended content item IDs or titles
    """
    # Example learner input
    performance_df = pd.DataFrame([learner_data])

    # Simulate recommendation logic (replace with real Merlin model call)
    content_pool = ['Intro to AI', 'Advanced Python', 'Data Science 101', 'Linear Algebra Basics']
    if learner_data.get("score", 0) < 60:
        return [content_pool[0], content_pool[3]]
    else:
        return [content_pool[1], content_pool[2]]
