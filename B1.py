import requests
from bs4 import BeautifulSoup

def get_book_links(book):
    atag = book.find("a")
    href = atag["href"]
    link = "https://www.barnesandnoble.com" + href.split(";")[0]
    return link

def get_page_info(page):
    result = requests.get("https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=20&page=" + str(page))
    bs_obj = BeautifulSoup(result.content, "html.parser")
    shelf = bs_obj.find("div", {"class": "product-shelf-list"})
    books = shelf.findAll("h3", {"class": "product-info-title"})
    link_list = [get_book_links(book) for book in books]
    return link_list

with open("C:\\Users\\json_data\\BN_book_links.txt", 'w', encoding='utf-8') as f:
    page = 0
    while True:
        page += 1
        f.write(str(get_page_info(page)))
        if page == 3: break

with open("C:\\Users\\json_data\\BN_book_links.txt", 'r', encoding='utf-8') as f:
    book_links = f.read()

book_links_fixed = book_links.replace("][", ", ")

with open("C:\\Users\\json_data\\BN_book_links.txt", 'w', encoding='utf-8') as f:
    f.write(book_links_fixed)


