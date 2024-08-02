# Web Scraping

## What is Web Scraping?
Web scraping is a process of extracting, copying, and screening data from various sources. When we extract data or feeds from web pages or websites, it is termed as web scraping. Web scraping, also known as web data extraction or web harvesting, provides a way for developers to collect and analyze data from the internet.

## Why Web Scraping?
Web scraping provides a great tool to automate most of the tasks a human does while browsing. Web scraping is used in an enterprise in various ways:

1. **Data for Research**
    - Smart analysts (like researchers or journalists) use web scrapers instead of manually collecting and cleaning data from websites.

2. **Products Prices & Popularity Comparison**
    - Several services use web scrapers to collect data from numerous online sites and use it to compare product popularity and prices.

3. **SEO Monitoring**
    - Numerous SEO tools such as Ahrefs, Seobility, SEMrush, etc., are used for competitive analysis and for pulling data from clients' websites.

4. **Search Engines**
    - Some big IT companies rely on web scraping for their business operations.

5. **Sales and Marketing**
    - Data gathered through web scraping can be used by marketers to analyze different niches and competitors or by sales specialists for selling content marketing or social media promotion services.

## Why Python for Web Scraping?
Python is one of the most popular languages for web scraping as it can handle most web crawling-related tasks very easily. Below are some reasons to choose Python for web scraping:

- **Ease of Use**
    - Python is very easy to code. It doesn't require curly braces `{}` or semi-colons `;`, making it more readable and easy to use while developing web scrapers.

- **Huge Library Support**
    - Python provides a vast set of libraries for different requirements, making it suitable for web scraping, data visualization, machine learning, etc.

- **Easily Explicable Syntax**
    - Python has a readable syntax that is easy to understand. Its expressive code and indentation help users differentiate different blocks or scopes in the code.

- **Dynamically-typed Language**
    - Python is dynamically typed, meaning the data assigned to a variable defines the type of variable it is. This saves time and makes work faster.

- **Huge Community**
    - The large Python community can assist you whenever you face challenges while writing code.

## Introduction to Beautiful Soup
Beautiful Soup is a Python library named after a Lewis Carroll poem in "Alice’s Adventures in Wonderland". It parses unwanted data and helps to organize and format messy web data by fixing bad HTML and presenting it in easily-traversable XML structures. In short, Beautiful Soup allows us to pull data out of HTML and XML documents.

## Installing Beautiful Soup
Beautiful Soup is not a standard Python library, so we need to install it first. We'll install the Beautiful Soup 4 library (also known as BS4), which is the latest version.

- If you’re using a recent version of Debian or Ubuntu Linux, you can install Beautiful Soup with the system package manager:

```sh
sudo apt-get install python3-bs4
```

- If you’re using Google Colaboratory, you can install Beautiful Soup using the command:

```python
!pip install beautifulsoup4
```

## Making the Soup
The Beautiful Soup object represents the parsed document as a whole.

**Syntax:** 
```python
bs4.BeautifulSoup(markup, "html.parser")
```
**Parameters:** 
- `markup`: The code used to structure and format the content of a webpage (URL used to create the parser).

**Example:** 
```python
bs4.BeautifulSoup(google_search.text, "html.parser")
```

## Finding Elements from the Soup
The `find_all()` method looks through a tag’s descendants and retrieves all descendants that match your filters from the parser stored in a variable.

**Syntax:** 
```python
variable_name.find_all('tags')
```

**Parameters:** 
- `tag`: The tag name whose content needs to be found and extracted from the parser.

**Example:** 
```python
heading_object = soup.find_all('h3')
link = soup.find_all("div", {"class": "yuRUbf"})
```

## Requests Module in Python
The requests module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

**Installation:** 
```sh
pip install requests
```

**Methods:**

### Python Requests get() Method
The `get()` method sends a GET request to the specified URL.

**Syntax:** 
```python
requests.get(url, params={key: value}, args)
```
**Parameters:** 
- `url`: The URL of the request.

## Fontstyle Module in Python
The fontstyle module is a package hosted on pypi.org for manipulating terminal text, making it more readable by adding colors, font weights, and other styles.

**Installation:** 
```sh
pip install fontstyle
```

**Features:**
- Format text
- Preserve formatting
- Remove formatting

**Methods:**

### fontstyle.apply()
This method adds formatting to the entire input argument string.

**Syntax:** 
```python
fontstyle.apply("STRING", "all/possible/formatting/options")
```

**Available Colors:**
- BLACK, BLUE, CYAN, DARKCYAN, GREEN, PURPLE, RED, YELLOW, WHITE

**Background Colors:**
- BLACK_BG, BLUE_BG, CYAN_BG, GREEN_BG, PURPLE_BG, RED_BG, YELLOW_BG, WHITE_BG

**Formatting Arguments:**
- BLINK, BOLD, FAINT, HIDDEN, ITALIC, INVERSE, STRIKE, UNDERLINE, END

### fontstyle.erase()
This method removes the formatting.

### fontstyle.preserve()
This method returns the original text before formatting without removing the actual formatting of the text.

## Conclusion
Although it’s possible to parse data from the web using tools in Python’s standard library, many tools on PyPI can help simplify the process.

In this tutorial, you learned how to:
- Request a web page using Python’s requests module
- Parse HTML using Beautiful Soup
- Repeatedly request data from a website to check for updates

Writing automated web scraping programs is fun, and the internet has no shortage of content that can lead to exciting projects. 

Just remember, not everyone wants you pulling data from their web servers. Always check a website’s Terms of Use before you start scraping, and be respectful about how you time your web requests so that you don’t flood a server with traffic.
```
