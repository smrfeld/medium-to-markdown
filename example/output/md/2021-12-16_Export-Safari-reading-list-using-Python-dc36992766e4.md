
Export Safari reading list using Python

Export Safari reading list using Python
=======================================




Clean up your teeming reading list.




---

### Export Safari reading list using Python

Clean up your teeming reading list.

<img class="graf-image" data-height="720" data-image-id="1*smDbzU8vO2mMObcS0jx03g.jpeg" data-is-featured="true" data-width="960" src="https://cdn-images-1.medium.com/max/800/1*smDbzU8vO2mMObcS0jx03g.jpeg"/>

<figcaption class="imageCaption">Image credit: author (Oliver K. Ernst)</figcaption>

[Here is the GitHub repo. with the script.](https://github.com/smrfeld/export-safari-reading-list)

If you are like me, your reading list is overflowing. Mine is over 1000+ entries. I use it daily to quickly remind myself of useful websites I’ve found, but I never bother to clean it up after those sites have used their purpose.

I didn’t want to clean it up manually by clicking through 1000+ items with a mouse is tedious. There is a shortcut to remove all items, but before doing that I wanted to export the data.

<img class="graf-image" data-height="715" data-image-id="1*XkSxG3aHOIeHmFSD8heXCw.png" data-width="1572" src="https://cdn-images-1.medium.com/max/800/1*XkSxG3aHOIeHmFSD8heXCw.png"/>

<figcaption class="imageCaption">JSON exported reading list.</figcaption>

<img class="graf-image" data-height="229" data-image-id="1*mLvsKlqXiUfUcVY7kzkm9A.png" data-width="1521" src="https://cdn-images-1.medium.com/max/800/1*mLvsKlqXiUfUcVY7kzkm9A.png"/>

<figcaption class="imageCaption">CSV exported reading list.</figcaption>

Here’s how it’s done.



---

Your reading list is stored in `~/Library/Safari/Bookmarks.plist` (at least, in Mac `11.4` Big Sur it is). Additionally, icons for the reading list are stored in `~/Library/Safari/ReadingListArchives` .

To read the `.plist` file format in Python, it is easiest to use the [plistlib](https://docs.python.org/3/library/plistlib.html) library:


```
pip install plistlib
```


---

### The complete script

Here is the complete script — the explanation is below:

[**export-safari-reading-list/export\_reading\_list.py at main · smrfeld/export-safari-reading-list**  
github.com](https://github.com/smrfeld/export-safari-reading-list/blob/main/export_reading_list.py "https://github.com/smrfeld/export-safari-reading-list/blob/main/export_reading_list.py")

### Usage

#### Basic usage:

* Export to CSV:


```
python export\_reading\_list.py csv reading\_list.csv
```
will write the reading list to `reading_list.csv`.

* Export to JSON:


```
python export\_reading\_list.py json reading\_list.json
```
will write the reading list to `reading_list.json`.

#### Options:

* Also copy the reading list icons:


```
python export\_reading\_list.py csv reading\_list.csv — dir-icons-out reading\_list\_icons
```
copies the icons to the folder `reading_list_icons`. They match up to the entries through the `WebBookmarkUUID` key.

* Specify the source directory for the icons:


```
python export\_reading\_list.py csv reading\_list.csv — dir-icons ~/Library/Safari/ReadingListArchives
```
The default is `~/Library/Safari/ReadingListArchives`.

* Specify the source directory for the reading list `.plist` file:


```
python export\_reading\_list.py csv reading\_list.csv — fname-bookmarks ~/Library/Safari/Bookmarks.plist
```
The default is `~/Library/Safari/Bookmarks.plist`.

* Include cached data for the websites:


```
python export\_reading\_list.py csv reading\_list.csv — include-data
```
The data is written to the `Data` field. The default is the`--exclude-data` option, which excludes the data.



---

### Explanation of the script

First, copy the `plist` file for safety:

<script src="https://gist.github.com/smrfeld/803aa0684a3019bbd7cfe9d64a502c3a.js"></script>

Next, find reading list elements in this terribly formatted dictionary:

<script src="https://gist.github.com/smrfeld/ec78f0a078842e1e60849e0ede1d3a29.js"></script>

Convert the reading list dictionaries to custom objects:

<script src="https://gist.github.com/smrfeld/54d38e3dfdec72b1b8e5553448353098.js"></script>

Finally, dump the entries to JSON or CSV:

<script src="https://gist.github.com/smrfeld/22ce465a643f6056a3cc8f8b519d1615.js"></script>



---

### Final thoughts

Now we have a backup of the reading list. A future project may write an edited CSV or JSON file back to the reading list `plist` format recognized by Safari.



By [Oliver K. Ernst, Ph.D.](https://medium.com/@oliver-k-ernst) on [December 16, 2021](https://medium.com/p/dc36992766e4).

[Canonical link](https://medium.com/@oliver-k-ernst/export-safari-reading-list-using-python-dc36992766e4)

Exported from [Medium](https://medium.com) on July 24, 2022.

