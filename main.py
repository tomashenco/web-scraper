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


def parser(content):
    tree = html.fromstring(content)
    links = tree.xpath('//div[@class="productInfo"]')
    for link in links:
        print link


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
    html = fetch_html(url)
    parser(html)


scrap()