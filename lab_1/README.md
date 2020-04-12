# Description
Program for tariffication. Var 5
# Functions
- parsing_tables(f) - parse CDR file from {f}, returns a dictionary of lists.
- tariffication_t(mydict, phone_number, k_ti, k_tv) - returns a cost for user's calls.
- tariffication_s(mydict, phone_number, k_s, free_cost) - returns a cost for user's sms. 
# How to run
 `python3 mob_1.py`  
 CDR must be in the same folder, named 'data.csv'  
 Program will write a price into output.txt (Create in case it isnt exist)