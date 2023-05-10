from django.shortcuts import render
from requests import Session,get
from selenium import webdriver





driver = webdriver.Chrome()
def get_html_content(city):
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
    accept_button = driver.find_element(by='id', value='L2AGLb')
    accept_button.click()
    return driver

def index(request):
    if 'city' in request.GET:
        from bs4 import BeautifulSoup
        city = request.GET.get('city')
        get_html_content(city)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        region = soup.find('span', attrs={'class':'BBwThe'}).text
        temperatura = soup.find('span', attrs={'id':'wob_tm'}).text
        print(temperatura)
        print(region)
        context = {'region' : region,
                   'temperatura' : temperatura
                   }
    return render(request, 'core/index.html', context)

