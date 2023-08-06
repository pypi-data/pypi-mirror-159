from soccer_articles.article import Article

class BBCArticle(Article):
    source = "bbc"
    author_css_selector = ("span", {"class": "qa-contributor-name"})
    date_css_selector = ("span", {"class": "qa-status-date-output"})
    headline_css_selector = ("h1", {"class": "qa-story-headline"})
    body_css_selector = ("div", {"class": "qa-story-body"})

def get_bbc_articles(urls):
    articles = [BBCArticle(url).to_dict() for url in urls] 
    return [article for article in articles if article["body"] != ""]