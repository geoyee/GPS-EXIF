# GPS-EXIF

Writing / Reading GPS coordinates in photo's EXIF by Python.

## Install

```shell
pip install gpsexif
```

## APIs

- setGPS

```python
from gpsexif import setGPS


img_path = "input/tyg.jpg"  # use your image path
save_dir = "output"
loc = [114.353458, 30.53624997, 363.5164]
setGPS(img_path, loc, save_dir)
```

- getGPS

```python
from gpsexif import getGPS


img_path = "output/tyg.jpg"  # use your image path
loc = getGPS(img_path)
```
