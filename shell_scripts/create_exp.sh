#!/bin/bash
# Program to submit experiment jobs

#set -x
set -e

exp_dir=/N/u/kkeshava/scratch/hwrf-dtc-br2/experiment_sst/exp_$1
t=$(echo $1 | sed s/0*//)
mkdir -p $exp_dir

cd $exp_dir

ln -sf /N/u/kkeshava/scratch/hwrf-dtc-br2/experiment_sst/exp_template/* ./
rm fort.63 job.sh
cp /N/u/kkeshava/scratch/hwrf-dtc-br2/experiment_sst/exp_template/job.sh ./
cp /N/u/kkeshava/scratch/hwrf-dtc-br2/experiment_sst/exp_template/fort.63 ./

sed -i "s/00000/$1/g" $exp_dir/submit_exp.sh
sed  -i -e "s/0/5/1" -e "s/0/$t/2" $exp_dir/fort.63
# Replaces the first zero by the magnitude of the velocity and the 3rd zero by the time of the perturbation

qsub submit_exp.sh

#cd /N/u/kkeshava/scratch/hwrf-dtc-br2/experiment_sst/scripts
cd /N/u/kkeshava/Karst/scripts

exit 0

# To submit, use following command
# for i in 00000 00540 00720 00900 01080 01260 01440 01620 01800 01980 02160 02340 02520 02700 02880 03060 03240 03420 03600 03780 03960 04140 04320; do echo $i; done
