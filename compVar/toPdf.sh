#!/bin/bash

pdflatex $1/$1.tex
echo "Compiling $1/$1.tex to pdf"
xdg-open $1/$1.pdf
find . -maxdepth 1 -type f -iname "*$1*" -exec mv {} $1/ \;
echo "Now opening $1/$1.pdf" 
