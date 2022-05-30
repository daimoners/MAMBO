#!/bin/bash

for directory in $(cat batch_8)
do
	rm -rf $directory
done
