from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from nltk import tokenize

def sentimentAnlysis(paragraph):
	analyser = SIA()
	snt = analyser.polarity_scores(paragraph)
	print(str(snt))

if __name__ == "__main__":
    print("short paragraph")
    paragraph = "The food is really GOOD! But the service is dreadful."
    sentimentAnlysis(paragraph)
    print("bad news")
    file = open('./badnews.txt', 'r')
    text = file.read().strip()
    file.close()
    sentimentAnlysis(text)
    print("good news")
    file2 = open('./goodnews.txt', 'r')
    text2 = file2.read().strip()
    file2.close()
    sentimentAnlysis(text2)
