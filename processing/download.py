import requests
import zipfile
import gzip
import shutil
import os

from urllib.parse import urlparse, unquote

def process_zip_file(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall('../datasets')
    shutil.move("../datasets/fr.openfoodfacts.org.products.csv", "../datasets/fr.openfoodfacts.org.products.tsv")

def process_gzip_file(gzip_file_path):
    output_file_path = os.path.join("../datasets", os.path.basename(gzip_file_path).replace('.gz', ''))

    with gzip.open(gzip_file_path, 'rb') as f_in:
        with open(output_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def load_file(url):
    parsed_url = urlparse(url)
    # Extract the file name from the path
    file_name = unquote(parsed_url.path.split('/')[-1])
    response = requests.get(url)
    with open(file_name, 'wb') as file:
        file.write(response.content)
    return file_name

def main():
    url = "https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/parcours-data-scientist/P2/fr.openfoodfacts.org.products.csv.zip"
    file_name = load_file(url)
    process_zip_file(file_name)
    os.remove(file_name)

    official_url = "https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv.gz"
    file_name = load_file(official_url)
    process_gzip_file(file_name)
    os.remove(file_name)

if __name__ == "__main__":
    main()

