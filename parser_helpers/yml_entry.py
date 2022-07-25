from dataclasses import dataclass
import datetime
from typing import Union, List
import os

@dataclass
class YMLImage:
    # URl
    url: str
    # Filename without the path
    fname_wo_path: str
    # Caption
    caption: str

    def get_yaml(self):
        return {
            'url': self.url,
            'basename': self.fname_wo_path,
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
    # Image directory if downloaded, else None
    img_dirname: Union[str,None] = None

    @property
    def basename(self) -> str:
        # Remove extension
        return os.path.splitext(os.path.basename(self.fname))[0]

    # Cover image fname if downloaded, else None
    @property
    def cover_img_fname_wo_path(self) -> Union[str,None]:
        if self.img_dirname == None:
            return None
        img = [x for x in self.imgs if x.url == self.cover_img_url][0]
        return img.fname_wo_path

    @property
    def cover_img_fname(self) -> Union[str,None]:
        fname_wo_path = self.cover_img_fname_wo_path
        if fname_wo_path == None:
            return None
        return os.path.join(self.img_dirname, fname_wo_path)

    def get_yaml(self):
        dat = {
            'title': self.title,
            'time': self.time,
            'time_human': self.time_human,
            'cover_img_url': self.cover_img_url,
            'url': self.url,
            'fname': self.fname,
            'imgs': [ x.get_yaml() for x in self.imgs ]
        }

        if self.cover_img_fname != None:
            dat['cover_img_fname'] = self.cover_img_fname
        
        if self.cover_img_fname_wo_path != None:
            dat['cover_img_fname_wo_path'] = self.cover_img_fname_wo_path

        if self.img_dirname != None:
            dat['img_dirname'] = self.img_dirname

        return dat