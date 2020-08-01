from requests import get
from bs4 import BeautifulSoup
from listing import Listing

def scrape():
    def get_price(raw_listing):
        price_container = raw_listing.find('p', 'price').span
        price = 0
        if price_container is not None:
            price = price_container.text.replace('$', '').replace(',','')

        return price


    def get_description(raw_listing):
        raw_prop_info = raw_listing.find('div', 'propinfo')
        beds_elem = raw_prop_info.select_one('li.beds > span.right')
        beds = ''
        if beds_elem is not None:
            beds = 'Beds: ' + beds_elem.text + ' '

        baths_elem = raw_prop_info.select_one('li.baths > span.right')
        baths = ''
        if baths_elem is not None:
            baths = 'Baths: ' + baths_elem.text

        return beds + baths

    main_url = 'https://ifindtbay.ca/?ct_keyword&ct_ct_status=0&ct_price_from&ct_price_to&search-listings=true&ct_beds=0&ct_baths=0&lat&lng'
    response = get(main_url)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    raw_listings = html_soup.find('ul', { 'id':'search-listing-mapper'}).find_all('div', 'grid-listing-info')
    listings = []

    for raw_listing in raw_listings:
        title = raw_listing.h5.a.text
        url = raw_listing.h5.a['href']
        listing = Listing(title, get_price(raw_listing), get_description(raw_listing), url)
        listings.append(listing)

    return listings

print(type(scrape()))
