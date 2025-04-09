#!/bin/sh
#BSUB -q hpc
#BSUB -J ex1_2_w8
#BSUB -P 02613
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=16GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -W 00:10
#BSUB -o ex1_2_w8_%J.out
#BSUB -e ex1_2_w8_%J.err

# Initialize Python environment
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

echo $CPUTYPE

set -e  # Stop on first error (because that would mean our script is wrong)

# Loop over chunk sizes
for c in 1000 10000 100000 1000000; do
echo $c
/usr/bin/time -f"mem=%M KB runtime=%e s" \
python ex1_1.py \
    /dtu/projects/02613_2025/data/dmi/2023_01.csv.zip $c \
2>&1  # Magic to redirect stderr to stdour (since time prints to stderr)
echo "--------------------------------------"
done