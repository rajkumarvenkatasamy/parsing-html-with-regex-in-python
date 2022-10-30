import re
import urllib.request

URL = "https://pypi.org/"


def get_html(input_url: str) -> bytes:
    html = urllib.request.urlopen(input_url).read()
    return html


def get_all_referenced_urls(input_url: str) -> list:
    links_list = []

    html = get_html(input_url)
    referenced_urls = re.findall(b'href="(https?://.*?)"', html)
    print("\n ***** Printing all http(s) URLs ***** \n")
    for referenced_url in referenced_urls:
        print(referenced_url.decode())
        links_list.append(referenced_url.decode())

    return links_list


get_all_referenced_urls(URL)
