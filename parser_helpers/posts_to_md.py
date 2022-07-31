from .data import PostEntry

from markdownify import MarkdownConverter
from typing import List
import os

from bs4 import BeautifulSoup

# Function to remove tags
def remove_tags(html):
  
    # parse html content
    soup = BeautifulSoup(html, "html.parser")
  
    for data in soup(['style']):
        # Remove tags
        data.decompose()
  
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)

INVALID_TAGS = ['style']

def sanitize_html(value):

    soup = BeautifulSoup(value, features="lxml")

    for tag in soup.findAll(True):
        if tag.name in INVALID_TAGS:
            tag.extract()

    return soup.renderContents()

class Converter(MarkdownConverter):
    # def convert_img(self, el, text, convert_as_inline):
    #     return super().convert_img(el, text, convert_as_inline) + '\n\n'
    pass

def to_md(html, **options):
    return Converter(**options).convert(html)

def convert_posts_to_md(posts_dir: str, output_dir: str, md_dir: str, posts: List[PostEntry]):

    dir_write = os.path.join(output_dir, md_dir)
    if not os.path.isdir(dir_write):
        os.makedirs(dir_write)

    for post in posts:
        
        # Read html
        fname = os.path.join(posts_dir, post.basename + ".html")
        with open(fname, 'r') as f:
            html = f.read()

        # Sanititze
        html = sanitize_html(html)

        # Convert
        strip = ['style']
        md = to_md(html, strip=strip)

        # Write
        fname = os.path.join(dir_write, post.basename + ".md")
        with open(fname, 'w') as f:
            f.write(md)