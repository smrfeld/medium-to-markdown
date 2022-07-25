from typing import List
import os
import glob

def get_fnames(posts_dir: str, ignore_drafts: bool = True) -> List[str]:
    
    # HTML
    glob_str = os.path.join(posts_dir, '*.html')
    fnames = glob.glob(glob_str)

    # Remove drafts
    if ignore_drafts:
        drafts = glob.glob('posts/draft*.html')
        fnames = list(set(fnames) - set(drafts))

    return fnames
