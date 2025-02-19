#!/bin/bash
#BSUB -J mat_mul
#BSUB -n 1
#BSUB -q hpc
#BSUB -W 1
#BSUB -o mat_mul_%J.out
#BSUB -e mat_mul_%J.err
#BSUB -u s242798@dtu.dk
#BSUB -B 
#BSUB -N 
#BSUB -R "rusage[mem=2GB]"
#BSUB -R "span[hosts=1]"

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python -u /zhome/b0/3/214044/02613/Python-High-Performance-Computing/Week2/numpy_5.py /zhome/b0/3/214044/02613/Python-High-Performance-Computing/Week2/input.npy 10