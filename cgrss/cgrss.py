import argparse
import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from feedgen.entry import FeedEntry

PAGE_URL = "http://www.davisenterprise.com/business/comings-and-goings/"


def entrygen(entries):
    for entry in entries:
        feedentry = FeedEntry()
        for k, v in entry.items():
            getattr(feedentry, k)(v)
        yield feedentry


def init_feed():
    fg = FeedGenerator()

    fg.title("Comings and Goings")
    fg.author({"name": "Kenneth Lyons", "email": "ixjlyons@gmail.com"})
    fg.link(href="http://www.davisenterprise.com/comings-and-goings/")
    fg.subtitle("Column of the Davis Enterprise by Wendy Weitzel.")
    fg.language("en")

    return fg


def grab_page():
    return requests.get(PAGE_URL).content


def parse_entries(html):
    entries = []
    soup = BeautifulSoup(html, 'html.parser')

    for article in soup.find_all("article"):
        entry_id = article['id']

        head = article.find("header")
        head_a = head.find("a")
        entry_link = {'href': head_a['href']}
        entry_title = head_a.contents[0]

        p = article.find("p")
        entry_description = p.contents[0]

        footer = article.find("footer")
        # super sensitive and stupid hack
        date = footer.contents[1].contents[1].contents[0]
        entry_published = '{} 8:00 PST'.format(date)

        entry = {
            'id': entry_id,
            'title': entry_title,
            'published': entry_published,
            'link': entry_link,
            'description': entry_description}
        entries.append(entry)

    return entries


def generate_feed(filename, entries):
    fg = init_feed()
    for entry in entrygen(entries):
        fg.add_entry(entry)
    fg.rss_file(filename)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate an RSS feed for Comings and Goings.")
    parser.add_argument(
        '-o', '--outfile', default='feed.xml',
        help="Output XML file. Default is `feed.xml` (current directory).")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    html = grab_page()
    entries = parse_entries(html)
    generate_feed(args.outfile, entries)
