def get_norm_texts(bs_elements):
    texts = []
    for element in bs_elements:
        norm_text = get_el_norm_texts(element)
        texts.append(norm_text)
    return texts


def get_el_norm_texts(element):
    return remove_whitespaces(get_el_raw_text(element))


def get_el_raw_text(element):
    return element.find(text=True, recursive=False)


def remove_whitespaces(s):
    return " ".join(s.split())