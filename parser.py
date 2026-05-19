#Extracts link from HTML
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_links(base_url, html):
    discovered_links = []

    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all("a"):
        href = tag.get("href")

        if href:
            full_url = urljoin(base_url, href)
            discovered_links.append(full_url)

    return discovered_links