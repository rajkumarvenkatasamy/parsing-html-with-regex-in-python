import os
import re
import urllib.request

URL = "https://pypi.org/"
HTML_FILE = "file.html"
ALTERED_HTML_FILE = "altered-file.html"


def write_html_of_given_url_to_file(input_url: str):
    urllib.request.urlretrieve(input_url, HTML_FILE)


def remove_comments_from_html(input_file, output_file):
    matched = re.compile('<!--').search
    with open(input_file, "r", encoding="utf-8") as file:
        with open('temp.html', 'w', encoding="utf-8") as temp_file:
            for line in file:
                if not matched(line):  # save lines that do not match
                    print(line, end='', file=temp_file)  # this goes to filename due to inplace=1

    os.replace('temp.html', output_file)


write_html_of_given_url_to_file(URL)
remove_comments_from_html(HTML_FILE, ALTERED_HTML_FILE)
