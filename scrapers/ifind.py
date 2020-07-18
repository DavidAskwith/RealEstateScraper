from requests import get
from bs4 import BeautifulSoup

class Listing:
  def __init__(self, title, price, description, url):
    self.title = title
    self.price = price
    self.description = description
    self.url = url

def scrape():
    def get_price(raw_info):
        price_container = raw_info.find('p', 'price').span
        price = 0
        if price_container is not None:
            price = price_container.text.replace('$', '').replace(',','')

        return price


    def get_description(raw_info):
        raw_prop_info = raw_info.find('div', 'propinfo')
        beds_elem = raw_prop_info.select_one('li.beds > span.right')
        beds = ''
        if beds_elem is not None:
            beds = 'Beds: ' + beds_elem.text + ' '

        baths_elem = raw_prop_info.select_one('li.baths > span.right')
        baths = ''
        if baths_elem is not None:
            baths = 'Baths: ' + baths_elem.text

        return beds + baths

    url = 'https://ifindtbay.ca/?ct_keyword&ct_ct_status=0&ct_price_from&ct_price_to&search-listings=true&ct_beds=0&ct_baths=0&lat&lng'
    response = get(url)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    raw_listings = html_soup.find('ul', { 'id':'search-listing-mapper'}).findChildren('li', recursive=False)

    listings = []

    for raw_listing in raw_listings:
        raw_info = raw_listing.find('div', 'grid-listing-info')
        title = raw_info.h5.a.text
        url = raw_info.h5.a['href']
        listing = Listing(title, get_price(raw_info), get_description(raw_info), url)
        listings.append(listing)

    return listings

print(type(scrape()))
