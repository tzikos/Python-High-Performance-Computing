#!/bin/sh
#BSUB -q hpc
#BSUB -J ex3_3_w8
#BSUB -P 02613
#BSUB -n 24
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=256MB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -W 00:10
#BSUB -o ex3_3_w8_%J.out
#BSUB -e ex3_3_w8_%J.err

# Initialize Python environment
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

set -e
ns="10 25 50 100 200"
echo $ns
for n in $ns; do
    echo $n
    python ex3_2.py 1000 $n
    du -sh mandelbrot_${LSB_JOBID}.zarr
done