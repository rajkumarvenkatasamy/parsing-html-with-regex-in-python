# parsing-html-with-regex-in-python
Parsing HTML with regex in python

# How to Parse HTML with Regex

The amount of information available for human consumption on the internet is astounding. But if it doesn't come in the form of a specialized REST API, this data can be challenging to access programmatically. The technique of gathering and processing such raw data from the internet is known as web scraping. There are several uses for web scraping in software development. Data collected through web scraping can be applied in Market Research, Lead Generation‍, Competitive Intelligence, Product Pricing Comparison, Monitoring Consumer Sentiment, Brand Audits, AI & Machine Learning, Creating a Job Board, and so on.

Utilizing an HTML parser that is specifically made for parsing out HTML pages is simpler. There are several tools created for web scraping using HTML parsers. [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) library is one such HTML parser for web scraping available and being used by Python programmers. Some prefer to parse HTML pages with Regex. A regular expression (often abbreviated as regex) is a string of letters that designates a text search pattern. Regular expressions are used in lexical analysis, word processors’ search and replace dialogues, text editors' search and replace functions, and text processing tools like sed and AWK.

In this article, you will learn how to parse HTML with Regex by getting your hands dirty in Python. During the course of action, you will download the contents of a website, search for required data using regex, explore use-cases and examples of varying complexity of parsing HTML content using regex, challenges involved in using regex for parsing arbitrary HTML and the alternative solution available to parsing HTML using regex. Without further ado, get ready for action.

## What is parsing using regex?

Regex support is provided by the majority of general-purpose programming languages, including Python, C, C++, Java, Rust, and JavaScript, either natively or through libraries.

Following is a simple regex syntax in Python, that can be used to find the string pattern “<img>” in a given text:

```python
import re

re.findall("<img>", "<img> : This is an image tag")
```

All the source code in this tutorial was developed and executed in Python 3.8.10 to be exact. However, it should work on any machine with Python 3+ version.

In the above example, the module **re** is used for performing operations related to regular expressions. **findall** is a function in the **re** module that is used for returning a list of all matches of a given pattern (first argument value: `<img>`) in the given string (second argument value: `<img>` : This is an image tag).

Using regular expressions to constantly look for and extract substrings that match a specific pattern is one straightforward method of parsing HTML. When your HTML is well-formatted and predictable, regular expressions function quite effectively. Imagine you have an HTML file, **simple.html** with the following code in it:

```html
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Simple HTML File</title>
</head>
<body>
   <h1>Tutorial on How to parse HTML with Regex</h1>
   <p>This is a sample html file used as an example</p>
</body>
</html>
```

And you would like to extract the information contained within the `<title>` tags. With Python, you could use the syntax below:

```python
import re


matched = re.compile('<title>').search
with open("simple.html", "r") as input_file:
   for line in input_file:
       if matched(line):
           print(line.replace("<title>", "").replace("</title>", ""))

```

to meet your goal. Place this Python script file, **simple-html-parser.py** in the same location as that of the simple.html file and run it to get the output as shown below:

```script
python .\simple-html-parser.py

Simple HTML File
```

In the above Python code, a regular expression pattern provided as a string is converted into a regex pattern object using Python's re. compile() function. You can utilize this pattern object to look for matches within various target strings and in this case, the target is the line read from the simple.html file. Once the pattern is matched, the `<title>` tags are removed as the goal is to extract only the string between the `<title>` tag.

Although regex simplifies and aids to build a parser quickly for simple and well-formed HTML sites, a parser application that exclusively uses regular expressions may either overlook some valid links or produce inaccurate data when being used for parsing arbitrary HTML pages online.

Websites may use nested tags in their HTML pages. Nested tags are nothing but an HTML element placed inside another HTML element. And at times, the nesting can go at multiple levels and if you wanted to parse for certain information from a particular level, it would be hard to carry out such tasks and at times carrying out parsing on such HTML will result in errors. Therefore, parsing with regex won’t be an ideal choice in such cases.

