#!/bin/bash
#BSUB -J sleeper
#BSUB -n 2
#BSUB -q hpc
#BSUB -W 2
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err
#BSUB -u s242798@dtu.dk
#BSUB -B 
#BSUB -N 
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -R "span[hosts=1]"
#BSUB -n 16

sleep 90
lscpu | grep "Model name"
