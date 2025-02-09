import requests

LATEST_VERSION_URL = "https://github.com/arman-31/phone_webcam/releases/tag/phone_webcam_v1.1.exe"
DOWNLOAD_URL = "https://github.com/arman-31/phone_webcam/releases/download/v1.1/phone_webcam.exe"
CURRENT_VERSION = "1.0"

def check_for_update():
    response = requests.get(LATEST_VERSION_URL)
    latest_version = response.text.strip()

    if latest_version > CURRENT_VERSION:
        print(f"New version {latest_version} available! Downloading...")
        download_update()
    else:
        print("You're using the latest version.")

def download_update():
    response = requests.get(DOWNLOAD_URL, stream=True)
    with open("new_app.exe", "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)

    print("Update downloaded as 'new_app.exe'. Please install manually.")

check_for_update()
