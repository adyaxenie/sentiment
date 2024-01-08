import requests
import os
import datetime


def get_articles():
	NEWS_API_KEY = "ff7411a4d0d04371bdbe0571388afcc1"

	start_date = datetime.date(2023, 12, 12)
	end_date = datetime.date.today()

	NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

	news_parameters = {
	    "q": "Tesla",
	    "from": start_date,
	    "sortBy": "popularity",
	    "language": "en",
	    "apiKey": NEWS_API_KEY
	}

	new_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
	new_response.raise_for_status()
	news_data = new_response.json()
	recent_articles = news_data["articles"]
	# recent_article_information = f"{recent_article['title']}: {recent_article['description']}"

	return recent_articles[:100]