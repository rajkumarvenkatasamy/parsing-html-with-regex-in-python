import os
import re
import shutil
import urllib.request

URL = "https://pypi.org/"
HTML_FILE = "file.html"
ALTERED_HTML_FILE = "altered-file.html"

# Source of Empty tags list or Void elements list :
# https://developer.mozilla.org/en-US/docs/Glossary/Void_element
EMPTY_TAGS_LIST = ["area", "base", "br", "col", "embed", "hr", "img", "input", "keygen", "link", "meta", "param",
                   "source", "track", "wbr"]


def write_html_of_given_url_to_file(input_url: str):
    urllib.request.urlretrieve(input_url, HTML_FILE)


def filter_empty_tags(input_file, output_file):
    """
    Accepts two files as input. One will be considered as input and the other will be for writing the output which
    will store html contents from input file except that of empty tags
    :param input_file:
    :param output_file:
    :return:
    """

    shutil.copyfile(input_file, output_file)
    for empty_tag in EMPTY_TAGS_LIST:
        remove_empty_tag_from_html(output_file, empty_tag)


def remove_empty_tag_from_html(input_file, empty_tag_element: str):
    matched = re.compile('<' + empty_tag_element).search
    with open(input_file, "r", encoding="utf-8") as file:
        with open('temp.html', 'w', encoding="utf-8") as output_file:
            for line in file:
                if not matched(line):  # save lines that do not match
                    print(line, end='', file=output_file)  # this goes to filename due to inplace=1

    os.replace('temp.html', input_file)


write_html_of_given_url_to_file(URL)
filter_empty_tags(HTML_FILE, ALTERED_HTML_FILE)
