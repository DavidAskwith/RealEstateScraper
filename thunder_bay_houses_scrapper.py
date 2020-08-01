from requests import get
from bs4 import BeautifulSoup
import sys
from listing import Listing

def scrape():
    def split_raw_title(raw_listing):
        return raw_listing.h3.a.text.split(' • ')

    def sanitize_price(raw_price):
        return raw_price.replace('$', '').replace(',', '')

    def get_listings(raw_listings):
        listings = []

        for raw_listing in raw_listings:
            title = split_raw_title(raw_listing)[0]
            price = sanitize_price(split_raw_title(raw_listing)[1])
            description = raw_listing.contents[1]
            url = main_url + raw_listing.h3.a['href']

            listing = Listing(title, price, description, url)
            listings.append(listing)

        return listings

    def get_feature_listings(raw_lisitngs):
        listings = []

        for raw_listing in raw_listings:
            title = split_raw_title(raw_listing)[0]
            price = sanitize_price(split_raw_title(raw_listing)[1])
            description = raw_listing.contents[1]
            url = main_url + raw_listing.h3.a['href']

            listing = Listing(title, price, description, url)
            listings.append(listing)

        return listings

    main_url = 'https://www.thunderbayhouses.com'
    response = get(main_url)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    raw_listings = html_soup.find_all('div', 'listinginfo')

    raw_feature_listings = html_soup.find_all('div', 'feature')

    return get_listings(raw_listings)


print(type(scrape()))
