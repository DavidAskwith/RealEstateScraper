import thunder_bay_houses_scrapper
import ifind_scrapper

listings = thunder_bay_houses_scrapper.scrape()
listings += ifind_scrapper.scrape()

for listing in listings:
    if listing.price < 200000:
        print(f'Title: { listing.title }')
        print(f'Price: ${ listing.price }')
        print(f'Description: { listing.description }')
        print(f'URL: { listing.url }')
        print()
