# Seeder for Math Affirm

Creates book-specific seed files for the Math Affirm Rails server.

## Requirements

* Linux
* Access to Dropbox/Problems/**book**/
* Python 2.7

## Configuration

You must specify your own system's relative filepaths to run these scripts.

If needed, use chmod to specify .sh files as executable. 
Short version:
`$ chmod u+x *file*`
Long version:
`$ man chmod`

### Paths to set (variables in seeder.sh)

* curriculum
* fillerPath
* pythonFillerPathLength
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
