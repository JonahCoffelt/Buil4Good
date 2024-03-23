from notion import *
from web_scraper import *

NOTION_TOKEN = "secret_cqvLNy1oJA7hy1A4yv3nx5u7yEROhpW3gmcQfeUab72"
DATABASE_ID = "7a276b34a7914843a66ef1cec7cebecc" 
PAGE_ID = "27bb75d7-0cc8-4b51-a182-aa0056d29c1e"  

# get menu from grubhub using webscraping and firefox
item_data = get_menu('https://www.grubhub.com/restaurant/rr-pinoy--thai-asian-cuisine-4345-wellborn-rd-bryan/5083928')

print(item_data)

# pull pages and ids from notion
pages = get_pages()

# creates dictionary of existing ids and names
page_data = {}
for page in pages:
    page_data[page['properties']["Name"]["title"][0]["text"]["content"]] = page['id']
    
# updates pagea and creates new ones for non-existing entries
for item in item_data:
    
    update_data = get_update_data(item, item_data[item])

    # checks if page exists
    if item in page_data:
        update_page(page_data[item], update_data)
    # create new page if no
    else:
        create_page(update_data)
