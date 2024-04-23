#!/usr/bin/env python3

import urllib.parse
import urllib.request
import time
import csv


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
        return "NA"


def process_urls():
    """Reads URLs from a file, shortens them, and writes the results to a CSV file."""
    with open("urls.txt", "r", encoding="latin1") as file:
        urls = [line.strip().replace("\t", "") for line in file]

    with open("tiny_urls.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Long URL", "Tiny URL"])  # Writing header
        for url in urls:
            print(url)
            tiny = "NA" if len(url) <= 3 else make_tiny(url)
            writer.writerow([url, tiny])
            time.sleep(0.5)


process_urls()
