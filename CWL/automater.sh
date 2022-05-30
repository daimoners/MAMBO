#!/bin/bash

python generate-batches.py 100
mkdir -p ./couples
./copy-batch.sh
#cd job-submitter
./job-submitter/slave.sh
#./move_completed.sh
