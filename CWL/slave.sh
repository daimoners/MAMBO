#!/bin/bash

templatescript=run_cp2k.slurm.template
script=run_cp2k.slurm
templateinput=DPBIC_double-mixed-cdft.inp.template
input=DPBIC_double-mixed-cdft.inp
#for directory in `find . -maxdepth 1 -mindepth 1 -type d|  sed 's#./##'`
for directory in 152_166 30_171 3_130
do
    work_dir=${directory}/mixed
    if [ ! -d $work_dir ] ; then
        mkdir -p $work_dir
    else
        rm -r $work_dir/*
    fi
    cp -r FILES $work_dir
    rm ./${directory}/DPBIC_double_resid_${directory}.xyz
    cp ./${directory}/DPBIC_double_resid_${directory}_align_rec.xyz $work_dir/FILES
    cd $work_dir/FILES
    sed -e "s/LT_PAIR/${directory}/g" $templatescript > $script
    sed -e "s/LT_PAIR/${directory}/g" $templateinput > $input
    cd ..
    cp ./FILES/$script .
    sbatch $script
    cd ../../
done
