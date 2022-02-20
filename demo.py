import os
from gpsexif import setGPS, getGPS


img_path = "input/tyg.jpg"  # use your image path
save_dir = "output"
loc = [114.353458, 30.53624997, 363.5164]
setGPS(img_path, loc, save_dir)
img_path = os.path.join(save_dir, img_path.split("/")[-1])
print(getGPS(img_path))