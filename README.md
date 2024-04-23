## `shorten.py`

This python script uses [tinyurl.com](https://tinyurl.com/) to shorten URLs. It takes a number of URLs in a text file `long_urls.txt` and shortens them. The shortened URLs are then saved in a new csv file `tiny_urls.csv` with two columns: `Long URL` and `Short URL`.

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
