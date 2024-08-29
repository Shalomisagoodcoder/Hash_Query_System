def save_sha1_values_to_file(value, filename):
    with open(filename, 'a') as file:
        file.write(' '.join(value) + '\n')
        file.close()

def save_md5_values_to_file(value, filename):
    with open(filename, 'a') as file:
        file.write(value + '\n')
        file.close()

def unprocessed_hashes(value, filename):
    with open(filename, 'a') as file:
        file.write(value + '\n')
        file.close()
