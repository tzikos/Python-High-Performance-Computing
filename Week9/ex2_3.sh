#!/bin/bash
#BSUB -J cuda_jit
#BSUB -n 4
#BSUB -q c02613
#BSUB -W 5
#BSUB -o gpujob_%J.out
#BSUB -e gpujob_%J.err
#BSUB -u s242798@dtu.dk
#BSUB -B 
#BSUB -N 
#BSUB -R "select[model==XeonGold6126]"
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -R "rusage[mem=1GB]"
#BSUB -R "span[hosts=1]"

cd ~/02613/Python-High-Performance-Computing/Week9

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

time python ex2_2.py 1000000
