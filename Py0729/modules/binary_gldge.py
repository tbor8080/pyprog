from PIL import Image, ImageOps
import base64

file='python-logo-master-v3-TM_sample.png'

g_text = base64.encodebytes(open(file, "rb").read())
# print(g_text)
glitched_image = base64.decodebytes(g_text.replace(b"0",b"1")) #0を1に書き変える
open("glitched.png", "wb").write(glitched_image)