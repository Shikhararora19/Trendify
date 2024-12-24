from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

gecko_driver_path = "/Users/shikhararora/Downloads/geckodriver"
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

# Function to scrape Google Trends
def scrape_google_trends():
    print("\n[Google Trends]")
    try:
        driver.get("https://trends.google.com/trends/trendingsearches/daily?geo=US")
        
        # Scroll down to ensure the content is loaded
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait for the rows in the table to load
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr"))
        )
        
        # Select all rows in the table body
        rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        if rows:
            for row in rows:  # Iterate through all rows
                try:
                    # Find all divs inside the second cell of the row
                    trend_elements = row.find_elements(By.CSS_SELECTOR, "td:nth-child(2) div")
                    for trend_element in trend_elements:
                        print(trend_element.text.strip())  # Print each trend
                except Exception as cell_error:
                    print(f"Error extracting data for a row: {cell_error}")
        else:
            print("No trends found. Check the updated website structure.")
    except Exception as e:
        print(f"Error scraping Google Trends: {e}")
        # Save the page source for debugging
        with open("google_trends_debug.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)


def scrape_reddit():
    print("\n[Reddit Trends]")
    try:
        driver.get("https://www.reddit.com/r/all/")
        
        # Wait for posts to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[slot='title']"))
        )
        
        # Find all post titles using the slot attribute
        posts = driver.find_elements(By.CSS_SELECTOR, "a[slot='title']")
        
        if posts:
            for post in posts[:10]:  # Limit to the first 10 posts
                print(post.text.strip())
        else:
            print("No Reddit posts found. Check the updated structure.")
    except Exception as e:
        print(f"Error scraping Reddit: {e}")


def scrape_youtube():
    print("\n[YouTube Trends]")
    try:
        driver.get("https://www.youtube.com/feed/trending")
        time.sleep(5)
        titles = driver.find_elements(By.CSS_SELECTOR, "a#video-title")
        for title in titles[:10]:
            print(title.text.strip())
    except Exception as e:
        print(f"Error scraping YouTube: {e}")
        with open("youtube_debug.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

def scrape_bbc():
    print("\n[BBC News Trends]")
    try:
        driver.get("https://www.bbc.com/news")
        time.sleep(5)
        WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3.gs-c-promo-heading__title"))
        )
        headlines = driver.find_elements(By.CSS_SELECTOR, "h3.gs-c-promo-heading__title")
        for headline in headlines[:10]:
            print(headline.text.strip())
    except Exception as e:
        print(f"Error scraping BBC News: {e}")
        with open("bbc_debug.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

def main():
    scrape_google_trends()
    scrape_reddit()
    scrape_youtube()
    scrape_bbc()
    driver.quit()

if __name__ == "__main__":
    main()
