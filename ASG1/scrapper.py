from playwright.sync_api import sync_playwright

# Using 'with' is best practice because it cleans up memory automatically
with sync_playwright() as p:
    print("Launching browser...")
    browser = p.chromium.launch(headless=False)
    
    print("Opening new page...")
    page = browser.new_page()
    
    # Let's actually navigate somewhere so you can see it working!
    page.goto("https://shopee.com.my")
    
    # THIS IS THE MAGIC LINE:
    # It freezes the Python script until you interact with the terminal
    input("The browser is now open! Press ENTER in this terminal to close it...")
    
    print("Closing browser...")
    browser.close()