from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

class RecipeScraper:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self.driver = webdriver.Chrome(executable_path='chrome-linux64/chrome')
    
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
        recipes = self.driver.find_elements(By.CSS_SELECTOR, '')

        for recipe in recipes:
            recipe_links.append(recipe.get_attribute('href'))

        return recipe_links
    
    def scrape_recipe(self, recipe_url) -> dict:
        """Extracts core data points from a single recipe"""

        self.drive.get(recipe_url)
        time.sleep(3)

        # Extract basic data points
        title = self.driver.find_element(By.CSS_SELECTOR, '').text
        description = self.driver.find_element(By.CSS_SELECTOR, '').text
        ingredients = self.driver.find_element(By.CSS_SELECTOR, '').text
        instructions = self.driver.find_element(By.CSS_SELECTOR, '').text

        # Format ingredients and instructions
        ingredient_list = [ingredient.text for ingredient in ingredients]
        instruction_list = [instruction.text for instruction in instructions]

        # Return the data as a dictionary
        recipe_data = {
            'title': title,
            'description': description,
            'ingredients': ingredient_list,
            'instructions': instruction_list
        }

        return recipe_data

    def close(self):
        """Closes browser session"""
        self.driver.quit()
