import re
import urllib.request


URL = "https://pypi.org/"


def get_html(input_url: str) -> bytes:
    html = urllib.request.urlopen(input_url).read()
    return html


def print_projects_count(input_url: str) -> None:
    html = get_html(input_url)
    stats = re.findall(b'\\d+,?\\d+,?\\d+\\s+projects', html)
    print("\n ***** Printing Projects Count ***** \n")
    for stat in stats:
        print(stat.decode())


print_projects_count(URL)
