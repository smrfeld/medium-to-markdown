from .yml_entry import YMLEntry, YMLImage

from bs4 import BeautifulSoup
from typing import Union, List
import unidecode

def parse_yml(fname: str) -> Union[YMLEntry,None]:    

    # Read file
    with open(fname,"r") as f:
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
        imgs.append(YMLImage(
            basename=entry['data-image-id'], 
            url=entry['src'], 
            caption=""
            ))

    # Construct yml data
    return YMLEntry(
        title=title, 
        time=time, 
        time_human=time_human,
        cover_img_url=cover_img_url,
        url=url,
        fname=fname,
        imgs=imgs
        )

def get_ymls(fnames: List[str]) -> List[YMLEntry]:
    return [x for x in [parse_yml(fname) for fname in fnames] if x != None]

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