#!/bin/bash

# Define the root directory where you want to start the search
root_directory=$(pwd)

# Use find to locate files containing "Report" in the specified directory and its subdirectories
find "$root_directory" -type f -iname "Report*" -print0 |
while IFS= read -r -d '' file; do
  # Check if the filename contains "Report" (case-insensitive)
  if [[ "$file" =~ [Rr]eport ]]; then
    # Extract the directory path and filename
    directory=$(dirname "$file")
    filename=$(basename "$file")
    
    # Rename the file with "report" (all lowercase) in the same directory
    new_name="$directory/$(echo "$filename" | sed 's/[Rr]eport/report/g')"
    mv "$file" "$new_name"
    echo "Renamed $file to $new_name"
  fi
done

