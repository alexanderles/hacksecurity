from bs4 import BeautifulSoup
import requests

# Class which represents our web crawler, which we can use to crawl websites/the Internet
class Crawler():
    """
    
    For any methods with the keyword pass in them, please place the code you'd like to run above the statement, and remove pass completely after doing so.

    """

    def __init__(self):
        pass

    def form_target(self):
        """
        Form the target URL. If you have query parameters, assign them to the path variable below.
        """
        base_url = "???"
        path = "???"
        return base_url + path

    def get_target(self, target : str):
        """
        Send an HTTP GET request to the target.
        """
        in_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
        }
        response = requests.get(target, headers=in_headers)
        if response.status_code == 200: # read about the different response codes here: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
            return response.text
        else:
            # TODO: What else could you do if the response errors out?
            print(f"Response code {response.status_code}, please debug.")
            return None

    def post_target(self):
        """
        Send an HTTP POST request to the target.
        """
        pass

    def parse_target_data(self):
        """
        Parse the data returned from the target, in any way you'd like! Please feel free to add any additional helper methods as needed!!
        """
        data = "???"
        bs = BeautifulSoup(data, "html.parser")
        # print(bs.prettify()) # use prettify to print out HTML in a reader-friendly format
        pass

    def generator_to_list(self, generator):
        """
        Converts the given generator into a list. Generators/iterators can only be iterated over, and cannot be indexed normally.

        :param generator: an object that acts as a generator or iterator.
        """
        array = []
        for value in generator:
            array.append(value)
        return array

    def top_google_search(self, keywords: str):
        """
        Returns link to the top result on the search page for the given keyword(s).

        :param keywords: a string to enter into Google's search engine
        """
        search_keywords = keywords.replace(" ", "%20") # conversion for space to UNICODE

        google_search_response = self.get_target(f"https://www.google.com/search?q={search_keywords}") # first get all HTML for first page of google search
        response_parser = BeautifulSoup(google_search_response, "html.parser")
        first_page_search_results = response_parser.find("div", {"data-async-context": f"query:{search_keywords}"}) # deep dive into the HTML and pull out the search results list
        first_search_result = self.generator_to_list(first_page_search_results)[0] # get the first HTML chunk for the top result from that list
        extracted_url = first_search_result.find("a", href=True) # extract the first url seen across the resulting HTML chunk 
        return extracted_url["href"]
        
    # run this web crawler
    def run(self):
        """
        Run this web crawler by calling the functions you want, here.
        """
        search_keywords = "puppy cat" # <- Feel free to change this value and check out the result!
        first_search_result = self.top_google_search(search_keywords)
        print(first_search_result)