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
            caption="",
            ext=ext
            ))

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
        imgs=imgs
        )

def htmls_to_posts(fnames: List[str]) -> List[PostEntry]:
    return [x for x in [html_to_post(fname) for fname in fnames] if x != None]

'''
fnames = glob.glob('posts/*.html')

# Remove drafts
drafts = glob.glob('posts/draft*.html')
fnames = list(set(fnames) - set(drafts))

# Parse
data = []
for fname in fnames:
    data0 = parse(fname)
    if data0 != None:
        data.append(data0)

# Resize
os.system("cd img/blog && magick mogrify -resize 150x150 *.png")
os.system("cd img/blog && magick mogrify -resize 150x150 *.jpeg")
# os.system("cd img/blog && magick mogrify -resize 150x150 *.jpg")

data_yml = []
for i,d in enumerate(data):
    k = 'entry' + str(i)

    dat = { k: d.get_yaml() }
    data_yml.append(dat)

with open('blog.yml', 'w') as f:
    yaml.dump(data_yml, f)

print("Wrote blog.yml")
print("WARNING: YOU MUST REINDENT 4 -> 2 spaces in the yml file manually")
'''