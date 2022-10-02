from bs4 import BeautifulSoup
from lxml import etree
from requests import get
from io import StringIO


def get_tree(url):
    response = get(url)
    html_str = response.text
    return etree.parse(StringIO(html_str), etree.HTMLParser())

def get_vinyl_urls(url):
    tree = get_tree(url)
    first_div ='//div[contains(@class, "grid-list")]'
    second_div = '//div[contains(@class, "product-preview__title")]'
    get_href = '/a/@href'
    hrefs = tree.xpath(first_div+second_div+get_href)
    links = []
    main_page = 'https://collectomania.ru'
    for href in hrefs:
        links.append(main_page+href)
    return links

def remove_whitespaces(s):
    return " ".join(s.split())


def print_info_by_url(url):
    tree = get_tree(url)
    # Выведем название
    name_of_vinyl = get_vinil_name(tree)
    print(f'Название: {name_of_vinyl}')
    # Выведем ссылку на картинку
    image_href = get_vinil_img(tree)
    print(f'Ссылка на изображение: {image_href}')
    # Выведем информацию о пластинке
    info = get_vinil_info(tree)
    for title, value in info:
        title = remove_whitespaces(title.text)
        value = remove_whitespaces(value.text)
        if title[-1] == ':':
            title = title[:-1]
        print(f'{title}: {value}')


def get_vinil_name(tree):
    name_of_vinyl = tree.xpath('//h1[@class="product__title heading"]')[0].text
    return remove_whitespaces(name_of_vinyl)


def get_vinil_img(tree):
    image_href = tree.xpath('//a[@class="img-ratio img-fit product__photo"]/@href')[0]
    return image_href


def get_vinil_info(tree):
    descendant = '//div[contains(@class, "product__chars--list")]//span'
    title_class = '[contains(@class, "product__chars--item--title")]'
    value_class = '[contains(@class, "product__chars--item--value")]'
    titles_arr = tree.xpath(descendant+title_class)
    values_arr = tree.xpath(descendant+value_class)
    return zip(titles_arr, values_arr)


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