import requests
from lxml import html
import logging

logger = logging.getLogger('log')


def fetch_html(url):
    try:
        results = requests.get(url)
        logger.info('Website found successfully.')
    except requests.exceptions.RequestException:
        logger.error('Failed to find the page: [ %s ]' % url)
        return None, None

    page_size = int(results.headers.get('Content-Length')) / 1024.0

    return page_size, results.content


def fetch_tree(content):
    return html.fromstring(content)


def fetch_links(content):
    tree = fetch_tree(content)
    links = tree.xpath('//div[@class="productInfo"]/h3/a')
    return [link.get('href') for link in links]


def fetch_title(tree):
    try:
        (title, ) = tree.xpath('//div[@class="productTitleDescriptionContainer"]/h1/text()')
    except ValueError:
        logger.error('More than one title found per product')
        return ''

    return title


def fetch_price(tree):
    try:
        (price, _) = tree.xpath('//div[@class="productSummary"]//p[@class="pricePerUnit"]/text()')
    except ValueError:
        logger.error('More than one price found per product')
        return None

    _, real_price = price.split(u'\xa3')
    return str(real_price)


def fetch_description(tree):
    description = tree.xpath('//div[@class="productText"]/p/text()')[0]

    return description
