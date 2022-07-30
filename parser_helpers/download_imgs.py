from .data import PostEntry
import requests
import os
from typing import List, Union
from dataclasses import dataclass

@dataclass
class Context:
    noentries: int
    ientry: int = 0
    iimage: int = 0
    noimages: int = 0

    @property
    def progress(self) -> str:
        return "(entry %04d/%04d) (img %02d/%02d)" % (self.ientry, self.noentries, self.iimage, self.noimages)

def download_img(url: str, fname_dest: str, c: Context):
    print("%s - downloading entry: %s from %s" % (c.progress, fname_dest, url))

    img_data = requests.get(url).content
    with open(fname_dest, 'wb') as handler:
        handler.write(img_data)

def download_imgs_for_entry(entry: PostEntry, img_dirname: str, c: Context):
    # Make directory
    if not os.path.isdir(img_dirname):
        os.makedirs(img_dirname)

    # Make directory for this article's images
    img_dirname_entry = os.path.join(img_dirname, entry.basename)
    if not os.path.isdir(img_dirname_entry):
        os.makedirs(img_dirname_entry)
    
    # Download
    c.noimages = len(entry.imgs)
    for c.iimage, img in enumerate(entry.imgs):
        fname = os.path.join(img_dirname_entry, img.fname_wo_path)
        download_img(img.url, fname, c)

def download_imgs_from_md(entries: List[PostEntry], img_dirname: str, limit: Union[int,None] = None):
    if limit == None:
        limit = len(entries)

    c = Context(noentries=limit)

    for c.ientry, entry in enumerate(entries[:c.noentries]):
        download_imgs_for_entry(entry, img_dirname, c)