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
Since the code relies on the VirusTotal API, you'll need to create an account and add your API key inside the `VirusTotal_Communicator.py` file. 

```
headers = {
        "accept": "application/json",
        "x-apikey": "PLACE_YOUR_KEY_HERE"
          }
```
Lastly, key in the excel file name in the `Excel_File_Name.py` file. 

```
File_name = 'THE_EXCEL_FILE_NAME'
```

## Demo <a name="demo"/>
