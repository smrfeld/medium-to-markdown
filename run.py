from parser_helpers import *

import argparse
import os

def convert(args):
    html_fnames = get_fnames(args.posts_dir)
    posts = htmls_to_posts(html_fnames)
    print(posts)

    yml_fname = os.path.join(args.output_dir, '%s.yml' % args.output_name)
    write_posts_to_yml(posts, yml_fname)

def resize_imgs(args):
    yml_fname = os.path.join(args.output_dir, '%s.yml' % args.output_name)
    posts = read_posts_from_yml(yml_fname)

    os.system("cd img/blog && magick mogrify -resize 150x150 *.png")
    os.system("cd img/blog && magick mogrify -resize 150x150 *.jpeg")
    # os.system("cd img/blog && magick mogrify -resize 150x150 *.jpg")

def download_imgs(args):
    yml_fname = os.path.join(args.output_dir, '%s.yml' % args.output_name)
    posts = read_posts_from_yml(yml_fname)

    # Downloadßß
    dir_name = os.path.join(args.output_dir, 'img')
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    download_imgs(posts, 'output')

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Convert HTML files from Medium to markdown')
    parser.add_argument('command', choices=['convert', 'download-imgs', 'resize-imgs'])

    parser.add_argument('--posts-dir', dest='posts_dir', type=str, default='posts',
                    help='Posts directory', required=False)
    parser.add_argument('--output-dir', dest='output_dir', default='output', type=str,
                    help='Output directory', required=False)
    parser.add_argument('--output-name', dest='output_name', default='posts', type=str,
                    help='Output name', required=False)
    parser.add_argument('--no-download-imgs', dest='no_download_imgs', default=False, type=bool,
                    help='Used in the convert command; if included, does not download images as part of the command.', required=False)
    
    args = parser.parse_args()

    if args.command == 'convert':
        convert(args)
        #if not args.no_download_imgs:
        #    download_imgs()
    else:
        if args.command == 'resize-imgs':
            resize_imgs(args)
        elif args.command == 'download-imgs':
            download_imgs(args)
        else:
            raise ValueError("Command: %s not recognized" % args.command)