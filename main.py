#pip install pillow
#pip install rembg
#pip install onnxruntime
#input=>open=>BgRemove=>output=>save

#Auto Import (Alt+Enter)

from  PIL import Image
from rembg import remove

#input
input_img='img.jpg'

#open
input_img_open=Image.open(input_img)

#BgRemove
output_img=remove(input_img_open)

#Save
output_img.save('output_img.png')

print("Process Completed......")

