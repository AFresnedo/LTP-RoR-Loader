#!/usr/bin/env bash
# case-sensitive folder name of the book to seed (from Dropbox)
curriculum=$1
# shared-path of all project-related files
fillerPath=~/Documents/GA/projects/oc
# python scripts need to know how many folders to ignore in absolute paths
# /, home, andres, Documents, GA, projects, oc
pythonFillerPathLength=7
# files is the path of the folder containing the book content
# !!!DO NOT SET THE PATH OF THE DROPBOX FOLDER, it is your LOCAL copy!!!
files=$fillerPath/input/$1
# seeds is the path of the seed folder for the rails application
seeds=$fillerPath/Online-Curriculum/db/seeds
# loader is the path of the folder containing all the input scripts
loader=$fillerPath/OC-Loader
# path to the rails application
ma=$fillerPath/Online-Curriculum
# for picture seeder
pic_files=$fillerPath/input/$1
# export variables so that file-specific seeders can use them
export curriculum
export files
export seeds
export loader
export fillerPath
export pic_files
export ma
export pythonFillerPathLength

# TODO re-evaluate "all" seed, right now it re-seeds users and $1 book
# setup for gigantic seed file
rm $seeds/all.rb
find $ma/db -name 'seeds.rb' -exec cat {} >> $seeds/all.rb \;

# fix figure HREFs
find $files -name *.html | xargs sed -i 's/img src="FIGS/img src="\/FIGS/'

# call file-specific seeders
$loader/copy_pictures.sh
$loader/problem_seeder.sh
$loader/theory_seeder.sh
$loader/graph_seeder.sh
$loader/globalgraph_seeder.sh
