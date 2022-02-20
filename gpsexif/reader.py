import piexif
import numpy as np
from PIL import Image


def getGPSfromImage(img_path):
    img = Image.open(img_path)
    if isinstance(img.info, dict):
        exif_dict = piexif.load(img.info["exif"])
        gps = exif_dict["GPS"]
        lon = __dict2Loc(gps[2]) * (1 if gps[1] == b"N" else -1)
        lat = __dict2Loc(gps[4]) * (1 if gps[3] == b"E" else -1)
        alt = gps[6][0] / gps[6][1] * (1 if gps[5] == 0 else -1)
        return np.array([lat, lon, alt])
    else:
        raise EXIFError("This photo has not EXIF!")


class EXIFError(Exception):
    def __init__(self, str):
        self.str = str
    def __str__(self):
        print(self.str)


def __dict2Loc(dct):
    D = dct[0][0] / dct[0][1]
    F = dct[1][0] / dct[1][1]
    M = dct[2][0] / dct[2][1]
    loc = D + F / 60 + M / 3600
    return loc


if __name__ == "__main__":
    img_path = "output/tyg.jpg"
    print(getGPSfromImage(img_path))