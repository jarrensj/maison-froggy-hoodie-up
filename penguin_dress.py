from PIL import Image, ImageFilter
import requests
from io import BytesIO

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

# urls and/or paths to the images 
base_image_url = "https://ipfs.io/ipfs/QmNf1UsmdGaMbpatQ6toXSkzDpizaGmC9zfunCyoz1enD5/penguin/3420.png"
overlay_image_path = "penguin_hoodie.png"  

# download the base image
base_image = download_image(base_image_url)

# overlay images
final_image = overlay_images(base_image, overlay_image_path)

# display the image
# final_image.show()

# save the image
final_image.save("dressed_up_image.png")
