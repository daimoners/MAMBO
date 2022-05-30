#!/bin/bash

for directory in $(cat batch_9)
do
	cp -r ../build/structures_0_16/$directory .
done
mkdir ./results_9
