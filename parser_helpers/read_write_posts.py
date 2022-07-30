from .data import PostEntry

from typing import List
import yaml

def write_posts_to_yml(posts: List[PostEntry], yml_fname: str):
    data_yml = [ d.to_json() for d in posts ]
    with open(yml_fname, 'w') as f:
        yaml.dump(data_yml, f)

def read_posts_from_yml(yml_fname: str) -> List[PostEntry]:
    with open(yml_fname, 'r') as f:
        res = yaml.safe_load(f)

    return [ PostEntry.from_json(d) for d in res ]