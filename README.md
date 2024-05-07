To install:

bash -x install.sh

To launch downloadings of datasets:

python processing/download.py

To launch jupyter:

bash -x start_jupyter.sh

To prepare beamer presentation:

pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf -output-directory=./out slides.tex

