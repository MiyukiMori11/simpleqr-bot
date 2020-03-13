import pyqrcode
import random


def generate(text):
    qr_txt = pyqrcode.create(text, encoding='utf-8')
    name = random.randint(10000, 99999)
    qr_txt.png(f"{name}.png", scale=8)
    return f"{name}.png"
