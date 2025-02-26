#!/bin/bash
#BSUB -J ex2_1
#BSUB -n 1
#BSUB -q hpc
#BSUB -W 1
#BSUB -o outputs_%J.out
#BSUB -e errors_%J.err
#BSUB -u s242798@dtu.dk
#BSUB -B 
#BSUB -N 
#BSUB -R "select[model==XeonGold6126]"
#BSUB -R "rusage[mem=2G]"
#BSUB -R "span[hosts=1]"

cd ~/02613/Python-High-Performance-Computing/Week4

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python ex2_1.py /dtu/projects/02613_2025/data/locations/locations_100.csv