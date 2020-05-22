from bs4 import BeautifulSoup
import requests

source = requests.get('https://job.heykorean.com/web/us/jobs/category?category%5B%5D=13').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())
# platinum job

for article in soup.find_all('div', class_='job-description'):
    print(article.find('div', class_='company-title').text.strip()) # company title
    print(article.find('span', class_='date-created').text.strip()) # date created
    print(article.find('a', class_='job-title').text.strip()) # job title
    print(''.join(['job.heykorean.com', article.find('a').get('href')])) # make link 
    # print(article.prettify()) # to see everything
    print()

'''
for article in soup.find_all('div', class_='job-item'):
    # print(article.find('a').text.strip()) # company title
    try:
        print(article.find('div', class_='jobTitle').a.text.strip())

    # print(article) # print everything
    # print()
'''