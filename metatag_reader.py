# Works with Python 3.4 or higher
import os
from PIL import Image

# start with main
def main():
    path = "./images/unregistered/"

    files = os.listdir(path)
    filename = [f for f in files if os.path.isfile(os.path.join(path, f))]
    print(filename)

    im = Image.open(path + filename[0])
    im.load()
    print(im.info['parameters'])


if __name__ == '__main__':
    main()
