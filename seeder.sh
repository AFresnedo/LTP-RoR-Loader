#!/usr/bin/env bash
curriculum=LIFETOMATH
files=~/Documents/persProj/ma_files/LIFETOMATH
seeds=~/Documents/persProj/math_affirm/db/seeds
loader=~/Documents/persProj/ma_loader
export curriculum
export files
export seeds
export loader

# TODO trigger backup of Dropbox/MathAffirm/Problems

# prepare local source
rm -r ~/Documents/persProj/ma_files/backup_LIFETOMATH/
mkdir ~/Documents/persProj/ma_files/backup_LIFETOMATH/
mv $files ~/Documents/persProj/ma_files/backup_LIFETOMATH
mkdir $files
cp -r ~/Dropbox/MathAffirm/Problems/LIFETOMATH/* $files

# setup for gigantic seed file
rm $seeds/all.rb
find ~/Documents/persProj/math_affirm/db -name 'seeds.rb' -exec cat {} >> $seeds/all.rb \;

$loader/problem_seeder.sh
$loader/theory_seeder.sh
$loader/graph_seeder.sh
$loader/globalgraph_seeder.sh
