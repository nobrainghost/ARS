class RecommenderBase:
    def __init__(self):
        pass

    def fit(self, data):
        """Fit the model to the data."""
        raise NotImplementedError("This method should be overridden by subclasses.")

    def recommend(self, user_id, num_recommendations=5):
        """Generate recommendations for a given user."""
        raise NotImplementedError("This method should be overridden by subclasses.")