import CSV_Converter
import SHA1_Finder
import Hash_Saver
import VirusTotal_Communicator
import API_Usage_Counter
import CSV_Checker
from File_Name import xlsx_file_name

CSV_Converter.xlsx_to_csv(xlsx_file_name)

df = CSV_Checker.scan_and_read_CSV_file()

Hashes_found_counter = 0
Hashes_not_found_counter = 0
SHA1_values_created = False
Unprocessed_hashes_created = False
Untraceable_SHA1_Hashes_created = False

try:
    if df.empty:
        print("\nThe codes have stopped running.")

    else:
        # Use a for loop to print the first 500 lines of the 'SHA1' column
        for i in range(min(500, len(df))):
            #Take note of the coloumn name as it may varies from time to time
            MD5_Hash = df['MD5'].iloc[i]
            print("\nRow",i+1, "has a hash value of", MD5_Hash)

            # Find 'sha1' values
            sha1_values = SHA1_Finder.find_sha1_values(VirusTotal_Communicator.virustotal(MD5_Hash))
            if sha1_values:
                print("SHA1 values exist!")
                for value in sha1_values:
                    print(f"The value is: {value}")

                    # Save sha1 values to a text file
                    Hash_Saver.save_sha1_values_to_file(sha1_values, 'SHA1_values.txt')
                    Hashes_found_counter += 1
                    SHA1_values_created = True

            elif sha1_values == None:
                Hash_Saver.unprocessed_hashes(MD5_Hash, 'Unprocessed_hashes.txt')
                Unprocessed_hashes_created = True
            else:
                print("No 'sha1' values found.")
                Hash_Saver.save_md5_values_to_file(MD5_Hash, 'Untraceable_SHA1_Hashes.txt')
                Hashes_not_found_counter += 1
                Untraceable_SHA1_Hashes_created = True

        print("\n\nCode execution has ended!")
        print(f"A total of {Hashes_found_counter} SHA1 values were found, while {Hashes_not_found_counter} hashes were not located in VirusTotal.")

        #Find remaining API tokens left
        API_tokens_used = API_Usage_Counter.get_response()
        API_tokens_left = 500 - API_tokens_used
        print(f"You have utilized {API_tokens_used} tokens, leaving you with {API_tokens_left} tokens remaining.")

        if SHA1_values_created and Unprocessed_hashes_created and Untraceable_SHA1_Hashes_created == True:
            print("\nText files SHA1_values, Unprocessed_hashes, and Untraceable_SHA1_Hashes have been created.")

        elif SHA1_values_created and Unprocessed_hashes_created == True:
            print("\nText files SHA1_values and Unprocessed_hashes have been created.")

        elif SHA1_values_created and Untraceable_SHA1_Hashes_created == True:
            print("\nText files SHA1_values and Untraceable_SHA1_Hashes have been created.")

        elif Unprocessed_hashes_created and Untraceable_SHA1_Hashes_created == True:
            print("\nText files Unprocessed_hashes and Untraceable_SHA1_Hashes have been created.")

        elif SHA1_values_created == True:
            print("\nText file SHA1_values has been created.")

        elif Unprocessed_hashes_created == True:
            print("\nText file Unprocessed_hashes has been created.")

        elif Untraceable_SHA1_Hashes_created == True:
            print("\nText file Untraceable_SHA1_Hashes has been created.")

except AttributeError as e:
    print('\n'+'#' * 140)
    print(f"AttributeError: {e}.")
    print("\nThe scan_and_read_CSV_file function returned None. This is because FileNotFoundError happened first.")
    print('#' * 140)
    print("\nThe codes have stopped running.")

except TypeError as e:
    print('\n'+'#' * 140)
    print(f"AttributeError: {e}.")
    print("\nThe get_response function returned None. This is because KeyError happened first.")
    print('#' * 140)
    print("\nThe codes have stopped running.")

except KeyError as e:
    print('\n'+'#' * 140)
    print(f"AttributeError: {e}.")
    print("\nIt looks like the MD5_Hash variable isn't defined properly.")
    print("Kindly check the Excel file and make sure the column name matches the MD5_Hash variable.")
    print('#' * 140)
    print("\nThe codes have stopped running.")
