## `shorten.py`

This python script uses [tinyurl.com](https://tinyurl.com/) to shorten URLs. It takes a number of URLs in a text file `long_urls.txt` and shortens them. The shortened URLs are then saved in a new text file `tiny_urls.txt` with mapping of long and short URLs.

### Prerequisites

> [!IMPORTANT]
> Note that [Python3](https://www.python.org/downloads/) is required to run this script.
> `tqdm` is also required to display progress bar. We can install it using pip like below.

```bash
pip install tqdm
```

### Usage

```bash
shorten.py long_urls.txt
```
