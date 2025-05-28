import requests
from bs4 import BeautifulSoup

# Lista de URLs dos sites de notícias
urls = [
    'https://tribunaes.com.br/',
    'https://www.es360.com.br/',
    'https://www.esmais.com.br/',
    'https://www.esfala.com.br/',
    'https://jornaldoes.com.br/'
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

for url in urls:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Exemplo: encontrar títulos em tags <h2>
        titulos = soup.find_all('h2')
        
        print(f'\nTítulos encontrados em {url}:')
        for titulo in titulos:
            print('-', titulo.get_text(strip=True))
    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar {url}: {e}')
