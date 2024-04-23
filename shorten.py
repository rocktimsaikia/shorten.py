#!/usr/bin/env python3

import urllib.parse
import urllib.request
import time
from tqdm import tqdm


def make_tiny(url):
    """Shortens a URL using the TinyURL API."""
    request_url = "http://tinyurl.com/api-create.php?" + urllib.parse.urlencode(
        {"url": url}
    )
    try:
        with urllib.request.urlopen(request_url) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        print(f"Error shortening URL {url}: {e}")
        return "N/A"


def process_urls():
    """Reads URLs from a file, shortens them, and writes the results to another file."""
    with open("long_urls.txt", "r", encoding="latin1") as file:
        urls = [line.strip().replace("\t", "") for line in file]

    with open("tiny_urls.txt", "w", encoding="utf-8") as file:
        for url in tqdm(urls):
            print(url)
            tiny = "N/A" if len(url) <= 3 else make_tiny(url)
            file.write(f"{url}\t{tiny}\n")
            time.sleep(0.5)


process_urls()
