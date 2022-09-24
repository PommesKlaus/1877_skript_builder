from heapq import merge
from typing import Set
import requests
from bs4 import BeautifulSoup

# Base settings
base_url = "https://moodle-wrm.fernuni-hagen.de/mod/book/"
entry_page = "view.php?id=121362&chapterid=10614"

# Get Cookies from Export file
cookies = dict()
with open("fernuni-hagen.de_cookies.txt", "r") as cookiefile:
    filecontent = cookiefile.read().splitlines()
    for row in filecontent[4:]:
        rowcontent = row.split("\t")
        cookies[rowcontent[5]] = rowcontent[6]

merged_content = []
visited_pages = set(entry_page)
sites_to_visit = [entry_page]

while len(sites_to_visit) > 0:
    url = sites_to_visit.pop(0) # Select first URL from sites_to_visit
    visited_pages.add(url) # Keep track of visited URLs
    r = requests.get(base_url + url, cookies=cookies)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find Chapter Links on Page and add to queue
    chapter_links = [a["href"] for a in soup.select(".book_toc > ul > li a")]
    for link in chapter_links:
        if link not in visited_pages and link not in sites_to_visit:
            sites_to_visit.append(link)
    # Get Book Content and merge
    merged_content = merged_content + soup.select(".book_content")

# print(merged_content)

with open("out.html", "w") as out:
    out.writelines([
        """
        <html>
        <body>
        """
    ])
    out.writelines([str(element) for element in merged_content])
    out.writelines([
        """
        </body>
        </html>
        """
    ])
