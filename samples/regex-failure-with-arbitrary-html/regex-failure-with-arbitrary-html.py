import re

ARBITRARY_HTML_FILE = "./arbitrary-html-file.html"


def extract_h2_info_from_arbitrary_html_file(input_file):
    matched = re.compile("(<h2>(.*)</h2>)").search
    with open(ARBITRARY_HTML_FILE, "r") as input_file:
        for line in input_file:
            if matched(line):
                print(line)


extract_h2_info_from_arbitrary_html_file(ARBITRARY_HTML_FILE)
