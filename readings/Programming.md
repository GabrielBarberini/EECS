# Programming

## Command line
* [Command line tricks](https://medium.com/@kadek/command-line-tricks-for-data-scientists-c98e0abe5da)
  --> `grep -lr 'word' .` recursively search and list all files in directory containing 'word';
  --> `sort -t, -k2 filename.csv` sort a CSV file by the second column alphabetically;
  --> `split -l 500 filename.csv new_filename_` split CSV into new_filename every 500 lines
  --> `cat tab_delimited.txt | tr "\\t" "," > comma_delimited.csv` converting a tab delimited file into commas
  