from bs4 import BeautifulSoup
import requests

response= requests.get("https://news.ycombinator.com/news")  
yc_web_page=response.text

soup=BeautifulSoup(yc_web_page, "lxml")
articles=soup.find_all(name="span", class_="titleline")

article_texts=[]
article_links=[]

for article_tag in articles:
  article_text=article_tag.find("a").getText()
  article_texts.append(article_text)
  article_link=article_tag.find("a").get("href")
  article_links.append(article_link)

article_upvotes= [score.getText() for score in soup.find_all(name="span", class_="score")] 

print(article_texts)
print(article_links)
print(article_upvotes)
