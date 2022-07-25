from parser_helpers import *


if __name__ == "__main__":

    output_dir = 'output'

    fnames = get_fnames('posts')
    ymls = extract_ymls(fnames)
    print(ymls)

    yml_fname = os.path.join(output_dir, 'blog.yml')
    write_ymls(ymls, yml_fname)

    # download_imgs(ymls, 'output')