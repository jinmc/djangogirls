from bs4 import BeautifulSoup
import requests
import sqlite3
import os
from django.utils import timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

source = requests.get('https://job.heykorean.com/web/us/jobs/category?category%5B%5D=13').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())
# platinum job
'''
for article in soup.find_all('div', class_='job-description'):
    print(article.find('div', class_='company-title').text.strip()) # company title
    print(article.find('span', class_='date-created').text.strip()) # date created
    print(article.find('a', class_='job-title').text.strip()) # job title
    print(''.join(['job.heykorean.com', article.find('a').get('href')])) # make link 
    # print(article.prettify()) # to see everything
    print()
'''
dbfile = os.path.join(BASE_DIR, 'db.sqlite3')
print(dbfile)
conn = sqlite3.connect(dbfile)
c = conn.cursor()
# c.execute('DELETE FROM blog_job_heykorean;')
for article in soup.find_all('div', class_='job-item'):
    company_title = article.find('a').text.strip() # company title
    # link somethings dont have..
    try:
        link = ''.join(['job.heykorean.com',article.find('div', class_='title').find('a').get('href')])
        job_desc = article.find('div', class_='title').find('a').text
        sub_info = article.find('div', class_='sub-info').find_all('span')
        area = sub_info[0].text
        published_date = sub_info[1].text
        # print(sub_info)
        deadline = article.find('div', class_='jobDeadLine').find('span').text
        jobCondition = article.find('div', class_='jobCondition').find_all('span')
        jobstyle = jobCondition[0].text
        salary = jobCondition[1].text
        print(f'company_title : {company_title}')
        print(f'link : {link}')
        print(f'job description : {job_desc}')
        # date_created = article.find('div', class_='sub-info').find('a')
        print(f'area : {area}')
        published_date = '20' + '-'.join(published_date.split()[1].split('.'))
        print(f'pub date : {published_date}')
        print(f'deadline : {deadline}')
        print(f'jobstyle : {jobstyle}')
        print(f'salary : {salary}')
        # print(f'date_created : {date_created}')

        c.execute(
            "INSERT OR IGNORE INTO blog_job_heykorean ('company_name', 'post_link', 'job_description', 'area', 'published_date', 'deadline', 'jobstyle', 'salary') VALUES  (?,?,?,?,?,?,?,?)", 
            (company_title, link, job_desc, area, published_date, deadline, jobstyle, salary)
        )

        # this query causes error.. dont know why
        # c.execute("INSERT OR IGNORE INTO blog_job_heykorean ( company_name, post_link, job_description, area, published_date, deadline, jobstyle, salary) VALUES ( :company_name, :post_link, :job_description, :area, :published_date, :deadline, :jobstyle, :salary)", 
        # { 'company_name': company_title, 'post_link': link, 'job_description': job_desc, 'area': area, 'published_date': published_date, 'deadline':deadline, 'jobstyle':jobstyle, 'salary':salary })
        # c.execute()
    except Exception as e:
        print(e)
        print()
conn.commit()
    # print(article) # print everything
    # print("linebreak-------------")
conn.close()