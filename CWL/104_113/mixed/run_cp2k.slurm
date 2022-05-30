#!/bin/bash
#SBATCH -n 16
#SBATCH --nodes=1
##SBATCH --nodelist=dmn04
#SBATCH --exclude=dmn01,dmn02,dmn03
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=1
#SBATCH --time=144:00:00
##SBATCH --mem=110000
#SBATCH --job-name=DP_104_113
#SBATCH --error=job.error
#SBATCH --output=job.output
#
#---------------------------------------------------------------------------------------

rootname=DPBIC_double-mixed-cdft
cd $SLURM_SUBMIT_DIR ! The directory from which sbatch was invoked
RUNDIR=/scratch/fabio/${SLURM_JOB_ID}
mkdir $RUNDIR
echo "Running on $SLURM_JOB_NODELIST at $RUNDIR"
cp ./FILES/* $RUNDIR
cd $RUNDIR

module load cp2k/6.1.0
### pure mpi executable cp2k.popt
export OMP_NUM_THREADS=1

mpirun -np 16 cp2k.popt -i ${rootname}.inp -o ${rootname}.out

#Bring them back home
cp -p * $SLURM_SUBMIT_DIR
#rm -r $RUNDIR
