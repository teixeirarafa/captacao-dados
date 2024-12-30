import pandas as pd
from bs4 import BeautifulSoup
from requests import RequestException, get


def fetch_data(url):
    try:
        response = get(url)
        response.encoding = 'UTF-8'
        return response.text
    except RequestException as error:
        print(f'Error fetching data: {error}')
        return None


def delete_span(element):
    for span in element.find_all('span'):
        span.decompose()


def extract_titles(element):
    titles = []
    container = element.find_all(class_='list-title')
    for i in container:
        delete_span(i)
        titles.append(''.join(i.find_all(string=True)).strip())
    return titles


def extract_authors(element):
    authors = []
    container = element.find_all(class_='list-authors')
    for i in container:
        aux = []
        aux.append(''.join(i.find_all(string=True)).strip())
        authors.append(aux)
    return authors


def extract_primary_subject(element):
    primary_subject = []
    container = element.find_all(class_='primary-subject')
    for i in container:
        primary_subject.append(''.join(i.find_all(string=True)).strip())
    return primary_subject


def extract_links(element):
    links = []
    container = element.find_all('dt')
    for i in container:
        links.append('https://arxiv.org' + i.find_all('a')[1].get('href'))
    return links


url_base = 'https://arxiv.org/list/cs.AI/recent?skip=0&show=100'

html_content = fetch_data(url_base)

if html_content:
    soup = BeautifulSoup(html_content, 'html.parser')

    df = pd.DataFrame(columns=['title', 'authors', 'primary subject', 'article url'])
    df['title'] = extract_titles(soup)
    df['authors'] = extract_authors(soup)
    df['primary subject'] = extract_primary_subject(soup)
    df['article url'] = extract_links(soup)

    df.to_csv('articles-arxiv.csv', index=False)
