from .data import PostEntry
import requests
import os
from typing import List, Union
from dataclasses import dataclass

@dataclass
class Downloader:
    noentries: int = 0
    ientry: int = 0
    iimage: int = 0
    noimages: int = 0

    def download_imgs(self, entries: List[PostEntry], img_dirname: str, cover_img_only: bool, limit: Union[int,None] = None):
        if limit == None:
            limit = len(entries)
        self.noentries = limit

        for self.ientry, entry in enumerate(entries[:self.noentries]):
            self._download_imgs_for_entry(entry, img_dirname, cover_img_only)

    @property
    def progress(self) -> str:
        return "(entry %04d/%04d) (img %02d/%02d)" % (self.ientry, self.noentries, self.iimage, self.noimages)

    def _download_img(self, url: str, fname_dest: str):
        print("%s - downloading entry: %s from %s" % (self.progress, fname_dest, url))

        img_data = requests.get(url).content
        with open(fname_dest, 'wb') as handler:
            handler.write(img_data)

    def _download_imgs_for_entry(self, entry: PostEntry, img_dirname: str, cover_img_only: bool):
        # Download
        if cover_img_only:
            if entry.cover_img_idx == None:
                return
            imgs_to_download = [entry.imgs[entry.cover_img_idx]]
        else:
            imgs_to_download = entry.imgs

        # Make directory
        if not os.path.isdir(img_dirname):
            os.makedirs(img_dirname)

        # Make directory for this article's images
        img_dirname_entry = os.path.join(img_dirname, entry.basename)
        if not os.path.isdir(img_dirname_entry):
            os.makedirs(img_dirname_entry)

        # Download
        self.noimages = len(imgs_to_download)
        for self.iimage, img in enumerate(imgs_to_download):
            fname = os.path.join(img_dirname_entry, img.basename + img.ext)
            self._download_img(img.url, fname)