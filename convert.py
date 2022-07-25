from parser_helpers import *


if __name__ == "__main__":

    fnames = get_fnames('posts')
    ymls = get_ymls(fnames)
    print(ymls)

    download_imgs(ymls, 'output')