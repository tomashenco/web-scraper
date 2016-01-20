import requests
import json
from lxml import html
import logging

logger = logging.getLogger(__name__)


def fetch_html(url):
    try:
        results = requests.get(url)
        logger.info('Website found successfully.')
    except requests.exceptions.RequestException:
        logger.error('Failed to find the page: [ %s ]' % url)
        return None

    return results.content


def fetch_links(content):
    tree = html.fromstring(content)
    links = tree.xpath('//div[@class="productInfo"]/h3/a')
    return [link.get('href') for link in links]


def read_page(page):
    results = requests.get(page)
    tree = html.fromstring(results.content)
    print tree


def scrap():
    """ Gets page and summarises all product information
    :param url: page address
    :return:
    """

    # Specify logger handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    url = 'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html'
    content = fetch_html(url)
    results = fetch_links(content)
    for page in results:
        read_page(page)


scrap()