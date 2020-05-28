from bs4 import BeautifulSoup
import requests
import sqlite3
import os, sys
from datetime import date
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

url = 'http://www.jobkorea.co.kr/recruit/joblist?menucode=duty&dutyCtgr=10016'
page_count = 1

dbfile = os.path.join(BASE_DIR, 'db.sqlite3')
print(dbfile)
conn = sqlite3.connect(dbfile)
c = conn.cursor()
c.execute('DELETE FROM blog_job_jobkorea;')
count = 0
for i in range(10):
    if i == 1:
        url_target = url
    else:
        url_target = url + 'anchorGICnt_' + str(i)

    source = requests.get(url_target).text
    soup = BeautifulSoup(source, 'lxml')

    general = soup.find('div', id='dev-gi-list')

    for job in general.find_all('tr', class_='devloopArea'):
        try:

        # print(job)
            tplco = job.find('td', class_='tplCo') # company name
            company_name = tplco.find('a').text
            count += 1
            titBx = job.find('div', class_='titBx') # job title, desc
            job_title = titBx.find('a').text
            job_description = titBx.find('p', class_='dsc').text
            post_link = 'http://www.jobkorea.co.kr/' + titBx.find('a').get('href')
            etcs = titBx.find('p', class_='etc').find_all('span')
            # print(etcs)
            experience =  etcs.pop(0).text.replace('외', '').strip()
            education = etcs.pop(0).text.replace('외', '').strip()
            area = etcs.pop(0).text.replace('외', '').strip()
            jobstyle = etcs.pop(0).text.replace('외', '').strip()
            if etcs:
                salary = etcs.pop(0).text.replace('외', '').strip()
            odd = job.find('td', class_='odd')
            # print(odd)
            deadline = odd.find('span', class_='date').text.replace('~','')
            deadline = deadline.split('(')[0]
            # print(deadline)

            published_date = odd.find('span', class_='time').text.replace('등록', '').strip()
            # print(published_date)

            # print(titBx)
            # print(tplco)
            print()
            print(company_name, count)
            print(job_title)
            print(job_description)
            print(post_link)
            print(published_date)
            print(area)
            print(jobstyle)
            print(deadline)
            print(salary)
            print(experience)
            print(education)
                #this works
            c.execute(
                "INSERT OR IGNORE INTO blog_job_jobkorea ('company_name', 'job_title', 'post_link', 'published_date', 'job_description', 'area', 'jobstyle', 'deadline', 'salary', 'education', 'experience') VALUES  (?,?,?,?,?,?,?,?,?,?,?)", 
                (company_name, job_title, post_link, published_date, job_description, area, jobstyle, deadline, salary, education, experience)
            )

        except Exception as e:
            print(e)
        # print(etc)
        # break

    print(f'count : {count}')


print("dying now...")
sys.exit()
print("this message will not print")


# scrape jobkorea's it jobs
source = requests.get('http://www.jobkorea.co.kr/recruit/joblist?menucode=duty&dutyCtgr=10016').text
soup = BeautifulSoup(source, 'lxml')

dbfile = os.path.join(BASE_DIR, 'db.sqlite3')
print(dbfile)
conn = sqlite3.connect(dbfile)
c = conn.cursor()
# c.execute('DELETE FROM blog_job_jobkorea;')

# print(soup.prettify())
# all jobs
general = soup.find('div', id='dev-gi-list')
# print(general)

count = 0
for job in general.find_all('tr', class_='devloopArea'):
    # print(job)
    tplco = job.find('td', class_='tplCo') # company name
    company_name = tplco.find('a').text
    count += 1
    titBx = job.find('div', class_='titBx') # job title, desc
    job_title = titBx.find('a').text
    job_description = titBx.find('p', class_='dsc').text
    post_link = 'http://www.jobkorea.co.kr/' + titBx.find('a').get('href')
    etcs = titBx.find('p', class_='etc').find_all('span')
    # print(etcs)
    experience =  etcs.pop(0).text.replace('외', '').strip()
    education = etcs.pop(0).text.replace('외', '').strip()
    area = etcs.pop(0).text.replace('외', '').strip()
    jobstyle = etcs.pop(0).text.replace('외', '').strip()
    if etcs:
        salary = etcs.pop(0).text.replace('외', '').strip()
    odd = job.find('td', class_='odd')
    # print(odd)
    deadline = odd.find('span', class_='date').text.replace('~','')
    deadline = deadline.split('(')[0]
    # print(deadline)

    published_date = odd.find('span', class_='time').text.replace('등록', '').strip()
    # print(published_date)

    # print(titBx)
    # print(tplco)
    print()
    # print(deadline)
    # print(published_date)
    # print(experience)
    # print(education)
    # print(area)
    # print(jobstyle)
    # print(salary)
    # print(post_link)
    # print(job_description)
    # print(company_name, count)
    # print(job_title)
    # break
    
'''
for article in soup.find('div', id='dev-gi-list'):
    # print(article.find('div', class_='company-title').text.strip()) # company title
    # print(article.find('span', class_='date-created').text.strip()) # date created
    # print(article.find('a', class_='job-title').text.strip()) # job title
    # print(''.join(['job.heykorean.com', article.find('a').get('href')])) # make link 
    print(article.prettify()) # to see everything
    print()
'''