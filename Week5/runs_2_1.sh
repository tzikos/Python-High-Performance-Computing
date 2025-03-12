#!/bin/bash
#BSUB -J ex2_1_w5
#BSUB -n 16
#BSUB -q hpc
#BSUB -W 1
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

echo "Results for fully serial"
echo ""
time python ex2_1_1.py
echo "--------------------------------------"
echo ""
echo "Results for fully parallel"
echo ""
time python ex2_1_2.py
echo "--------------------------------------"
echo ""
echo "Results for chunked parallel"
echo ""
time python ex2_1_3.py

