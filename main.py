#step 6 Main Spider
from queue_manager import URLQueue
from downloader import download_page
from parser import extract_links
from graph_builder import WebsiteGraph

import matplotlib.pyplot as plt
import networkx as nx

#Starting URL
seed_url = "https://quotes.toscrape.com"

#Queue
url_queue = URLQueue()

#Add Seed URL
url_queue.add_url(seed_url)

#Visited URL
visited = set()

#Graph object
website_graph = WebsiteGraph()

#limit crawling
MAX_PAGES = 15

while url_queue.has_urls() and len(visited) < MAX_PAGES:

    current_url = url_queue.get_url()

    if current_url in visited:
        continue

    print(f"Crawling: {current_url}")

    visited.add(current_url)

    #Download page
    html = download_page(current_url)

    if not html:
        continue

    #Extract Links
    links = extract_links(current_url, html)

    for link in links:

        #Add graph relationships
        website_graph.add_relationship(current_url, link)

        #Add to queue
        if link not in visited:
            url_queue.add_url(link)

#Draw Graph
plt.figure(figsize=(12, 8))

nx.draw(
    website_graph.get_graph(),
    with_labels=False,
    node_size=50
)

plt.title("Mini Hellhound Spider Graph")

plt.show(block=True)