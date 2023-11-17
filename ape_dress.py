from PIL import Image, ImageFilter
import requests
from io import BytesIO
import sys

def download_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image

def overlay_images(base_image, overlay_image_path):
    overlay = Image.open(overlay_image_path)

    # resize overlay image to match the base image size
    overlay = overlay.resize(base_image.size, Image.Resampling.LANCZOS)

    # place the overlay image on top of the base image
    base_image.paste(overlay, (0, 0), overlay)
    
    return base_image

def main(image_number):
    # urls and/or paths to the images 
    base_image_url = "https://ipfs.io/ipfs/QmQ6VgRFiVTdKbiebxGvhW3Wa3Lkhpe6SkWBPjGnPkTttS/" + image_number + ".png"
    overlay_image_path = "hoodies/ape_hoodie.png"  

    # download the base image
    base_image = download_image(base_image_url)

    # overlay images
    final_image = overlay_images(base_image, overlay_image_path)

    # display the image
    # final_image.show()

    # save the image
    final_image.save("dressed_up_image.png")    


if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_number = sys.argv[1]
        main(image_number)
    else:
        print("Please provide an image number as a command line argument.")
        print("Example: python3 ape_dress.py 2450")