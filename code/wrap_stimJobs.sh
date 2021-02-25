#!/bin/bash

parentDir=~/Projects/cal_abstract
codeDir=${parentDir}/code
stimDir=${parentDir}/stimuli
# blockDir=${parentDir}/blocks

# get stimuli
source ${codeDir}/job_stimGet.sh

# resize stim
cd $stimDir
catList=(`ls`)
for cat in ${catList[@]}; do
    python ${codeDir}/job_stimScale.py ${stimDir}/$cat
done

# rename resampled
cd $stimDir
for cat in ${catList[@]}; do
    cd $cat
    for file in res_*; do
        mv $file "${file/res_/}"
    done
    cd $stimDir
done

# # make blocks
# rm -r $blockDir
# python ${codeDir}/task_setup.py
