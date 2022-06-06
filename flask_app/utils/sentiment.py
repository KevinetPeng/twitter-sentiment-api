from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Sentiment:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def __getSingleSentiment(self, str):
        return self.analyzer.polarity_scores(str)
    
