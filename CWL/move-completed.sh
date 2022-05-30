#!/bin/bash

for directory in $(cat batch_9)
do
	mv $directory results_9
done
mv *.dat results_9
mv *.csv results_9
mv results_9 couples
