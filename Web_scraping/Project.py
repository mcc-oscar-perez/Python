# Here we will extract all the books with five or four stars from a ranking page

import bs4
import requests

# Create a URL without the page number 
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Ranking list
high_ranking_list = []

# Iterate pages
for page in range(1,51):
    
    # Create a soup for each page
    url_page = url_base.format(page)
    result = requests.get(url_page)
    soup = bs4.BeautifulSoup(result.text,'html.parser')
    
    # Select book information
    books = soup.select('.product_pod')
    
    # Iterate through the books
    for book in books:
        
        # First we check if the book has 4 or 5 stars
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0 :
            
            # Save title to a variable
            book_title = book.select('a')[1]['title']
            
            # Add books to the list 
            high_ranking_list.append(book_title)
            
# Show books with four or five stars.
for t in high_ranking_list:
    print(t)
            