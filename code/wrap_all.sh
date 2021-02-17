#!/bin/bash

parentDir=~/Projects/cal_abstract
codeDir=${parentDir}/code
stimDir=${parentDir}/stimuli
blockDir=${parentDir}/blocks

# get stimuli
if [ ! -f ${stimDir}/Dangerous/0.jpg ]; then
    source ${codeDir}/get_stim.sh

    # resize stim
    cd $stimDir
    catList=(`ls`)
    for cat in ${catList[@]}; do
        python ${codeDir}/scale_images.py ${stimDir}/$cat
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
fi

# make blocks
rm -r $blockDir
python ${codeDir}/task_setup.py
