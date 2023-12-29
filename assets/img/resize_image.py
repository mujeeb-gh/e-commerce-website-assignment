from PIL import Image

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img = img.resize(size)
        img.save(output_path)




resize_image("jpg/featured2.jpg", "output.jpg", (400, 594))
