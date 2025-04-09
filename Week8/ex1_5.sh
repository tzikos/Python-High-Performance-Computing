#!/bin/sh
#BSUB -q hpc
#BSUB -J ex1_5_w8
#BSUB -P 02613
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=16GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -W 00:10
#BSUB -o ex1_5_w8_%J.out
#BSUB -e ex1_5_w8_%J.err

# Initialize Python environment
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

echo $CPUTYPE

/usr/bin/time -f"mem=%M KB runtime=%e s" \
python ex1_5.py dmi_chunks.parquet \
2>&1  # Magic to redirect stderr to stdour (since time prints to stderr)