import os
import math
import time
import piexif
import numpy as np
from PIL import Image


def setGPSinImage(img_path, loc, save_dir="output"):
    file_name = img_path.split("/")[-1]
    ext = "PNG" if file_name.split(".")[-1] == "png" else "JPEG"
    img = Image.open(img_path)
    if isinstance(loc, (list, dict, np.ndarray)):
        if len(loc) >= 2 and len(loc) <= 3:
            lat_sym = b"N" if loc[1] > 0 else b"S"
            lat = __loc2Dict(loc[1])
            lon_sym = b"E" if loc[0] > 0 else b"W"
            lon = __loc2Dict(loc[0])
            if len(loc) == 3:
                alt_sym = 0 if loc[2] >= 0 else 1
                alt = (int(1000 * loc[2]), 1000)
            else:
                alt_sym = 0
                alt = (0, 1000)
        else:
            raise ValueError("The loc's lenght must be 2/3!")
        b7, b29 = __getTime()
        gps_dict = {
            "GPS": {
                1: lat_sym,
                2: lat,
                3: lon_sym,
                4: lon,
                5: alt_sym,
                6: alt,
                7: b7,
                29: b29
            }
        }
        exif_bytes = piexif.dump(gps_dict)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        save_path = os.path.join(save_dir, file_name)
        img.save(save_path, ext, exif=exif_bytes)
        print(save_path, "write GPS EXIF successfully!")
    else:
        raise ValueError("The loc must be list/dict/ndarray!")


def __loc2Dict(loc):
    D = math.floor(loc)
    F, M = divmod((loc - D) * 60, 1)
    M *= 60
    dct = ((int(D), 1), (int(F), 1), (int(10000 * M), 10000))
    return dct


def __getTime():
    HMS = str(time.strftime("%H,%M,%S", time.localtime())).split(",")
    b7 = ((int(HMS[0]), 1), (int(HMS[1]), 1), (int(HMS[2]), 1))
    b29 =  str(time.strftime("%Y:%m:%d", time.localtime())).encode("utf8")
    return b7, b29


if __name__ == "__main__":
    img_path = "input/tyg.jpg"
    loc = [114.353458, 30.53624997, 363.5164]
    setGPSinImage(img_path, loc)