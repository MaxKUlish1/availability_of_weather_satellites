from helpers.libs import *


# Получить URL-адреса для различных типов спутников
url = "https://celestrak.com/NORAD/elements/"
response = requests.get(url)


if response.status_code != 200:
    print("Failed to fetch the URL")
else:
    soup = BeautifulSoup(response.text, 'html.parser')

    satellite_urls = {}

    for link in soup.find_all('a'):
        href = link.get('href')
        if href and 'table.php' in href:
            name = href.split('=')[1].split('&')[0]
            satellite_urls[name] = url + name + '.txt'
