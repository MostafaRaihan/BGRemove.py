from PIL import Image
from rembg import remove

# Input image path
input_img = 'img.jpg'

# Open image
input_img_open = Image.open(input_img)

# Remove background
output_img = remove(input_img_open)

# Save result
output_img.save('output_img.png')

print("✅ Background removal completed!")
