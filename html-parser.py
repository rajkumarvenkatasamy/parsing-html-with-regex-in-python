import os
import shutil
import re
import urllib.request


URL = "https://pypi.org/"
HTML_FILE = "C:\\Users\\venkara\\Documents\\Personal\\GitHub\\parsing-html-with-regex-in-python\\file.html"
ALTERED_HTML_FILE = "C:\\Users\\venkara\\Documents\\Personal\\GitHub\\parsing-html-with-regex-in-python\\altered-file.html"

# Source of Empty tags list or Void elements list :
# https://developer.mozilla.org/en-US/docs/Glossary/Void_element
EMPTY_TAGS_LIST = ["area", "base", "br", "col", "embed", "hr", "img", "input", "keygen", "link", "meta", "param",
                   "source", "track", "wbr"]
COMMENT_PATTERN = "<!--"


def get_html(input_url: str) -> bytes:
    html = urllib.request.urlopen(input_url).read()
    return html


def write_html_of_given_url_to_file(input_url: str):
    urllib.request.urlretrieve(input_url, HTML_FILE)


def get_all_referenced_urls(input_url: str) -> list:
    links_list = []

    html = get_html(input_url)
    referenced_urls = re.findall(b'href="(http[s]?://.*?)"', html)
    print("\n ***** Printing all http(s) URLs ***** \n")
    for referenced_url in referenced_urls:
        print(referenced_url.decode())
        links_list.append(referenced_url.decode())

    return links_list


def print_projects_count(input_url: str) -> None:
    html = get_html(input_url)
    stats = re.findall(b'\\d+,?\\d+,?\\d+\\s+projects', html)
    print("\n ***** Printing Projects Count ***** \n")
    for stat in stats:
        print(stat.decode())


def get_content_with_empty_tags(input_url: str) -> list:
    empty_tags_content_list = []

    html = get_html(input_url)

    print("\n ***** Empty tags ***** \n")
    for empty_tag in EMPTY_TAGS_LIST:
        stats = re.findall(b'<' + empty_tag.encode() + b'.*>', html)
        for stat in stats:
            print(stat.decode())
            empty_tags_content_list.append(stat.decode())
    return empty_tags_content_list


def get_commented_lines(input_url: str):
    html = get_html(input_url)

    print("\n ***** Commented Lines ***** \n")

    stats = re.findall(COMMENT_PATTERN.encode() + b'.*>', html)
    for stat in stats:
        print(stat.decode())


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


def remove_comments_from_html(input_file):
    matched = re.compile('<!--').search
    with open(input_file, "r", encoding="utf-8") as file:
        with open('temp.html', 'w', encoding="utf-8") as output_file:
            for line in file:
                if not matched(line):  # save lines that do not match
                    print(line, end='', file=output_file)  # this goes to filename due to inplace=1

    os.replace('temp.html', input_file)


write_html_of_given_url_to_file(URL)
get_all_referenced_urls(URL)
print_projects_count(URL)
get_content_with_empty_tags(URL)
get_commented_lines(URL)
filter_empty_tags(HTML_FILE, ALTERED_HTML_FILE)
remove_comments_from_html(ALTERED_HTML_FILE)
print("\n ***** Reached End of the Program ***** \n")
