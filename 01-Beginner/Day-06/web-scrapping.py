import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
parsed_content = soup.prettify()

# Printing the parsed HTML content
print(parsed_content)

# Writing the parsed HTML content to a file
with open("parsed_content.txt", "w", encoding="utf-8") as file:
    file.write(parsed_content)

print("Data has been written to parsed_content.txt")
