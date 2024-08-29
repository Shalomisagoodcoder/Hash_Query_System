def find_sha1_values(data):

    def search(obj):
        # Check for quota error in the current object
        if isinstance(obj, dict):
            if 'error' in obj:
                error_code = obj['error'].get('code')
                if error_code == 'QuotaExceededError':
                    print('Quota has exceeded.')
                    return None

            # Continue searching the dictionary
            for key, value in obj.items():
                if key == 'sha1':
                    results.append(value)
                search(value)

        elif isinstance(obj, list):
            # Continue searching each item in the list
            for item in obj:
                search(item)

        else:
            None
        return results
    # Initialize the results list
    results = []
    return search(data)

