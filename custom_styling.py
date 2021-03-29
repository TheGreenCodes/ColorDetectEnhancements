from colordetect import ColorDetect

# parse the image.
flowers = ColorDetect('./images/flowers.jpg')

flowers.get_color_count(color_format="human_readable")

flowers.write_color_count(top_margin=40)

flowers.save_image(location='./images', file_name='processed-human-image.jpg')

