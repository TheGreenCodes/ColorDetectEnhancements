from colordetect import ColorDetect

# parse the image.
flowers = ColorDetect('./images/flowers.jpg')

flowers.get_color_count()

flowers.write_color_count(font_color=(0,0,255), top_margin=40)

flowers.save_image(location='./images', file_name='processed.jpg')

