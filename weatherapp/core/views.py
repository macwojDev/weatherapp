from django.shortcuts import render
from requests import Session,get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
service = Service(chrome_path)
driver = webdriver.Chrome(service=service)

def get_html_content(city=''):
    url = f'https://www.google.com/search?q=weather+in+{city}'

    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = Session()
#   pobieranie danych z sekcji header kodu html
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE   
    session.headers['Content-Language'] = LANGUAGE
    
#   formatowanie parametru, aby wskazywał na poprawny adres url przy miastach o kilkuczłonowej nazwie
    city = city.replace(' ','+')

#   pobieranie kodu html tej strony dzięki .text, bez .text pobiera response http
    driver.get(url)
    accept_button = driver.find_element_by_xpath('//button[@aria-label="Akceptuj wszystkie pliki cookie"]')
    accept_button.click()

def index(request):
    if 'city' in request.GET:
        from bs4 import BeautifulSoup
        city = request.GET.get('city')
        html_content = get_html_content(city)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        region = soup.find('div', attrs={'id':'wob_loc'})
        print(region)
    return render(request, 'core/index.html')
