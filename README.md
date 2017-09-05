# Seeder for Math Affirm

## Purpose

* Processes the Dropbox source file input for a book.
    * Theories
    * Problems
    * Graphs
    * Figures

* Creates one gigantic seed file **db/seeds/all.rb** for ease of seeding
    * Includes any entries from db/seed.rb


* Creates file specific seeds
    * db/seeds/problem_seed.rb
    * db/seeds/theory_seed.rb
    * db/seeds/graph_seed.rb
    * db/seeds/globalgraph_seed.rb

* Copies all the figures and adds them to Public/FIGS

## Requirements

* Linux
* Access to Dropbox/Problems/**book**/
* Python 2.7

## Configuration

Please refer to **seeder.sh** to configure all the necessary folder paths.

### Paths to set (variables in seeder.sh)

* curriculum
* fillerPath
* files
* seeds
* loader
* ma
* pic_files
* dropbox
    * if Dropbox's inner structure changes, find/fix all affected paths

## Usage

Execute `$ *path*/seeder.sh *book*` from the linux command line

* *book* represents the case-sensitive folder name for the book in Dropbox
    * Example: `$ ./seeder.sh LIFETOMATH` if seeding the LIFETOMATH book

## Documentation

Please refer to the [wiki](https://bitbucket.org/AFresnedo/math-affirm-loader/wiki/Home).
