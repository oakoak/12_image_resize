# Image Resizer

---
This script resizes the image to the ones you need
---

## Description
+ Script resize image to the specified parameter
+ Unless you specify the path to the destination file, it will be saved by template *"path to image"__height x width."format""*
+ If you enter only one parameter, then the second one will be set so that the aspect ratio does not change


## How using
```bash
python image_resize.py <path to image> <path to new image> --height  1000 --width 1000
```
or 
```bash
python image_resize.py <path to image> --height 1000
```

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
