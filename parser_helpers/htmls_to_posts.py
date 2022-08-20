from .data import PostEntry, PostImage

from bs4 import BeautifulSoup
from typing import Union, List
import unidecode
import glob
import os

def get_fnames(posts_dir: str, ignore_drafts: bool = True) -> List[str]:
    
    # HTML
    glob_str = os.path.join(posts_dir, '*.html')
    fnames = glob.glob(glob_str)

    # Remove drafts
    if ignore_drafts:
        drafts = glob.glob('posts/draft*.html')
        fnames = list(set(fnames) - set(drafts))

    return fnames

def html_to_post(html_fname: str) -> Union[PostEntry,None]:    

    # Read file
    with open(html_fname,"r") as f:
        content = f.read()

    # Parse HTML
    soup = BeautifulSoup(content, 'lxml')

    # Skip incomplete articles
    if soup.title == None or soup.time == None or soup.img == None:
        return None

    # Extract info
    title = unidecode.unidecode(soup.title.text)
    time = soup.time['datetime']
    time_human = soup.time.text
    cover_img_url = soup.img['src']

    # Get the url
    links = soup.find_all("a", {"class": "p-canonical"})
    if len(links) > 0:
        url = links[0]['href']
    else:
        url = "https://medium.com/@oliver-k-ernst"

    # Get img urls
    img_entries = soup.find_all("img")
    imgs = []
    for entry in img_entries:
        basename, ext = os.path.splitext(entry['data-image-id'])
        imgs.append(PostImage(
            basename=basename, 
            url=entry['src'], 
            ext=ext
            ))

    summary = soup.find("section", {"data-field": "subtitle"}).text.strip()

    cover_img = [ img for img in imgs if img.url == cover_img_url ]
    if len(cover_img) > 0:
        cover_img = cover_img[0]
        cover_img_idx = imgs.index(cover_img)
    else:
        cover_img_idx = None

    # Construct yml data
    return PostEntry(
        title=title, 
        time=time, 
        time_human=time_human,
        cover_img_idx=cover_img_idx,
        url=url,
        fname=html_fname,
        imgs=imgs,
        summary=summary
        )

def htmls_to_posts(fnames: List[str]) -> List[PostEntry]:
    return [x for x in [html_to_post(fname) for fname in fnames] if x != None]