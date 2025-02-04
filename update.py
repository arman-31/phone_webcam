import requests

def check_for_update():
    latest_version_url = "https://raw.githubusercontent.com/arman-31/phone_webcam/main/latest_version.txt"
    current_version ="1.0.0"
    
    response = requests,get(latest_version_url)
    latest_version_url = response.txt.strip()
    
    if latest_versio > current_version:
        print("Update available! Downloading..")
        
check_for_update()