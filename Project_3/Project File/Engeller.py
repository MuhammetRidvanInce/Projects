
import os
from PIL import Image
import numpy as np


class Engel():
    def __init__(self, size):
        self.size = size
        self.original_images = []
        for file in os.listdir("original_images"):
            if os.path.isfile(os.path.join("original_images", file)):
                self.original_images.append(file)

        self.engel_cesitleri = {}
        for image in self.original_images:
            img = Image.open("original_images\{}".format(image))
            img = img.resize((self.size, self.size))
            value = image.split(".")[0]
            boyut = np.array([int((image[:3])[0]), int((image[:3])[2])])
            id = value[-1]
            img.save("resize_images\{}.gif".format(value), optimize=True)
            self.engel_cesitleri["resize_images\{}.gif".format(
                value)] = (boyut, int(id))
