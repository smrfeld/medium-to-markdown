from .data import PostEntry

import os
import glob
from typing import List

def run_command(command: str):
    # print("Executing: %s" % command)
    os.system(command)

def resize_cover_imgs(
    output_dir: str, 
    img_dirname: str, 
    img_resized_dirname: str, 
    posts: List[PostEntry],
    new_size: int
    ):

    img_dir = os.path.join(output_dir, img_dirname)
    img_resized_dir = os.path.join(output_dir, img_resized_dirname)

    # Make dir
    if not os.path.isdir(img_resized_dir):
        os.makedirs(img_resized_dir)

    # Go through posts
    for post in posts:
        if post.cover_img_idx == None:
            continue
        
        # Images
        img0 = post.imgs[post.cover_img_idx].basename + post.imgs[post.cover_img_idx].ext
        img = os.path.join(img_dir, post.basename, img0)
        img_resized = os.path.join(img_resized_dir, post.basename, img0)

        if not os.path.isfile(img):
            continue

        # Make directory
        post_dir = os.path.join(img_resized_dir, post.basename)
        if not os.path.isdir(post_dir):
            os.makedirs(post_dir)

        # Copy image
        run_command("cp %s %s" % (img, img_resized))

        # Resize
        run_command("magick mogrify -resize %dx%d %s" % (new_size, new_size, img_resized))