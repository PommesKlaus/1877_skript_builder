import requests
from bs4 import BeautifulSoup
from time import sleep

# Base settings
base_url = "https://moodle-wrm.fernuni-hagen.de/mod/book/"
kurseinheiten = [
    "view.php?id=121362&chapterid=10614",  # KE1
    "view.php?id=121368&chapterid=10624",  # KE2
    "view.php?id=121374&chapterid=10633",  # KE3
    "view.php?id=121380&chapterid=10642",  # KE4
    "view.php?id=121386&chapterid=10652",  # KE5
    "view.php?id=121392&chapterid=10661",  # KE6
    "view.php?id=121398&chapterid=10674"   # KE7
]

# Get Moodle Session Cookie from file
cookies = dict()
with open("MoodleSession_cookie.txt", "r") as f:
    cookies["MoodleSession"] = f.read().splitlines()[0]

output = open("output.html", "w")
output.writelines([
    """
<html>
  <link rel="stylesheet" href="style.css" />
  <body>"""])

for nr, kurseinheit in enumerate(kurseinheiten):
    print("Verarbeite Kurseinheit " + str(nr + 1))
    merged_content = []
    visited_pages = set(kurseinheit)
    sites_to_visit = [kurseinheit]

    while len(sites_to_visit) > 0:
        sleep(0.5)  # Slow down requests to Moodle-Server by 1/2 second
        url = sites_to_visit.pop(0)  # Select first URL from sites_to_visit
        visited_pages.add(url)  # Keep track of visited URLs
        r = requests.get(base_url + url, cookies=cookies)
        soup = BeautifulSoup(r.text, 'html.parser')

        print("    " + soup.select_one(".book_toc > ul > li strong").getText())

        # Get Kurseinheit Title-Page
        title_page = soup.select_one(".generalbox")

        # Find Chapter Links on Page and add to queue
        chapter_links = [a["href"]
                         for a in soup.select(".book_toc > ul > li a")]
        for link in chapter_links:
            if link not in visited_pages and link not in sites_to_visit:
                sites_to_visit.append(link)
        # Get Book Content and merge
        merged_content = merged_content + soup.select(".book_content")

    # Write to file, eliminating irregular font-size settings
    output.writelines([str(title_page)])
    output.writelines([str(element).replace("font-size:", "_font-size:") for element in merged_content])

output.writelines([
    """
  </body>
</html>"""
])

output.close()
