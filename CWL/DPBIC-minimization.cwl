cwlVersion: v1.1
class: CommandLineTool

baseCommand: mpirun

requirements:
    EnvVarRequirement:
        envDef:
            OMP_NUM_THREADS: 1
            ROOTNAME: DPBIC_double-mixed-cdft
            RUNDIR: /scratch/${username}/${SLURM_JOB_ID}

inputs:
    filesA:
        type: File
        inputBinding:
            prefix: -np
            position: 1

    filesB:
         type: File
         inputBinding:
            prefix: -i 
            position: 2

outputs:
    simulation_output:
        type: File
