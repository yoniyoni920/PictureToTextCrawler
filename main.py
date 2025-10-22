from crawler.spider import Spider
from parsers.html_parser import HTMLParser
from storage.json_storage import JSONStorage

def main():
    spider = Spider("https://example.com")
    spider.crawl()

    parser = HTMLParser()
    data = parser.parse("<html>...</html>")

    storage = JSONStorage()
    storage.save(data, "results.json")

if __name__ == "__main__":
    main()
