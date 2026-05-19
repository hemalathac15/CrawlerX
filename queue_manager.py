#Step2: This manages URLs waiting to crawl
from collections import deque

class URLQueue:
    def __init__(self):
        self.queue = deque()
        
    def add_url(self, url):
        self.queue.append(url)
        
    def get_url(self):
        return self.queue.popleft()
    
    def has_urls(self):
        return len(self.queue) > 0