#!/bin/sh
### General options
#BSUB -q hpc
#BSUB -P 02613
#BSUB -J ex2_2_w8
#BSUB -n 32
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=256MB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -W 00:10
#BSUB -o batch_output/ex2_2_w8_%J.out
#BSUB -e batch_output/ex2_2_w8_%J.err

# Initialize Python environment
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

set -e
ns="1 2 4 8 16 24 32"
echo $ns
for n in $ns; do
    echo $n
    python mandelbrot_memmap.py 1000 $n
done