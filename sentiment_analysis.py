import random
import pandas as pd
from stock_news import get_articles
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

def news_articles():
    articles = get_articles()
    article1 = articles[0]

    df = pd.DataFrame(columns=["Title", "Subjectivity", "Polarity"])

    for article in articles:
        try:
            sentiment = round(TextBlob(article['description']).subjectivity, 2)
            polarity = round(TextBlob(article['description']).polarity, 2)

            df = pd.concat([df, pd.DataFrame([{"Title": article["title"], "Subjectivity": sentiment, "Polarity": polarity}])], ignore_index=True)


        except Exception as e:
            print(e)

    average_polarity = round(df['Polarity'].mean(), 2)
    average_subjectivity = round(df['Subjectivity'].mean(), 2)

    return {"average_polarity": average_polarity, "average_subjectivity": average_subjectivity}

print(news_articles())
# df.to_csv('tesla_news.csv')