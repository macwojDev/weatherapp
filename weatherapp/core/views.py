from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# przydatne komercyjnie, otwieranie chrome w trybie niewidocznym.
chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)


def get_html_content(city):
    url = f'https://www.google.com/search?q=weather+in+{city}'

#   formatowanie parametru, aby wskazywał na poprawny adres url przy miastach o kilkuczłonowej nazwie
    city = city.replace(' ','+')

#   pobieranie kodu html tej strony dzięki .text, bez .text pobiera response http
    driver.get(url)
    accept_button = driver.find_element(by='id', value='L2AGLb')
    accept_button.click()

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

