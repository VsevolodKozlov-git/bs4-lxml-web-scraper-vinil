import scrapping_tools
from bs4 import BeautifulSoup
from requests import get


def get_bs(url):
    response = get(url)
    return BeautifulSoup(response.text, 'html.parser')


def get_vinyl_urls(url):
    bs = get_bs(url)
    els_href = scrapping_tools.get_hrefs(bs)
    links = []
    main_page = 'https://collectomania.ru'
    for el_href in els_href:
        links.append(main_page+el_href['href'])
    return links


def print_info_by_url(url):
    bs = get_bs(url)
    # Выведем название
    name_of_vinyl = scrapping_tools.get_vinil_name(bs)
    print(f'Название: {name_of_vinyl}')
    # Выведем ссылку на картинку
    image_href = scrapping_tools.get_vinil_img(bs)
    print(f'Ссылка на изображение: {image_href}')
    # Выведем информацию о пластинке
    info = scrapping_tools.get_vinil_info(bs)
    for title, value in info:
        if title[-1] == ':':
            title = title[:-1]
        print(f'{title}: {value}')


def get_all_info_from_page(url):
    vinyl_urls = get_vinyl_urls(url)
    for url in vinyl_urls:
        print('-'*40)
        print_info_by_url(url)


def main():
    urls = input('Введите через пробел ссылки на страницы:')
    urls = urls.split()
    for url in urls:
        get_all_info_from_page(url)


if __name__ == '__main__':
    main()