from text_tools import get_norm_texts


def get_hrefs(bs):
    hrefs = []
    elements =  bs.select('div.grid-list div.product-preview__title > a')
    for element in elements:
        hrefs.append(element['href'])
    return elements


def get_vinil_name(bs):
    name = get_norm_texts(bs.select('h1.product__title'))[0]
    return name


def get_vinil_img(bs):
    img_href = bs.select('a.product__photo')[0]['href']
    return img_href


def get_vinil_info(bs):
    titles = bs.select('div.product__chars--list span.product__chars--item--title')
    titles = get_norm_texts(titles)
    values = bs.select('div.product__chars--list span.product__chars--item--value')
    values = get_norm_texts(values)
    return zip(titles, values)
