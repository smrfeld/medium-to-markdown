# Medium to markdown

Convert your medium articles from their `html` format to `markdown`. A deep copy of your data can be made, including images.

## Usage

1. Go to your medium account and request a copy of your data.

2. Look for the `posts` directory where your articles are located in `html` format.

3. Execute:
    ```
    python run.py convert --posts-dir <PATH_TO_POSTS> --output-dir <DESIRED_OUTPUT_DIRECTORY>
    ```
    to convert the posts into the output directory in Markdown format.

    The default posts directory is `posts` and the default output directory is `output`.
    
    The `convert` command executes the following commands:
    ```
    convert_html_to_md(args)
    download_imgs(args, cover_img_only=True)
    resize_cover_imgs0(args)
    ```
    i.e.
    1. Converts HTML in the `posts` directory to markdown
    2. Downloads the cover images
    3. Resizes the cover images

    You can also run the commands independently:
    ```
    python run.py convert-html-to-md
    python run.py download-cover-imgs
    python run.py resize-cover-imgs
    ```
    To see a full list of options:
    ```
    python run.py -h
    ```

## Example

An example input and output are located in the `example` directory.