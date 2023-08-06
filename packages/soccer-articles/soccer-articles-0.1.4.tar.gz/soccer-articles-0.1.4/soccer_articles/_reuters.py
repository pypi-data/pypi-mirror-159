from soccer_articles.article import Article

class ReutersArticle(Article):
    source = "reuters"
    date_css_selector = ("time", {"data-testid": "Text"})
    headline_css_selector = ("h1", {"data-testid": "Heading"})
    body_css_selector = ("div", {"class": "paywall-article"})

def get_reuters_articles(urls):
    articles = [ReutersArticle(url).to_dict() for url in urls] 
    return [article for article in articles if article["body"] != ""]                   