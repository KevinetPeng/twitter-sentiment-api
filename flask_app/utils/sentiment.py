from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Sentiment:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def __getSingleSentiment(self, str):
        return self.analyzer.polarity_scores(str)
    
    # returns dict of sentiment data in same order of input list and average sentiments
    def getSentiment(self, strList, threshold):
        sentiment_list = []
        compound_sum = 0

        print(f'threshold input: {threshold}')

        summary = {
            'num_positive': 0,
            'num_neutral': 0,
            'num_negative': 0,
            'average_compound': 0,
        }

        for str in strList:
            sentiment = self.__getSingleSentiment(str)
            sentiment_list.append(sentiment)

            compound = sentiment['compound']

            compound_sum += compound

            if compound >= threshold:
                summary['num_positive'] += 1
            elif compound <= -threshold:
                summary['num_negative'] += 1
            else:
                summary['num_neutral'] += 1

        summary['average_compound'] = compound_sum / len(strList)
        
        return {
            'sentiment_list': sentiment_list,
            'summary': summary,
        }