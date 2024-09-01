# filename: fetch_gpt4_paper.py
import requests
from xml.etree import ElementTree

# Query the arXiv API for papers related to GPT-4
url = "http://export.arxiv.org/api/query?"
params = {
    'search_query': 'all:GPT-4',
    'start': 0,
    'max_results': 1,
}
response = requests.get(url, params=params)
data = response.text

# Parse the returned XML data
root = ElementTree.fromstring(data)
entry = root.find('{http://www.w3.org/2005/Atom}entry')

# Extract required information
title = entry.find('{http://www.w3.org/2005/Atom}title').text
authors = ', '.join(author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author'))
summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
published = entry.find('{http://www.w3.org/2005/Atom}published').text

# Output results
print("Title:", title)
print("Authors:", authors)
print("Summary:", summary)
print("Published:", published)