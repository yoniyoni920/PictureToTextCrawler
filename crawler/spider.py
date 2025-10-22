class Spider:
    def __init__(self, start_url: str):
        self.start_url = start_url

    def crawl(self):
        print(f"Crawling from {self.start_url}")
