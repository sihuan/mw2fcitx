#!/bin/bash
pushd ..
cp tests/blob/titles.txt titles.txt
# Fetch process are skipped
make moegirl.dict
make moegirl.dist.yaml
popd