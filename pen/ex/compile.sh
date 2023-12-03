#!/bin/bash

pdflatex $1/report.tex
pdflatex $1/report.tex
find . -maxdepth 1 -iname "report*" -exec mv {} $1/ \;
xdg-open $1/report.pdf