With this, you got a basic idea of how regex based HTML parsing works at a high level. Keep progressing with this tutorial to go deep on implementing HTML parsing using regex for more complicated use cases.

## Implementing HTML parsing using regex

### Download the Contents of a Website

To start with, proceed by downloading the site content from the internet on your local machine. For this purpose, you can use the [PyPI site's URL](https://pypi.org/). Create a python file named, **download-site-content.py** and paste the following code:

```python
import urllib.request


URL = "https://pypi.org/"
HTML_FILE = "file.html"


def write_html_of_given_url_to_file(input_url: str):
   urllib.request.urlretrieve(input_url, HTML_FILE)


write_html_of_given_url_to_file(URL)
```

It is a simple program to understand. The method, **write_html_of_given_url_to_file** accepts the input URL of the PyPI site and uses the urlretrieve method of urllib.request module to retrieve the site content and write it into the given file name, file.html. This output HTML file will be created in the same directory where you have placed this Python script.

### Search for Required Data Using Regex

In the earlier section, you have seen an example of how to extract the information within the `<title>` tag of a simple HTML file. Now, in this section, you will see a bit more complicated search use case. You have to search for one of the key stats published on the PyPI site, such as the number of projects published on the PyPI site. A screenshot of this information is shown below:

![PyPI Site](https://i.imgur.com/QoaISGe.png)

Note that the stat value captured in the screenshot is valid during the writing of this tutorial and it may vary when you carry out this exercise. So, you will see a different number in your downloaded file or on the site.

As you can see in the screenshot, there are multiple stats published on the PyPI site like the total number of projects, releases, users, and so on. Among these, you have to extract only the information about the total number of projects. If you view the source code of the downloaded html file in the earlier section, file.html, you will notice that this stat is present as part of a `<p>` tag present inside a `<div>` tag:

```html
<div class="horizontal-section horizontal-section--grey horizontal-section--thin horizontal-section--statistics">
 <div class="statistics-bar">
   <p class="statistics-bar__statistic">
   410,645 projects
   </p>
   <p class="statistics-bar__statistic">
   3,892,920 releases
   </p>
   <p class="statistics-bar__statistic">
   6,961,696 files
   </p>
   <p class="statistics-bar__statistic">
   633,650 users
   </p>
 </div>
</div>
```

You will also notice that there are multiple instances of the word, projects in the file.html. So, the challenge is to extract only the required stat part. Copy and paste the below code in a python file named, print-total-number-of-projects.py


```python
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
```

In the above code, **print_projects_count** is called with the PyPI site URL as input. This method in turn uses the **get_html** method to read the site content and returns the html bytes to the caller method. The **print_projects_count** then uses a regex pattern to get the list of all matches for the supplied pattern. The regex pattern, `b'\\d+,?\\d+,?\\d+\\s+projects'` is the key here to find the total number of projects. Where,
* b stands for bytes
* \\d+ stands for one or more numbers
* , stands for comma, as the stats published in the PyPI site uses comma as a separator
* ? stands for zero or one time match of the previous token, in this case, the previous token is comma
* \\s+ stands for one or more spaces
* projects is just the string, project

Since the return type of findall is a list, an iteration of the list is performed to finally print the project stats to the terminal output.

When you run this script, you will see an output as shown below:

```script
python .\print-total-number-of-projects.py

 ***** Printing Projects Count *****

410,645 projects
```

### Extract Links

Based on the above understanding of parsing HTML with regex, see if you can program to extract links (any https or http referenced urls) from the same site. You have all the help you need from the earlier sections, the only thing that you have to do is find the right regular expression for your goal of extracting these http(s) URLs.

You can consider this as an exercise to carry out, but don’t worry, if you want an answer, you can refer to the source code in, samples/extract-links.py in the [github repository](https://github.com/rajkumarvenkatasamy/parsing-html-with-regex-in-python)

When you run the given script using the command `python extract-links.py`, you will be displayed with the list of referenced URL links in the PyPI site.

### Filter Empty Tags

HTML supports and has empty tags, the tags which can’t have any nested tags or child nodes. These empty tags are known also as Void elements. These usually have a start tag and need not have an end tag as it is required to have one for non empty tags. Even if you have specified an end tag in the HTML page for such empty tags, the browser won’t throw an error. Refer this [link](https://developer.mozilla.org/en-US/docs/Glossary/Void_element) to understand more on these empty tags and to know the list of empty tags in HTML.

If you want to filter out these empty tags from the downloaded PyPI site’s HTML file, how would you go about it? Copy and paste the code shared in the [GitHub repository](https://github.com/rajkumarvenkatasamy/parsing-html-with-regex-in-python) from the file, samples/filter-empty-tags/filter-empty-tags-from-html.py into a file on your machine. Call it as, filter-empty-tags-from-html.py.

Run the command given below:

```script
python filter-empty-tags-from-html.py
```

This will create two files (file.html and altered-file.html) in the directory where you have placed and executed the above Python script. The original downloaded content of the PyPI site is contained in the file.html file and the modified html content (after filtering the empty tags) is contained in the altered-file.html.

In a similar way, you can do the filtering of comments from the HTML page. Comments in HTML are represented as:

```html
<!-- I am a HTML comment -->
```

You can try this use case from your end based on the learnings from the earlier section on  filtering empty tags. If you want a source code for this use case, refer to the method, **remove_comments_from_html**, in the file, **html-parser.py** shared in the [GitHub repository](https://github.com/rajkumarvenkatasamy/parsing-html-with-regex-in-python) under the directory, samples/html-parser. This Python file also contains the source code for all the use cases covered in this article in one place for your reference.

## How Regex Fails with Arbitrary HTML

So far, you have seen how regex can be used to parse an HTML page. However, when the parsing is to be done on an arbitrary HTML with irregular tags or no standard format involved, you will also witness how parsing with regex misses out the required information to be extracted.

The sample files used for this use case demo is available under the samples/regex-failure-with-arbitrary-html directory of the GitHub repository. The html file has the content shown below:

```html
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Arbitrary HTML</title>
</head>
<body>
 <div id="1">
     <h1>Heading 1 of Section 1</h1>
     <h2>Heading 2 of Section 1</h2>
     <h3>Heading 3 of Section 1</h3>
 </div>
 <div id="2">
     <h1>Heading 1 of Section 2</h1>
     <h2>Heading 2 of Section 2</h2>
     <h3>Heading 3 of Section 2</h3>
 </div>
 <div id="3">
     <h1>Heading 1 of Section 3</h1>
     <h2>
         <p>Heading 2 of Section 3</p>
         <br>
     </h2>
     <h3>Heading 3 of Section 3</h3>
 </div>
</body>
</html>
```

Notice that the `<h2>` tag of the third `<div>`  is nested with child tags `<p>`, and an empty tag `<br>`. If your goal is to extract all the information available as part of all `<h2>` tags, such an HTML format would present a challenge.

Copy and paste the code below:

```python
import re

ARBITRARY_HTML_FILE = "./arbitrary-html-file.html"


def extract_h2_info_from_arbitrary_html_file(input_file):
   matched = re.compile("(<h2>(.*)</h2>)").search
   with open(ARBITRARY_HTML_FILE, "r") as input_file:
       for line in input_file:
           if matched(line):
               print(line)


extract_h2_info_from_arbitrary_html_file(ARBITRARY_HTML_FILE)
```
in a file named, regex-failure-with-arbitrary-html.py and remember to copy the HTML content also into a file named, arbitrary-html-file.html. Both these files should be present in the same directory. Now run,

```script
python regex-failure-with-arbitrary-html.py
```

You will get an output shown below:

```script-output
      <h2>Heading 2 of Section 1</h2>

      <h2>Heading 2 of Section 2</h2>                                                                                      
```                                               

Notice that the information in the third `<h2>` tag fails to get retrieved by using the regex parser. When one of the HTML tags is nested with multiple tags than that of other equivalent tags, parsing such a content with regex has its own drawbacks. Hence, you can use alternative and more robust solutions including but not limited to Scrapingbee, BeautifulSoup, JSoup, and Selenium. 

