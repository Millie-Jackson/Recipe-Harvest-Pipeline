from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

class RecipeScraper:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self.driver = webdriver.Chrome(executable_path='chromedriver-linux64/chromedriver')
    
    def accept_cookies(self) -> None:
        """Method to accept cookies if prompted"""

        try:
            accept_button = self.driver.find_element(By.XPATH, '')
            accept_button.click()
            time.sleep(3)
        except Exception as e:
            print(f"No cookie prompt found: {e}")

    def get_recipe_links(self) -> list:
        """Extracts all recipe links from a page"""

        self.driver.get(self.base_url)
        self.accept_cookies()

        recipe_links = []
        #recipes = self.driver.find_elements(By.CSS_SELECTOR, '')

        #for recipe in recipes:
            #recipe_links.append(recipe.get_attribute('href'))

        return recipe_links
    
    def scrape_recipe(self, recipe_url) -> dict:
        """Extracts core data points from a single recipe"""

        self.drive.get(recipe_url)
        time.sleep(3)

        # Step 1: Get recipe name
        recipe_name = self.get_recipe_name(recipe_url)

        # Extract basic data points
        #title = self.driver.find_element(By.CSS_SELECTOR, '').text
        #description = self.driver.find_element(By.CSS_SELECTOR, '').text
        #ingredients = self.driver.find_element(By.CSS_SELECTOR, '').text
        #instructions = self.driver.find_element(By.CSS_SELECTOR, '').text

        # Format ingredients and instructions
        #ingredient_list = [ingredient.text for ingredient in ingredients]
        #instruction_list = [instruction.text for instruction in instructions]

        # Return the data as a dictionary
        recipe_data = {
            "name": recipe_name
            #'title': title,
            #'description': description,
            #'ingredients': ingredient_list,
            #'instructions': instruction_list
        }

        return recipe_data
    
    def get_recipe_name(self, recipe_url) -> str:

        self.driver.get(recipe_url)
        time.sleep(3) #  Wait for page to load


        if "pickuplimes" in recipe_url:
            recipe_name_element = self.driver.find_element(By.CSS_SELECTOR, "#header-info-col > div > header > h1")
        elif "gazoakleychef" in recipe_url:
            recipe_name_element = self.driver.find_element(By.CSS_SELECTOR, "#post-130150 > header > h1")
        elif "rainbowplantlife" in recipe_url:
            recipe_name_element = self.driver.find_element(By.CSS_SELECTOR, "#content-wrapper > article > header > div.entry-summary > h1")

        recipe_name = recipe_name_element.text

        return recipe_name

    def close(self):
        """Closes browser session"""
        self.driver.quit()



# Test functions
if __name__ == "__main__":

    # Step 1: Initialize scrapers
    scrapers = {
        'PULScraper': RecipeScraper('https://www.pickuplimes.com'),
        'AGVScraper': RecipeScraper('https://www.gazoakleychef.com'),
        'RPLScraper': RecipeScraper('https://www.rainbowplantlife.com')
    }

    all_recipes = [] # Stores all scraped recipes

    for scraper_name, scraper in scrapers.items():
        print(f"Scraping recipes from {scraper_name}...")
    
        # Step 2: Get list of recipe links

        # Example recipe
        recipe_urls = {
            'PickUpLimes': 'https://www.pickuplimes.com/recipe/dan-dan-noodles-894',
            'AvantGuardeVegan': 'https://www.gazoakleychef.com/recipes/stuffed-tomatoes/',
            'RainbowplantLife': 'https://rainbowplantlife.com/malaysian-curry-noodle-soup/'
        }
        #recipe_links = scraper.get_recipe_links()
        recipe_links = recipe_urls
        

        # Step 3: Scrape each recipe
        for link in recipe_links:
            recipe_data = scraper.scrape_recipe(link)
            print(f"Scraped recipe: {recipe_data['name']} from {scraper_name}")

            # Add recipe to master list
            all_recipes.append(recipe_data)

    # Get recipe name
    recipe_url = recipe_urls[scraper_name]
    recipe_name = scraper.get_recipe_name(recipe_url)
    print(f"Recipe Name from {scraper_name}: {recipe_name}")

    scraper.close()

