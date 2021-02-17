#!/bin/bash

sourceDir="/Users/nmuncy/Google\ Drive/PostDoc/Projects/Learning/Stimuli"
outDir=~/Projects/cal_abstract/stimuli
catList=(Alive Dangerous Distance Healthy Light Old Sad School Small Smell Soft Temperature Wealth)

eval cd $sourceDir
for cat in ${catList[@]}; do

	# make/update workDir
	workDir=${outDir}/$cat
	if [ -d $workDir ]; then
		rm -r $workDir
	fi
	mkdir $workDir
	cp ${cat}/*.* $workDir
	cd $workDir

	# clean spaces
	for file in *.*; do
		mv "$file" `echo $file | tr ' ' '_'`
	done

	# number
	imageList=(`ls`)
	for img in ${!imageList[@]}; do
		file=${imageList[$img]}
		suff=${file##*.}
		mv $file ${img}.$suff
	done

	# convert png to jpg
	for suff in *png; do
		str=${suff%.*}
		convert ${str}.png ${str}.jpg && rm ${str}.png
	done

	# fix jpeg suff
	for suff in *jpeg; do
		mv $suff "${suff/jpeg/jpg}"
	done

	eval cd $sourceDir
done
