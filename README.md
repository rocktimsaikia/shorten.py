## `shorten.py`

This python script uses [tinyurl.com](https://tinyurl.com/) to shorten URLs in bulk.

It takes a number of URLs in a text file `long_urls.txt` separated by newlines. It then shortens each URL synchronously and writes to a new csv file `short_urls.csv` with the original URL and the shortened URL mapped to the corresponding columns:

1. `Long URL`
2. `Short URL`

> [!NOTE]
> This csv file can be easily imported into a spreadsheet like Google Sheets or Microsoft Excel for further processing.

### Prerequisites

> [!IMPORTANT]
> It is assumed that you have `python3` installed on your system. `tqdm` is also required to display progress bar on the terminal. You can install it using the following command:

```bash
pip install tqdm
```

### Usage

```bash
./shorten.py long_urls.txt
```
