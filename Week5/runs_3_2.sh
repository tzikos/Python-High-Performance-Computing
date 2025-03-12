#!/bin/bash
#BSUB -J ex3_2_w5
#BSUB -n 8
#BSUB -q hpc
#BSUB -W 10
#BSUB -o outputs_%J.out
#BSUB -e errors_%J.err
#BSUB -u s242798@dtu.dk
#BSUB -B 
#BSUB -N 
#BSUB -R "select[model==XeonGold6126]"
#BSUB -R "rusage[mem=256MB]"
#BSUB -R "span[hosts=1]"

cd ~/02613/Python-High-Performance-Computing/Week5

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python ex3_2.py
