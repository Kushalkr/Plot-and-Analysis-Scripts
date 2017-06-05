# To paste the time series in multiple directories next to each other in a  single file

#paste exp_0*/time_series_exp_*.txt > 12hr_shear_timeseries.txt

# This is more robust
find exp_0*/ -type f -name time_series_exp*.txt | xargs paste > 12hr_shear_timeseries2.txt
