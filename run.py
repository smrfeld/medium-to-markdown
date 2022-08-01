from parser_helpers import *

import argparse
import os

def convert_html_to_md(args):
    html_fnames = get_fnames(args.posts_dir)
    posts = htmls_to_posts(html_fnames)

    if not os.path.isdir(args.output_dir):
        os.makedirs(args.output_dir)

    yml_fname = os.path.join(args.output_dir, '%s.yml' % args.output_name)
    write_posts_to_yml(posts, yml_fname)

    convert_posts_to_md(args.posts_dir, args.output_dir, args.md_dir, posts)

def resize_cover_imgs0(args):
    yml_fname = os.path.join(args.output_dir, '%s.yml' % args.output_name)
    posts = read_posts_from_yml(yml_fname)

    resize_cover_imgs(args.output_dir, args.img_dir, args.cover_img_resized_dir, posts, args.new_size)

def download_imgs(args, cover_img_only: bool):
    yml_fname = os.path.join(args.output_dir, '%s.yml' % args.output_name)
    posts = read_posts_from_yml(yml_fname)

    dir_name = os.path.join(args.output_dir, args.img_dir)
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    
    dl = Downloader()
    dl.download_imgs(posts, dir_name, cover_img_only)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Convert HTML files from Medium to markdown')
    parser.add_argument('command', choices=['convert', 'convert-html-to-md', 'download-all-imgs', 'download-cover-imgs', 'resize-cover-imgs'])

    parser.add_argument('--posts-dir', dest='posts_dir', type=str, default='posts',
                    help='Posts directory', required=False)
    parser.add_argument('--output-dir', dest='output_dir', default='output', type=str,
                    help='Output directory', required=False)
    parser.add_argument('--output-name', dest='output_name', default='posts', type=str,
                    help='Output name', required=False)
    parser.add_argument('--img-dir', dest='img_dir', default='img', type=str,
                help='Directory in which images are stored', required=False)
    parser.add_argument('--md-dir', dest='md_dir', default='md', type=str,
                help='Directory in which markdown are stored', required=False)
    parser.add_argument('--cover-img-resized-dir', dest='cover_img_resized_dir', default='cover_img_resized', type=str,
                help='Directory in which resized cover images are stored.', required=False)
    parser.add_argument('--new-size', dest='new_size', default=150, type=int,
                help='The new size to resize images to.', required=False)

    args = parser.parse_args()

    if args.command == 'convert':
        convert_html_to_md(args)
        download_imgs(args, cover_img_only=True)
        resize_cover_imgs0(args)
    elif args.command == 'convert-html-to-md':
        convert_html_to_md(args)
    elif args.command == 'resize-cover-imgs':
        resize_cover_imgs0(args)
    elif args.command == 'download-all-imgs':
        download_imgs(args, False)
    elif args.command == 'download-cover-imgs':
        download_imgs(args, True)
    else:
        raise ValueError("Command: %s not recognized" % args.command)