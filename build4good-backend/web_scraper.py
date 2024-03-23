from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def get_menu(url):
    
    print('Running...')
    firefox_options = Options()
    
    firefox_options.add_argument("--headless")

    browser = webdriver.Firefox()
    print('pulling')
    browser.get(url)
    print('pulled')
    time.sleep(5)
    innerHTML = browser.page_source

    html = BeautifulSoup(innerHTML, 'html.parser')
    
    item_names = html.find_all('h6', class_="sc-dkrFOg sc-hLBbgP gSBpp dtFsES u-text-ellipsis")
    item_prices = html.find_all('span', itemprop="price")
    
    item_names = [str(name).split('>')[1][:-4] for name in item_names]
    item_prices = [str(price).split('>')[1][1:-6] for price in item_prices]
    for i, price in enumerate(item_prices):
        if price[-1] == '0': continue
        item_prices[i] = price.split('<')[0]
    
    file = open('temp2.txt', 'w')
    file.write(str(innerHTML))
    
    file.close()

    item_data = {}
    for i in range(len(item_names)):
        item_data[item_names[i]] = item_prices[i]
    
    return item_data

# pulled from website

#['Tom Kha Kai', 'Tom Yum Soup', 'Shrimp Soup with Coconut Milk', 'Spicy Shrimp Soup', 'Adobo', 'Pinoy Curry in Coconut Milk', 'Mechado', 'Afritado', 'Pineapple Chicken', 'Bicol Express', 'Sinigang Pork', 'Lechon Kawali', 'Kare Kare', 'Kaldereta', 'Sweet and Sour', 'Basil', 'Red Curry', 'Green Curry', 'Vegetable Fried Rice', 'Chicken Fried Rice', 'Pork Fried Rice', 'Beef Fried Rice', 'Shrimp Fried Rice', 'Combo Fried Rice', 'Pancit Noodles', 'Pancit Noodle Combo', 'Pad Thai Noodle', 'Pad Woon Sen Noodle'] ['$4.50', '$4.50', '$6.50', '$6.50', '$11.00', '$11.00+', '$11.00+', '$11.00+', '$11.00', '$11.00+', '$11.00', '$15.50+', '$15.50+', '$15.50+', '$11.00+', '$11.00+', '$11.00+', '$11.00+', '$9.50', '$11.00', '$11.00', '$15.50', '$15.50', '$16.75+', '$11.00+', '$16.75+', '$11.00+', '$11.00+']