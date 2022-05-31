cwlVersion: v1.1
class: CommandLineTool

baseCommand: cp2k.popt

requirements:
    EnvVarRequirement:
        envDef:
            OMP_NUM_THREADS: 1
            ROOTNAME: DPBIC_double-mixed-cdft

inputs:
    filesA:
         type: File
         inputBinding:
            prefix: -i 
            position: 1
    filesB:
         type: File
         inputBinding:
            prefix: -o 
            position: 2

outputs:
    simulation_output:
        type: File
