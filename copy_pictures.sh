#!/usr/bin/env bash

# NOTE: call from the curriculum folder you want to process

# TODO first version will grab all ../FIG/* files and move them to
# math_affirm/public/'controller'/FIGS/; second version will actually preserve directories
# and not have 2 copies for everything

find ./**/**/FIGS/* -type f -exec cp {} ~/Documents/persProj/math_affirm/public/problems/FIGS/ \;
find ./**/**/FIGS/* -type f -exec cp {} ~/Documents/persProj/math_affirm/public/theories/FIGS/ \;
