# Hash Query System <a name="title"/>

This tool automates the process of collecting all the SHA1 hashes for our analysts, streamlining your workflow and ensuring accurate data retrieval. In this repository, you'll find the source code along with clear instructions on how to use it. The code will handle tasks such as reading Excel files, querying VirusTotal, and generating two text files, each containing different sets of results.

## Table of Contents
* [Hash Query System](#title)  
* [Setup](#setup)
* [Demo](#demo)

## Setup <a name="setup"/>
Please install the following packages and make sure you have Python 3.8+ installed:
```
pip install -r requirements.txt
```
Since the code relies on the VirusTotal API, you'll need to create an account and add your API key inside the `VirusTotal_Communicator.py` and `API_Usage_Counter` files. 

```
headers = {
        "accept": "application/json",
        "x-apikey": "PLACE_YOUR_KEY_HERE"
          }
```

Additionally, you need to add your API key into url variable found in the `API_Usage_Counter` file
```
url = "https://www.virustotal.com/api/v3/users/PLACE_YOUR_KEY_HERE/overall_quotas"
```

For certain cases, you'll need to replace the `MD5` with the corresponding column title from the Excel file. 
```
MD5_Hash = df['MD5'].iloc[i]
```

Lastly, key in the excel file name in the `Excel_File_Name.py` file. 

```
File_name = 'THE_EXCEL_FILE_NAME'
```

## Demo <a name="demo"/>
Here are the results you'll see when you encounter any of these scenarios.
### Successful Script Execution
```
Successfully converted Excel_File.xlsx to Excel_File.csv

Row 1 has a hash value of 000070b6ed87d3c54e335e5e98eeb181
SHA1 values exist!
The value is: ccd0cb34e6496cadad1d8129b3a1fc699a46c71f

Row 2 has a hash value of 00ef84b157a6a033623a64c3767b8299
SHA1 values exist!
The value is: 07d5a333593434ec5def68c8391f6c20ee797542

Row 3 has a hash value of 0118c591b84da186aeec8802cb7659ee
SHA1 values exist!
The value is: 4198f5d0017e11c5dc9858db3d1d9f5803bc8f03

Row 4 has a hash value of 012d7d7aba617660dc8fd939a0de7d65
SHA1 values exist!
The value is: 7edf54e4717d322538140882cc36ac9df4cc2d69

Row 5 has a hash value of 0173130bbf6bf93a02153981e3bcfbaa
SHA1 values exist!
The value is: 4d65ab326228f24c4e171576b857abdd979ab84f

Row 6 has a hash value of 01b009d38901412618fecc7bcc2c790b
SHA1 values exist!
The value is: e0770c905449f712ad96594e97148d012d6937dd

Row 7 has a hash value of 02deae1cb9ad12add3d9fef4a2f598de
SHA1 values exist!
The value is: 10d5f1f87e366bcc4b927232bcf459f5d60ffe5b

Row 8 has a hash value of 034138daf6dbcad0130892a8fe482782
SHA1 values exist!
The value is: 7f6e02624468b0b3bb1e249853748e027cf510d2

Row 9 has a hash value of 036b4e7099ac2d8097872eb55c4e8f47
SHA1 values exist!
The value is: 7ec78cba468280d7fdd25626f82a7b20795a80f4

Row 10 has a hash value of 039d4c538d5528cd050b7109be174975
SHA1 values exist!
The value is: e43e8632efe7cda5d05ec1ea670474f4f7d32ac5

Code execution has ended!
A total of 10 SHA1 values were found, while 0 hashes were not located in VirusTotal.
You have utilized 10 tokens, leaving you with 490 tokens remaining.

Text file SHA1_values has been created.
```

### Scenario 1 of Unsuccessful Script Execution
When you didn't handle the excel file correctly:
```
####################################################################################################
FileNotFoundError: [Errno 2] No such file or directory: 'Excel_File.csv'.

Here are 2 possible reason for this error:
-The excel file is not in the same directory as your script
-You misspelled the file name in File_Name.py
####################################################################################################

####################################################################################################
AttributeError: 'NoneType' object has no attribute 'empty'.

The scan_and_read_CSV_file function returned None. This is because FileNotFoundError happened first.
####################################################################################################

The codes have stopped running.
```

### Scenario 2 of Unsuccessful Script Execution
When you forgot to add your API key in file `API_Usage_Counter`:
```
####################################################################################
KeyError: 'data' not found in the JSON data

Here is a possible reason for this error:
-You didn't add your API key in file API_Usage_Checker

Please ensure that you have added your API key in both the url and headers variables
####################################################################################

####################################################################################
AttributeError: unsupported operand type(s) for -: 'int' and 'NoneType'.

The get_response function returned None. This is because KeyError happened first.
####################################################################################

The codes have stopped running.
```

### Scenario 3 of Unsuccessful Script Execution
When you ran out of VirusTotal API tokens:
```
Successfully converted Excel_File.xlsx to Excel_File.csv

Row 1 has a hash value of 000070b6ed87d3c54e335e5e98eeb181
Quota has exceeded.

Row 2 has a hash value of 00ef84b157a6a033623a64c3767b8299
Quota has exceeded.

Row 3 has a hash value of 0118c591b84da186aeec8802cb7659ee
Quota has exceeded.

Row 4 has a hash value of 012d7d7aba617660dc8fd939a0de7d65
Quota has exceeded.

Row 5 has a hash value of 0173130bbf6bf93a02153981e3bcfbaa
Quota has exceeded.

Row 6 has a hash value of 01b009d38901412618fecc7bcc2c790b
Quota has exceeded.

Row 7 has a hash value of 02deae1cb9ad12add3d9fef4a2f598de
Quota has exceeded.

Row 8 has a hash value of 034138daf6dbcad0130892a8fe482782
Quota has exceeded.

Row 9 has a hash value of 036b4e7099ac2d8097872eb55c4e8f47
Quota has exceeded.

Row 10 has a hash value of 039d4c538d5528cd050b7109be174975
Quota has exceeded.

Code execution has ended!
A total of 0 SHA1 values were found, while 0 hashes were not located in VirusTotal.
You have utilized 500 tokens, leaving you with 0 token remaining.

Text file Unprocessed_hashes has been created.
```

### Scenario 4 of Unsuccessful Script Execution
When you forgot to update the MD5_Hash variable:
```
########################################################################################
AttributeError: 'MD51'.

It looks like the MD5_Hash variable isn't defined properly.
Kindly check the Excel file and make sure the column name matches the MD5_Hash variable.
########################################################################################

The codes have stopped running.
```
