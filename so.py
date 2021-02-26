import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)

    return int(last_page)


def extract_job(html):
    title = html.find("h2").find("a")["title"]

    company, location = html.find("h3").find_all("span", recursive=False)

    print(location.get_text(strip=True))
    print(company.get_text(strip=True))
    print(title)

    return {"title": title, "company": company, "location": location}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
      print(f"Scrapping page {page+1}")
      result = requests.get(f"{URL}&pg={page+1}")
      soup = BeautifulSoup(result.text, "html.parser")
      job_results = soup.find_all("div", {"class": "-job"})
      
      for job in job_results:
        jobs.append(extract_job(job))

    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)

    return jobs
