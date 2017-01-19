#!/bin/bash


dir='/N/u/kkeshava/scratch/hwrf-dtc-br2/experiment_sst'
cd $dir

for idir in `ls -d */ | cut -f1 -d'/'`
do
  cd $idir
  rm time_series*.txt
  paste ./exp_0*/time_series_*.txt > ./time_series_${idir}K.txt
  cd ..
done



for idir in `ls -d */ | cut -f1 -d'/'`
do
  cd $idir
  (awk '{print $2"\t"$5"\t"$8"\t"$11"\t"$14"\t"$17"\t"$20"\t"$23"\t"$26"\t"$29"\t"$32"\t"$35"\t"$38"\t"$41"\t"$44"\t"$47"\t"$50"\t"$53"\t"$56"\t"$59"\t"$62"\t"$65"\t"$68}' time_series_${idir}K.txt ) | paste > time_series_${idir}K_2.txt ; mv time_series_${idir}K_2.txt time_series_${idir}K.txt
  cd ..
done
