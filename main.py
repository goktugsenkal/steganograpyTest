from PIL import Image


# example usage
# image_path = "example_image.png"
# image = open_image(image_path)
def open_image(image_path):
    try:
        image = Image.open(image_path)

        if image.mode != 'RGB':
            image = image.convert('RGB')
            print("Converting image to RGB")

        print("Image opened: {}".format(image_path))
        print("Image size: {}".format(image.size))
        print("Image mode: {}".format(image.mode))

        return image

    except Exception as e:
        print("Error opening image: {}".format(e))
