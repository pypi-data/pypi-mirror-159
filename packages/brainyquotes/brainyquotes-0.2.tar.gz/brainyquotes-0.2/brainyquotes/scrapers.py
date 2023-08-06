import re
import requests
import random
from bs4 import BeautifulSoup as bs
from lxml import etree

# grab topics
def topics():
    """A function that returns available topics to pass in quotes()"""
    # define empty list for loop
    category = []

    # grab topic html contents
    cat_url = "https://www.brainyquote.com/topics"
    html = requests.get(cat_url)
    text = bs(html.text, "html.parser")

    # grab major topics only (not topic index)
    cat = text.find_all("a", href=re.compile("/topics/"))
    # loop to make readable
    for name in cat:
        category.append(name.text.strip())

    # return list of topics
    return category


# grab quotes
def quotes(category, num):
    """A function that returns a given number of quotes from a given category on
    brainyquote.com"""
    # define empty list for loop
    quotes = []

    # calculate pages to scrape -- site returns 60 quotes per page
    pages = num // 60 + 1

    # grab quotes html contents
    for i in range(pages):
        # grab html contents of each page
        url = "https://www.brainyquote.com/topics/" + category + "_" + str(i)
        html = requests.get(url)
        text = bs(html.content, "html.parser")
        # grab dom elements to use with xpath
        dom = etree.HTML(str(text))
        # xpath is easier to deal with than tags
        xpath_quote = dom.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "oncl_q", " " ))]//div'
        )
        xpath_author = dom.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "oncl_a", " " ))]'
        )
        # this should always be 60 but using this variable to be sure
        total_quotes = len(xpath_quote)
        # get quotes and auhors
        for i in range(total_quotes):
            quotes.append(
                xpath_quote[i].text.strip("\n")
                + " - "
                + xpath_author[i].text.strip("\n")
            )
        # return number of requested quotes
        quotes = quotes[:num]
    return quotes


def random_quote(category, num):
    """A function that returns a random quote using the quote() function"""
    # grab quote
    return random.choice(quotes(category, num))
