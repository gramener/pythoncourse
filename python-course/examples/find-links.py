"""Program to display all links in a web page.

USAGE: python find-links.py http://example.com/
"""

import sys
import urllib2
from urlparse import urljoin
from bs4 import BeautifulSoup

def wget(url):
    """Downloads the given url and returns all the contents.
    """
    return urllib2.urlopen(url).read()

def get_links(html):
    """Returns all links in the given html.
    """
    soup = BeautifulSoup(html)
    # find all <a> tags
    a_tags = soup.find_all("a")
    # and take the 'href' attribute
    links = [a['href'] for a in a_tags if "href" in a.attrs]
    return links

def main():
    url = sys.argv[1]
    html = wget(url)
    links = get_links(html)
    for link in links:
        # convert link to absolute URL
        link = urljoin(url, link)
        print link

if __name__ == "__main__":
    main()