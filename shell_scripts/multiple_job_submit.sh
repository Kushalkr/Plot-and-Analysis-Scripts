#!/bin/bash

exp_number=2
exp_dir=/N/u/kkeshava/scratch/hwrf-dtc-br2/experiment$exp_number
cd $exp_dir
echo `ls -d ./`
#for idir in `ls -d exp_01*` ; do cd $idir ; qsub submit_exp.sh ; cd .. ; done
