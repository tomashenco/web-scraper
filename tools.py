import requests
from lxml import html
import logging

logger = logging.getLogger('log')


def fetch_html(url):
    """
    Gets html and size of it
    :param url: Link to page
    :type url: string
    :return: size of website, content of website
    """
    try:
        results = requests.get(url)
        logger.info('Website found successfully.')
    except requests.exceptions.RequestException:
        logger.error('Failed to find the page: [ %s ]' % url)
        return None, None

    page_size = '%.1fkb' % (int(results.headers.get('Content-Length')) / 1024.0)

    return page_size, results.content


def fetch_links(content):
    """
    Gets all product links
    :param content: Content of page
    :type content: requests content
    :return: links to products
    """
    tree = fetch_tree(content)
    try:
        links = tree.xpath('//div[@class="productInfo"]/h3/a')
    except AttributeError:
        logger.error('Broken tree')
        return []

    return [link.get('href') for link in links]


def fetch_tree(content):
    """
    Gets lxml tree
    :param content: Content of page
    :type content: requests content
    :return: lxml tree
    """
    try:
        return html.fromstring(content)
    except TypeError:
        logger.error('Broken website content')
        return None


def fetch_title(tree):
    """
    Gets product title
    :param tree: lxml tree
    :return: product title
    """
    try:
        (title, ) = tree.xpath('//div[@class="productTitleDescriptionContainer"]/h1/text()')
    except ValueError:
        logger.error('More than one title found per product')
        return ''

    return title


def fetch_price(tree):
    """
    Gets product price
    :param tree: lxml tree
    :return: product price
    """
    try:
        (price, _) = tree.xpath('//div[@class="productSummary"]//p[@class="pricePerUnit"]/text()')
    except ValueError:
        logger.error('More than one price found per product')
        return None

    _, real_price = price.split(u'\xa3')
    return float(real_price)


def fetch_description(tree):
    """
    Gets product description
    :param tree: lxml tree
    :return: product description
    """
    description = tree.xpath('//div[@class="productText"]/p/text()')[0]

    return description


def sum_price(products):
    """
    Sums up total price of products
    :param products: list of products
    :return: total price
    """
    return round(sum(product['unit_price'] for product in products), 2)
