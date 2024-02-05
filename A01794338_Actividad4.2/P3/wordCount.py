import time
import sys

def get_word_count(words_list):
    """
    Count the occurrences of each word in a given list and return a dictionary
    where the keys are the unique words in the list and the values represent
    the number of occurrences of each word.

    Args:
        words_list (list): A list of words.

    Returns:
        dict: A dictionary where keys are unique words from the input list
              and values are the number of occurrences of each word in the list.

    """
    counted_words = []
    ocurrences = {}
    for word in words_list:
        ocurrences_number = 0
        if word not in counted_words:
            for item in words_list:
                if word == item:
                    ocurrences_number += 1
            ocurrences[word] = ocurrences_number
            counted_words.append(word)
    return ocurrences

def print_results(ocurrences, elapsed_time, file_name, origin_file):
    """
    Print word count results to screen and save them to a text file.

    This function takes the word count results, the execution time, and the filename
    where the results will be saved. 
    It prints the results to the screen and writes them to a text file.

    Args:
        results (list): A list containing the conversion results.
        execution_time (float): The execution time of the conversion process.
        output_filename (str): The filename to save the results to.

    Returns:
        None
    """
    results = ''
    sorted_ocurrences = dict(sorted(ocurrences.items(), key=lambda item:item[1], reverse=True))
    for key, value in sorted_ocurrences.items():
        results += f'{key} - {value}\n'
    results += f'\nElapsed time = {elapsed_time} seconds\n\n'
    print(results)
    with open(file_name, 'a', encoding="utf-8") as results_file:
        results_file.write(f'File {origin_file} results\n')
        results_file.write(results)


def main():
    """
    Main function of the program.

    This function is the main entry point of the program. 
    It performs the necessary operations to execute the program
    and coordinate different functionalities.

    Parameters:
    None.

    Returns:
    None.
    """
    file_name = sys.argv[1]
    results_file_name = 'WordCountResults.txt'
    start_time = time.time()
    with open(file_name, 'r', encoding="utf-8") as read_file:
        words_datum = []
        datum = read_file.readlines()
    read_file.close()
    for data in datum:
        words_datum.append(data.rstrip('\n'))
    ocurrences = get_word_count(words_datum)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print_results(ocurrences, elapsed_time, results_file_name, file_name)

if __name__ == '__main__':
    main()
