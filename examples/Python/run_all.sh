#!/bin/bash

# Run all the python examples endlessly.
while true; do
  for f in *.py; do
    if ! grep -q "Omit" $f; then
      echo $f
      if python $f; then
        sleep 4
      else
        exit 1
      fi
    fi
  done
done

