import logging
import json
from collections import OrderedDict
from tools import fetch_html, fetch_links, fetch_title, fetch_tree, fetch_price, fetch_description, sum_price


def scrap(url):
    """ Gets page and summarises all product information
    :param url: page address
    :return:
    """

    # Specify logger handler
    logger = logging.getLogger('log')
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Fetch main page
    _, main_content = fetch_html(url)
    # Fetch links to all products on page
    results = fetch_links(main_content)

    # Create a list of products
    products = []
    for page in results:
        size, content = fetch_html(page)
        tree = fetch_tree(content)
        product = OrderedDict([('title', fetch_title(tree)),
                               ('size',  size),
                               ('unit_price', fetch_price(tree)),
                               ('description',  fetch_description(tree))])
        products.append(product)

    # Show the result
    print json.dumps({'results': products, 'totals': sum_price(products)}, indent=2)

scrap('http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html')