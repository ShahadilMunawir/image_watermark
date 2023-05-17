from PIL import Image, ImageDraw

source_image = Image.open('6836718.png')
watermark_image = Image.open('setting.png')

watermark_size = (200, 200)
watermark_image = watermark_image.resize(watermark_size, Image.ANTIALIAS)

result_image = Image.new('RGBA', source_image.size)
result_image.paste(source_image, (0, 0))

position = (result_image.width - watermark_image.width - 30, result_image.height - watermark_image.height - 30)
result_image.paste(watermark_image, position, watermark_image)

result_image.save('result_image.png')
