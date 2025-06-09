import os
import json
import requests

def extract_images(json_file):
    """
    Extracts images from a JSON file and saves them to folders named after verification numbers.

    Args:
        json_file (str): Path to the JSON file.
    """
    with open(json_file, 'r') as f:
        data = json.load(f)

        for entry in data:
            process_entry(entry)

def process_entry(entry):
    verification_number = entry["appmartVerificationNumber"]
    bvn_image_url = entry["bvnImage"]
    verification_image_url = entry["verificationImage"]

    # Create folder for the entry
    folder_name = os.path.join(os.getcwd(), verification_number)
    os.makedirs(folder_name, exist_ok=True)

    # Download and save BVN image
    image_filename = os.path.join(folder_name, "bvn_image.jpg")
    download_image(bvn_image_url, image_filename)

    # Download and save verification image
    image_filename = os.path.join(folder_name, "verification_image.png")
    download_image(verification_image_url, image_filename)

def download_image(url, filename):
    """
    Downloads an image from a URL and saves it to a file.

    Args:
        url (str): URL of the image.
        filename (str): Path to save the image.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Image downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image from {url}: {e}")

if __name__ == "__main__":
    json_file = "new.json"  # Replace with your actual JSON file path
    extract_images(json_file)