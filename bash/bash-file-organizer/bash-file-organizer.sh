#!/bin/bash

# ===============================
# File Organizer Script
# Organize files by extension
# ===============================

# home directory
home_dir="$HOME"

# main folder
main_folder="$HOME/folder-extension"

# folder for files without extension
no_ext_folder="$main_folder/no-extension"

# create main folder if not exists
if [ ! -d "$main_folder" ]; then
    mkdir "$main_folder"
fi

# create no-extension folder if not exists
if [ ! -d "$no_ext_folder" ]; then
    mkdir "$no_ext_folder"
fi

# loop through files in home directory
for file in "$home_dir"/*; do

    # check if it is a file (not directory)
    if [ -f "$file" ]; then

        # get filename
        filename=$(basename "$file")

        # get extension
        extension="${filename##*.}"

        # check if file has extension
        if [ "$filename" != "$extension" ]; then

            # extension folder
            extension_folder="$main_folder/$extension"

            if [ ! -d "$extension_folder" ]; then
                mkdir "$extension_folder"
            fi

            # move file to extension folder
            mv "$file" "$extension_folder/"

        else
            # move file without extension
            mv "$file" "$no_ext_folder/"
        fi
    fi
done

echo "File organization completed"
echo "Files organized in $main_folder"
