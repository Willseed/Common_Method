# -*- coding: utf-8 -*-
import base64


def imageConvertBase64(filename):
    with open(filename, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
    return str


def base64Convertimage(imageStr, saveFilename):
    imgData = base64.b64decode(imageStr)
    with open(saveFilename, 'wb') as f:
        f.write(imgData)
