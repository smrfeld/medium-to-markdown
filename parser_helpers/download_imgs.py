from yml_entry import YMLEntry
import requests
import os

def download_img(url: str, fname_dest: str):
    print("Downloading entry: %s from %s" % (fname_dest, url))

    img_data = requests.get(url).content
    with open(fname_dest, 'wb') as handler:
        handler.write(img_data)

def download_imgs(entry: YMLEntry, img_dirname: str):
    # Make directory
    if not os.path.isdir(img_dirname):
        os.makedirs(img_dirname)
    
    # Store
    entry.img_dirname = img_dirname

    # Download
    fname = os.path.join(img_dirname, img.basename)
    for img in entry.imgs:
        download_img(img.url, img_dirname)