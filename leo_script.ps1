echo " "
echo "Experimentos da NASA -- Leo"
echo " "

echo "___COPY MATRIX"
python leo_copy_matrix.py 5000
echo " "

echo "___LOOK AND SAY"
python leo_look_and_say.py 45
echo " " 

echo "___FIBONACCI"
python leo_fibonacci.py 35
echo " "

echo "___COUNT UNIQUE WORDS"
python leo_count_unique_words.py ./Data/bible.txt
echo " "

echo "___IO"
python leo_time_series_AOA.py
python leo_time_series_AOA_multiproc.py 1
python leo_time_series_AOA_multiproc.py 2
python leo_time_series_AOA_multiproc.py 4
python leo_time_series_AOA_multiproc.py 8
python leo_time_series_AOA_multiproc.py 16
python leo_time_series_AOA_multiproc.py 24
python leo_time_series_AOA_multiproc.py 28
echo " "