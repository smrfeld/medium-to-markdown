from dataclasses import dataclass
import datetime
from typing import Union, List, Dict
import os

@dataclass
class PostImage:
    # URl
    url: str
    # Basename
    basename: str
    # Extension
    ext: str

    @classmethod
    def from_json(cls, d: Dict):
        return cls(
            url=d['url'],
            basename=d['basename'],
            ext=d['ext']
        )

    def to_json(self) -> Dict:
        return {
            'url': self.url,
            'basename': self.basename,
            'ext': self.ext
            }

@dataclass
class PostEntry:
    # Title
    title: str
    # Timestamp
    time: datetime.datetime
    # Human readable time
    time_human: str
    # Cover image index
    cover_img_idx: Union[int,None]
    # URL of the article
    url: str
    # Filename of the article
    fname: str
    # Images
    imgs: List[PostImage]
    # Summary
    summary: str

    @property
    def basename(self) -> str:
        # Remove extension
        return os.path.splitext(os.path.basename(self.fname))[0]
    
    @classmethod
    def from_json(cls, d: Dict):
        x = cls(
            title=d['title'],
            time=d['time'],
            summary=d['summary'],
            time_human=d['time_human'],
            cover_img_idx=None,
            url=d['url'],
            fname=d['fname'],
            imgs=[ PostImage.from_json(x) for x in d['imgs'] ]
            )
        
        if 'cover_img_idx' in d:
            x.cover_img_idx = d['cover_img_idx']
        
        return x

    def to_json(self):
        dat = {
            'title': self.title,
            'time': self.time,
            'time_human': self.time_human,
            'url': self.url,
            'fname': self.fname,
            'imgs': [ x.to_json() for x in self.imgs ],
            'basename': self.basename,
            'summary': self.summary
        }

        if self.cover_img_idx != None:
            dat['cover_img_idx'] = self.cover_img_idx

        return dat