#!/usr/bin/env bash
# case-sensitive folder name of the book to seed (from Dropbox)
curriculum=$1
# shared-path of all project-related files
fillerPath=~/Documents/persProj
# files is the path of the folder containing the book content
# !!!DO NOT SET THE PATH OF THE DROPBOX FOLDER, it is your LOCAL copy!!!
files=$fillerPath/ma_files/$1
# seeds is the path of the seed folder for the rails application
seeds=$fillerPath/math_affirm/db/seeds
# loader is the path of the folder containing all the input scripts
loader=$fillerPath/ma_loader
# export variables so that file-specific seeders can use them
export curriculum
export files
export seeds
export loader
export fillerPath

# prepare local source
rm -r $files
mkdir $files
cp -r ~/Dropbox/MathAffirm/Problems/$1/* $files

# TODO re-evaluate "all" seed, right now it re-seeds users and $1 book
# setup for gigantic seed file
rm $seeds/all.rb
find ~/Documents/persProj/math_affirm/db -name 'seeds.rb' -exec cat {} >> $seeds/all.rb \;

# fix figure HREFs
find $files -name *.html | xargs sed -i 's/img src="FIGS/img src="\/FIGS/'

# call file-specific seeders
$loader/copy_pictures.sh
$loader/problem_seeder.sh
$loader/theory_seeder.sh
$loader/graph_seeder.sh
$loader/globalgraph_seeder.sh
