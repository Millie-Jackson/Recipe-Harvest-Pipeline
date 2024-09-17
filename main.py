from scraper import RecipeScraper
import json



def main():
    # Initialize scrapers for each website
    pick_up_limes_scraper = RecipeScraper('https://www.pickuplimes.com')
    avant_garde_vegan_scraper = RecipeScraper('https://www.gazoakleychef.com')
    rainbow_plant_life_scraper = RecipeScraper('https://www.rainbowplantlife.com')

    # List to store all recipe data
    all_recipes = []

    # Define a list of scrapers to iterate through
    scrapers = [
        pick_up_limes_scraper,
        avant_garde_vegan_scraper,
        rainbow_plant_life_scraper
    ]

    # Step 1: Get list of recipe links for each website
    for scraper in scrapers:
        recipe_links = scraper.get_recipe_links()

        # Step 2: Scrape each recipe
        for link in recipe_links:
            recipe_data = scraper.scrape_recipe(link)
            all_recipes.append(recipe_data)

    print("First 3 recipes:")
    for recipe in all_recipes[:3]:
        print(recipe)
    
    print("\nTotal number of recipes scraped:", len(all_recipes))

    # Step 3: Store recipes in a file
    with open('recipes.json', 'w') as f:
        json.dump(all_recipes, f, indent=3)

    # Close all scrapers
    for scraper in scrapers:
        scraper.close()



if __name__=="__main__":
    main()