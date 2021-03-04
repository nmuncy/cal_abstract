#!/bin/bash

# Pass subj int to job_taskSetup.py
#	to generate blocks/sub-*/Blocks*.csv

for i in 00 {1..6}{0..3}; do
	python job_taskSetup.py $i
done