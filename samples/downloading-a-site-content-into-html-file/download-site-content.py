import urllib.request


URL = "https://pypi.org/"
HTML_FILE = "../PyPI-Site-HTML-File/file.html"


def write_html_of_given_url_to_file(input_url: str):
    urllib.request.urlretrieve(input_url, HTML_FILE)


write_html_of_given_url_to_file(URL)
