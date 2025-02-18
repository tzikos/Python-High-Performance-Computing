#!/bin/bash
#BSUB -J sleeper
#BSUB -n 2
#BSUB -q hpc
#BSUB -W 2
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err

sleep
