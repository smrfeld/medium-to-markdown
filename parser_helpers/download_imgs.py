from .yml_entry import YMLEntry
import requests
import os
from typing import List

def download_img(url: str, fname_dest: str):
    print("Downloading entry: %s from %s" % (fname_dest, url))

    img_data = requests.get(url).content
    with open(fname_dest, 'wb') as handler:
        handler.write(img_data)

def download_imgs_for_entry(entry: YMLEntry, img_dirname: str):
    # Make directory
    if not os.path.isdir(img_dirname):
        os.makedirs(img_dirname)
    
    # Store
    entry.img_dirname = img_dirname

    # Download
    for img in entry.imgs:
        fname = os.path.join(img_dirname, img.basename)
        download_img(img.url, fname)

def download_imgs(entries: List[YMLEntry], img_dirname: str):
    for entry in entries:
        download_imgs_for_entry(entry, img_dirname)