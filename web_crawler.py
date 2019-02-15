from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


def site_map_inside(url, map, domain, i):
    """
    This function makes a mapping of that domain as a Python dictionary. There can be set max deep
    recursion by adding or i = (int of max deep recursion) close to if items.get(url) statement.
    For example if items.get(url) or i = 50:

    :param url: it is current page url
    :param map: it is dictionary sorted like {url: {'title': <title_of_page>, 'links': {links_inside_url}}
    :param domain: it is domain of url
    :param i: max deep of recursion.
    :return: a mapping of that domain as a Python dictionary
    """
    if str(url).startswith(domain):
        if map.get(url):
            pass
        else:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.text, 'html.parser')
            except requests.exceptions.ConnectionError:

                return map
            map[url] = {}
            try:
                map[url]['title'] = soup.head.title.text
            except AttributeError:
                print("Attribute Error")
            if not soup.find_all('a'):
                map[url]['links'] = 'set()'
            else:
                for link in soup.find_all('a'):
                    link_text: object = link.get('href')
                    if str(urljoin(url, link_text)).startswith(domain) and link_text is not None:
                        if domain in urljoin(url, link_text):
                            if map[url].get('links') and not urljoin(url, link_text) in map[url]['links']:
                                map[url]['links'].add(urljoin(url, link_text))
                            elif not map[url].get('links') and urljoin(url, link_text):
                                map[url]['links'] = {urljoin(url, link_text)}
                            site_map_inside(urljoin(url, link_text), map, domain, i + 1)
    return map


def site_map(url):
    """
    It is function that gets as argument site wanted to be mapped.
    :param url: is link to page that is going to be mapped. Needs to be started with https or http.
    :return: a mapping of that url as a Python dictionary
    """
    domain = url
    scrapped_website = {}
    scrapped_website = site_map_inside(url, scrapped_website, domain, 1)
    return scrapped_website


site = 'http://0.0.0.0:8000/'
#site = 'http://127.0.0.1:8000/'


if __name__ == '__main__':
    site_map(site)
