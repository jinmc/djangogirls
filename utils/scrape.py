from bs4 import BeautifulSoup
import requests

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

for article in soup.find_all('div', class_='job-item'):

    company_title = article.find('a').text.strip() # company title
    # print(company_title)
    # link somethings dont have..
    try:
        link = ''.join(['job.heykorean.com',article.find('div', class_='title').find('a').get('href')])
        print(f'link : {link}')
        job_desc = article.find('div', class_='title').find('a').text
        print(f'job description : {job_desc}')
        sub_info = article.find('div', class_='sub-info').find_all('span')
        # date_created = article.find('div', class_='sub-info').find('a')
        area = sub_info[0].text
        published_date = sub_info[1].text
        print(f'area : {area}')
        print(f'pub date : {published_date}')
        # print(sub_info)
        deadline = article.find('div', class_='jobDeadLine').find('span').text
        print(f'deadline : {deadline}')
        jobCondition = article.find('div', class_='jobCondition').find_all('span')
        jobstyle = jobCondition[0].text
        salary = jobCondition[1].text
        print(f'jobstyle : {jobstyle}')
        print(f'salary : {salary}')
    except:
        print("none detected")


    # print(article) # print everything
    print("linebreak-------------")
