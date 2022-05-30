#!/bin/bash

output=DPBIC_double-mixed-cdft.out
directories=`find . -maxdepth 1 -mindepth 1 -type d|  sed 's#./##'`
auxDir=FILES
#echo $directories

echo "#MolI MolJ" > DPBIC_pairs.dat
echo "Strength_I" > Strength_of_constraint_I.dat
echo "Strength_J" > Strength_of_constraint_J.dat
echo "Constraint_I" > Final_value_of_constraint_I.dat
echo "Constraint_J" > Final_value_of_constraint_J.dat
echo "Overlap" > Overlap_between_states_I_and_J.dat
echo "CT_Energy(eV)" > Charge_transfer_energy_J-I.dat
echo "Coupling(meV)" > Diabatic_electronic_coupling.dat

#directories=9_96
for i in $directories ;
do
 if [ "$i" != "FILES" ] 
 then 
    echo ${i//_/ }>> DPBIC_pairs.dat
   
    work_dir=${i}/mixed

    strengthI=$(grep "Strength of constraint I:" ${work_dir}/${output} | awk '{print $5}')
    if [ -z "$strengthI" ]
    then
          echo "NaN" >> Strength_of_constraint_I.dat
    else
          echo "$strengthI" >> Strength_of_constraint_I.dat
    fi 

    strengthJ=$(grep "Strength of constraint J:" ${work_dir}/${output} | awk '{print $5}')
    if [ -z "$strengthJ" ]
    then
          echo "NaN" >> Strength_of_constraint_J.dat
    else
          echo "$strengthJ" >> Strength_of_constraint_J.dat
    fi

    finalI=$(grep "Final value of constraint I:" ${work_dir}/${output} | awk '{print $6}')
    if [ -z "$finalI" ]
    then
          echo "NaN" >> Final_value_of_constraint_I.dat
    else
          echo "$finalI" >> Final_value_of_constraint_I.dat
    fi

    finalJ=$(grep "Final value of constraint J:" ${work_dir}/${output} | awk '{print $6}')
    if [ -z "$finalJ" ]
    then
          echo "NaN" >> Final_value_of_constraint_J.dat
    else
          echo "$finalJ" >> Final_value_of_constraint_J.dat
    fi

    overlap=$(grep "Overlap between states I and J:" ${work_dir}/${output} | awk '{print $7}')
    if [ -z "$overlap" ]
    then
          echo "NaN" >> Overlap_between_states_I_and_J.dat
    else
          echo "$overlap" >> Overlap_between_states_I_and_J.dat
    fi

    ctE=$(grep "Charge transfer energy (J-I) (Hartree):" ${work_dir}/${output} | awk '{print $6*27.2114}')
    if [ -z "$ctE" ]
    then
          echo "NaN" >> Charge_transfer_energy_J-I.dat
    else
          echo "$ctE" >> Charge_transfer_energy_J-I.dat
    fi

    coupling=$(grep "Diabatic electronic coupling " ${work_dir}/${output} | awk '{if ($5=="mHartree):") print $6*27.2114; else if ($5=="microHartree):") print $6*27.2114/1000}')
    if [ -z "$coupling" ]
    then
          echo "NaN" >> Diabatic_electronic_coupling.dat
    else
          echo "$coupling" >> Diabatic_electronic_coupling.dat
    fi
 fi
done

paste -d " " DPBIC_pairs.dat Strength_of_constraint_I.dat Strength_of_constraint_J.dat Final_value_of_constraint_I.dat Final_value_of_constraint_J.dat Overlap_between_states_I_and_J.dat Charge_transfer_energy_J-I.dat Diabatic_electronic_coupling.dat > DPBIC_pairs_data.dat

cat DPBIC_pairs_data.dat | tr -s ' ' | tr ' ' ',' > DPBIC_pairs_data.csv
