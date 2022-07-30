from .data import PostEntry
import requests
import os
from typing import List, Union

def download_img(url: str, fname_dest: str):
    print("Downloading entry: %s from %s" % (fname_dest, url))

    img_data = requests.get(url).content
    with open(fname_dest, 'wb') as handler:
        handler.write(img_data)

def download_imgs_for_entry(entry: PostEntry, img_dirname: str):
    # Make directory
    if not os.path.isdir(img_dirname):
        os.makedirs(img_dirname)

    # Make directory for this article's images
    img_dirname_entry = os.path.join(img_dirname, entry.basename)
    if not os.path.isdir(img_dirname_entry):
        os.makedirs(img_dirname_entry)
    
    # Store
    entry.img_dirname = img_dirname

    # Download
    for img in entry.imgs:
        fname = os.path.join(img_dirname_entry, img.fname_wo_path)
        download_img(img.url, fname)

def download_imgs_from_md(entries: List[PostEntry], img_dirname: str, limit: Union[int,None] = 1):
    if limit == None:
        limit = len(entries)
    for entry in entries[:limit]:
        download_imgs_for_entry(entry, img_dirname)