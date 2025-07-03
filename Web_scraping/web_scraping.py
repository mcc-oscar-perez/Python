import bs4
import requests

# here we choice the page we want to scrape
# and we use the requests library to get the content of the page
resultado = requests.get("https://escueladirecta-blog.blogspot.com/")

sopa = bs4.BeautifulSoup(resultado.text, "lxml")
title_tags = sopa.select("title")
if title_tags:
	print(title_tags[0].getText())
else:
	print("No title tag found.")() 


# if we want to obtain all paragraphs from the page
parrafo = sopa.select('p')

#%%
# if we want to extract the text from the class
import bs4
import requests

# 1.- Choose the page we want to scrape
resultado = requests.get("https://escueladirecta-blog.blogspot.com/")

# 2.- Use BeautifulSoup to parse the content
sopa = bs4.BeautifulSoup(resultado.text, "html.parser")

# 3.- Select the first box with class "post-body"
first_box = sopa.select('.post hentry')

# 4.- print the text of the first box
print(first_box)
# %%

# if we cant to extract images from the page

import bs4
import requests

# 1.- Choose the page we want to scrape
resultado = requests.get("https://www.escueladirecta.com/l/products?sortKey=name&sortDirection=asc&page=1")

# 2.- Use BeautifulSoup to parse the content
sopa = bs4.BeautifulSoup(resultado.text, "html.parser")

# 3.- Select the first box with class "post-body"
images = sopa.find('img', alt="Product image for Excel Aplicado al Análisis Financiero")
if images:
    img_url = images['src']

    # 4.- download the image
    img_url = requests.get(img_url).content
    with open('excel_aplicado_al_analisis_financiero.jpg', 'wb') as file:
        file.write(img_url)

    # 5.- print the image url
    print(img_url)
else:
    print("No image found with the specified alt text.")
# %%
