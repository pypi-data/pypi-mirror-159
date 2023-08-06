import requests
from bs4 import BeautifulSoup

class Article:
    """Article base class. Inheriting from `Article` can be useful to
    create a simple news scraper, provided that the different CSS
    selectors are defined. The CSS selectors must be defined in the subclass
    as tuples (tag, { selector_type: selector_value }):

    tag: HTML tag (e.g "span", "div", "p", etc.)
    selector_type: "class", "id", etc. 
    selector_value: value of the `selector_type`.

    Parameters
    ----------
    url : str
        URL of the article. 
    Attributes
    ----------
    source : str
        News website name
    author_css_selector : tuple
        CSS selector targeting the author name.
    headline_css_selector : tuple
        CSS selector targeting the title.
    body_css_selector: 
        CSS selector targeting the main content.

    Examples
    --------
    >>> from news.article import Article
    >>> class BBCArticle(Article):
    ...     source = "bbc"
    ...     author_css_selector = ("span", {"class": "qa-contributor-name"})
    ...     date_css_selector = ("span", {"class": "qa-status-date-output"})
    ...     headline_css_selector = ("h1", {"class": "qa-story-headline"})
    ...     body_css_selector = ("div", {"class": "qa-story-body"})
    
    >>> bbc_articles = BBCArticle("https://www.bbc.com/sport/av/football/61314388")
    """

    def __init__(self, url):
        self.url=url
        self.soup=self._fetch_article(url)
        
    def __repr__(self):
        return f"{self.date} - {self.author}\n{self.headline}"
    
    @staticmethod
    def _fetch_article(url):
        page = requests.get(url)
        return BeautifulSoup(page.content, "html.parser")

    @property
    def source(self):
        raise NotImplementedError
            
    @property
    def author_css_selector(self):
        raise NotImplementedError
    
    @property
    def date_css_selector(self):
        raise NotImplementedError
        
    @property
    def headline_css_selector(self):
        raise NotImplementedError
    
    @property
    def body_css_selector(self):
        raise NotImplementedError
        
    @property
    def author(self):
        try:
            return self.soup.find(*self.author_css_selector).text
        except:
            return ""
    
    @property
    def date(self):
        try:
            return self.soup.find(*self.date_css_selector).text
        except:
            return ""
    
    @property
    def headline(self):
        try:
            return self.soup.find(*self.headline_css_selector).text
        except:
            return ""
        
    @property
    def body(self):
        try:
            return self.soup.find(*self.body_css_selector).text
        except:
            return ""
        
    def to_dict(self):
        return {
            "source": self.source,
            "url": self.url,
            "author": self.author,
            "date": self.date,
            "headline": self.headline,
            "body": self.body
        }
    