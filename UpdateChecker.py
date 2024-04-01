import requests
import time
# Replace 'YOUR_CURRENT_VERSION' with the actual version number of your software
YOUR_CURRENT_VERSION = "your-current-version-in-numbers"

# Function to check for updates
def check_for_updates():
    # URL of the auto-updater.txt file on your website
    url = "https://yoursite.com/update-checker.txt"

    try:
        # Fetch the content of the file
        response = requests.get(url)
        content = response.text
        
        # Extract the current version number
        current_version = content.split('=')[1].strip().strip('"')

        # Compare current version with the version of your software
        if current_version != YOUR_CURRENT_VERSION:
            # Notify the user about the update
            
            print("There's an update.") 
            time.sleep(10)
        else:
            print("Up To Date.")

    except Exception as e:
        print("Error occurred while checking for updates:", e)

# Call the function to check for updates
check_for_updates()

