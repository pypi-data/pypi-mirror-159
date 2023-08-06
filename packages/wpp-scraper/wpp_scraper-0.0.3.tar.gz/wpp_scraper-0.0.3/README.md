# Whatsapp-Web-Scraper-
The Most Powerful Contact Scraper for Whatsapp Web.

## Why the most powerful?
This powerful scraper is based on non-dynamic selectors, with well-structured and thought-out strategies for finding elements on the page. That's why it doesn't get lost with the change of classes and id's that happen in apps like instagram, whatsapp among others. Having a much longer lifetime and providing more security in its implementation.

## How to install:
###

To run you need chrome installed.
```
pip install --upgrade selenium
pip install --upgrade webdriver-manager
```

### Example:
```
from whats_scraper import WhatsAppScraper

test=WhatsAppScraper()
test.login()
test.get_all_names_contacts()
test.get_my_contacts()
```
