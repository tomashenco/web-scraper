import logging
import json
from tools import fetch_html, fetch_links, fetch_title, fetch_tree, fetch_price, fetch_description


def scrap():
    """ Gets page and summarises all product information
    :param url: page address
    :return:
    """

    # Specify logger handler
    logger = logging.getLogger('log')
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    url = 'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html'
    _, main_content = fetch_html(url)
    results = fetch_links(main_content)
    for page in results:
        size, content = fetch_html(page)
        tree = fetch_tree(content)
        print fetch_title(tree)
        print fetch_price(tree)
        print fetch_description(tree)


scrap()