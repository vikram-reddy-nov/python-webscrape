from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time
login_url = 'https://sales-history.pwccmarketplace.com/login?title=pokemon'
url = 'https://sales-history.pwccmarketplace.com/?title=pokemon'
xpath = '//div[@class="custom-x2ftu7"]'


def configure_chrome_driver():
#     chrome_options = ChromeOptions()
#     chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
    return driver

driver = configure_chrome_driver()
driver.get(login_url)
time.sleep(5)

driver.find_element_by_id('email').send_keys('vikram.reddy.nov@gmail.com')
driver.find_element_by_id('password').send_keys('Vikked007#pwcc')
driver.find_element_by_class_name('custom-1ujrmx').click()
print('reached 1')
time.sleep(10)
print('reached 2')
driver.find_element_by_xpath("//input").send_keys('pokemon')
driver.find_element_by_class_name('chakra-input__left-element').click()

time.sleep(10)
# Or, you can also "scroll into view" via scrollIntoView():
# driver.execute_script("arguments[0].scrollIntoView();", element)



i=0
while(i < 100):
    pokemons = driver.find_elements_by_xpath('//div[@class="custom-x2ftu7"]')
    print('relooping..')
    print(len(pokemons))
    time.sleep(10)
    i = len(pokemons)
    element = driver.find_element_by_class_name("custom-1l4w6pd")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    
    
for pokemon in pokemons:
#     print(person)
    title = pokemon.find_element_by_class_name('custom-y4x9ed').text
    sold_date = pokemon.find_element_by_class_name('custom-1aq0h2g').text
    sold_price = pokemon.find_element_by_class_name('custom-1iomzz5').text
    auction_type = pokemon.find_element_by_class_name('custom-1ousq9y').text
    payment_status = pokemon.find_element_by_class_name('custom-uazy06').text
    buyers_premium = pokemon.find_element_by_class_name('custom-yvdzps').text
    pokemon_url = pokemon.find_elements_by_tag_name('a')[0].get_attribute('href')

    
    
    print(title)
    print(sold_date)
    print(sold_price)
    print(auction_type)
    print(payment_status)
    print(buyers_premium)
    print(pokemon_url)