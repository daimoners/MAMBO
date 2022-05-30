#!/bin/bash

script=run_cp2k.slurm
baseName=DPBIC_double-mixed-cdft
input=${baseName}.inp
output1=${baseName}-r-1.out
output2=${baseName}-r-2.out
state1Wfn=${baseName}-state-1-1_0.wfn
state2Wfn=${baseName}-state-2-1_0.wfn

#structures="29_68 134_181 161_168 102_141 148_149 58_106 50_131 46_48 111_119 22_91 31_167 110_159 103_135 78_198 84_117 13_23 123_138 190_197 99_132 86_124 149_197 111_160 142_150 17_23 96_127 41_90 69_101 148_181 112_144 122_155 92_138 99_178 125_127 23_72 110_111 86_93 77_87 126_134 20_67 136_172 7_45"

for i in $structures ;
do
    work_dir=${i}/mixed/
    cd $work_dir
    cp $state1Wfn ./FILES
    cp $state2Wfn ./FILES
    state1Strength=$(grep "Strength of constraint" ${output1} | tail -n 1 | awk '{print $5}')
    state2Strength=$(grep "Strength of constraint" ${output2} | tail -n 1 | awk '{print $5}')
    cd ./FILES

    sed -e "s/@SET RESTART_WFN          FALSE/@SET RESTART_WFN          TRUE/g" \
        -e "s/@SET MAX_SCF              500/@SET MAX_SCF              700/g" \
        -e "s/@SET BECKE_STR_1.*/@SET BECKE_STR_1          ${state1Strength}/g" \
        -e "s/@SET BECKE_STR_2.*/@SET BECKE_STR_2          ${state2Strength}/g" $input > pippo
    mv pippo $input
    cd ..
    sbatch $script
    cd ../../
#    echo $PWD
done
