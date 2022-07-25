from dataclasses import dataclass
import datetime
from typing import Union, List

@dataclass
class YMLImage:
    # URl
    url: str
    # Basename
    basename: str
    # Caption
    caption: str

    def get_yaml(self):
        return {
            'url': self.url,
            'basename': self.basename,
            'caption': self.caption
            }

@dataclass
class YMLEntry:
    # Title
    title: str
    # Timestamp
    time: datetime.datetime
    # Human readable time
    time_human: str
    # Cover image url
    cover_img_url: str
    # URL of the article
    url: str
    # Filename of the article
    fname: str
    # Images
    imgs: List[YMLImage]
    # Cover image fname if downloaded, else None
    cover_img_fname: Union[str,None] = None
    # Image directory if downloaded, else None
    img_dirname: Union[str,None] = None

    def get_yaml(self):
        dat = {
            'title': self.title,
            'time': self.time,
            'time_human': self.time_human,
            'cover_img_url': self.cover_img_url,
            'url': self.url,
            'fname': self.fname
        }

        if self.cover_img_fname != None:
            dat['cover_img_fname'] = self.cover_img_fname
        
        if self.img_dirname != None:
            dat['img_dirname'] = self.img_dirname

        return dat