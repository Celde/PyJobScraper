import requests
import requests_html
from bs4 import BeautifulSoup


URL = "https://careers.molinahealthcare.com/search-jobs/healthcare%20data%20analyst?orgIds=21726&kt=1"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="search-results-list")

#print(results.prettify())

job_elements = results.find_all("li")

# print(job_elements)
'''
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
'''

#for link in soup.find_all("a"):
#    print(link.get('href'))


navigation_buttons = soup.find(id="pagination-bottom") # ["href"]
buttons = navigation_buttons.find_all("a")
#for button in buttons:
#    print(button.get('href'))
# because we are interested in the 'second' link, which moves us to the next page, we can consistently use the
# index of the second link [1]

next_button = buttons[1]
next_button_url = next_button["href"]
print(next_button_url)


#    print(type(button), button)
#print(buttons)


#    print()
#    print(job_element, end="\n"*2)