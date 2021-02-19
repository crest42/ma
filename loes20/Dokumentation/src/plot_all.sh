#!/bin/bash
TARGETS=($(find  ./loes20/Dokumentation/src/ -maxdepth 1 -type f -regex "^.*/plot.*py$"))
for item in ${TARGETS[*]}
do
  printf "%s\n" $item
  python $item
done
