# Web Crawler

## Disclaimer

The purpose of this project is to teach you about the ways you can create your own data collection scripts, and not to bring down a website (by flooding it with requests) that doesn't have the computational resources to handle a large volume of requests. If the website has a firewall blocking crawling attempts, please do not attempt to circumvent this. 

You may encounter some websites for which the default lack of headers (no Cookie, CSRF-Token) won't work. It is ok to try to work around this issue by adding those headers as a legitimate workaround (e.g. Page B on a website isn't returning the data you want and throws an error because your request is missing a cookie/token, but you can visit Page A on the same website without those, so you can reuse the cookie/token in the response for Page A within the request for Page B).

## What is a web crawler?

A web crawler is a piece of code that's capable of programmatically visiting a webpage/url and collecting metadata or the HTML/Javascript data that's present for that web target.

## Why is this important?

If you wanted to collect a lot of data/metadata across a large number of web pages, you can automate that using a web crawler! As long as you have some key pieces of information and computer resources, you can point your web crawler towards a target (or multiple) and begin collecting. 

It should be noted that web crawling is also used when testing whether a webpage exists (kind of like guessing and checking); if a GET request is made to a valid URL and a 20x code is returned, the observation that the page exists can be made. This can have various applications.

## Creating a web crawler

When we browse to a web page using a browser (e.g. Google Chrome, FireFox, Safari), our browser makes an HTTP GET request to a server for that page's raw HTML/JS code, which it then renders into what we see on the page. 
When we interact with the page, additional requests are made; for instance if you've filled out a text form and clicked a submit button, an HTTP POST request containing your input was sent to a server. Similarly, if you've ever filtered the results on a search page by toggling checkboxes or a dropdown menu, you may have noticed the URL changing, with additional query parameters appearing at the end.

With code and some thoughts on what data you want to collect, and from where, you can create a program to simulate those interactions for you. Instead of viewing that webpage in your browser, you can now grab the raw code for that webpage and work with that data.s

## What's the difference between this and making automated API calls?

Not much, actually! If you're familiar with how APIs work, and have practiced calling different APIs using the python requests library, the code will functionally be the same; while the purpose will be slightly different.

### Recommended Requirements

To follow along in this tutorial we recommend:

- basic knowledge of Python and the ability to process package documentation
- the ability to know when to ask for help

### Windows Users

To install the necessary modules:
`pip install -r requirements.txt`
To run the file:
In the root project folder, run `python src/web_crawler/main.py`

### MacOS/Linux Users

To install the necessary modules:
`python3 -m pip install -r requirements.txt`
To run the file:
In the root project folder, run `python3 ./src/web_crawler/main.py`

### Exercises

 - Compare the avg # of vulnerabilities per month in a CVE database across multiple years (Threat Intel)
  - Do this comparison for a specific library/package (e.g. log4j, python3.6, django) agnostic of language (e.g. Python package, Java package, C# package, etc)
 - Find the average CVSSv2/v3 score for a given library/package (Vulnerability Management)
 - Check the top x websites for how secure/performant they are (Threat Intel)

#### Resources
 - Get a FREE updated list of the top x websites: https://tranco-list.eu/
  - We would recommend not downloading the .zip file and instead calling the API endpoint documented [here](https://tranco-list.eu/api_documentation) as needed.
 - Here are some CVE/Vulnerability documentation databases that you can crawl, ranked from most popular to least:
  - [NIST Vulnerability Database](https://nvd.nist.gov/vuln/search)
  - [MITRE CVE Database](https://cve.mitre.org/)
  - [CVE Details](https://www.cvedetails.com/)
 - Documentation for the [requests](https://pypi.org/project/requests/) package.
 - Documentation for the [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) package.

#### Functional Milestones
1. Implement the ability to send a GET request to a target
1. Implement the ability to send a POST request to a target
1. Implement error handling for different error codes
 1. Before launching your code and sending GET requests to a large number of targets, it's always a good idea to test with one or two at first, in case you encounter any errors. Debug your request parameters first before running a large test.

#### Bonus Milestones
 - Create visualizations for the data you've collected!
  - You can use the [numpy](https://numpy.org/doc/stable/user/absolute_beginners.html) and [pandas](https://pandas.pydata.org/docs/getting_started/index.html#getting-started) libraries for this
