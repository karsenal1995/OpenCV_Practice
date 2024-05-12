from urllib.request import urlretrieve
from zipfile import ZipFile
import os


def download_and_unzip(url, path):
    save_path = os.path.join(os.getcwd(), path)
    if os.path.exists(save_path):
        print("Exist path: ", save_path)
        return

    print("Downloading")
    urlretrieve(url, save_path)

    try:
        with ZipFile(save_path) as z:
            z.extractall(os.path.split(save_path)[0])
        print("Done")
    except Exception as ex:
        print("Exception: ", ex)
