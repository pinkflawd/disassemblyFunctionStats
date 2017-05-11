# disassemblyFunctionStats
Comparing function detection of R2 and IDA

Call both scripts to fill the database:

python funcCountR2.py [dir]

python idaPython.py [dir]

Note:
[dir] needs to be a directory containing Windows PE files, best named after file hashes. 
funcCountIDA.py currently contains a dummy path, needs to be fixed before running.
For flushing the DB, funcCountR2.py contains two lines of code that can be uncommented. 

The project is a proof of concept and serves debugging purposes only, don't expect wonders ;)
