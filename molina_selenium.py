#import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
#options = webdriver.ChromeOptions()
#options.add_argument('--incognito')
#options.add_argument('--headless')

driver = webdriver.Chrome()



URL = "https://careers.molinahealthcare.com/search-jobs/healthcare%20data%20analyst?orgIds=21726&kt=1"
#URL = "https://google.com"


driver.get(URL)

'''
soup = BeautifulSoup(driver.page_source, "html.parser")
results = soup.find(id="search-results-list")

#print(results.prettify())

job_elements = results.find_all("li")

for job_element in job_elements:
    title_element = job_element.find("h2")
    company_element = job_element.find(class_="job-location")
    date_element = job_element.find(class_="job-date-posted")
    link_element = job_element.find("a")["href"]
#    link_element = job_element.find("a")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(date_element.text.strip())
    print(f"apply here: {link_element}\n")

pagination_bar = soup.find(id="pagination-bottom")
buttons = pagination_bar.find_all("a")
#for button in buttons:
#    print(button.get('href'))

# because we are interested in the 'second' link, which moves us to the next page, we can consistently use the
# index of the second link [1]

next_button = buttons[1]
next_button_url = next_button["href"]
print(next_button_url)

#driver.find_element_by(next_button_url).click()
#driver.find_element_by_link_text(next_button_url)

driver.find_element(By.CLASS_NAME, "next").click()
'''

for page in range(3):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    results = soup.find(id="search-results-list")
    job_elements = results.find_all("li")

    for job_element in job_elements:
        title_element = job_element.find("h2")
        company_element = job_element.find(class_="job-location")
        date_element = job_element.find(class_="job-date-posted")
        link_element = job_element.find("a")["href"]
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(date_element.text.strip())
        print(f"apply here: {link_element}\n")

    print("XXXXXX NEXT PAGE XXXXXX")

    driver.implicitly_wait(10)
    driver.find_element(By.CLASS_NAME, "next").click()







#driver.find_element(next_button_url).click()


#print(soup)

#page = requests.get(URL)

#soup = BeautifulSoup(page.content, "html.parser")
#results = soup.find(id="search-results-list")
