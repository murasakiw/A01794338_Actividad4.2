import time
import sys

def calculate_mean(items_list):
    """
    Calculate the mean of a list of numbers.

    Args:
        items_list (list): A list of numbers.

    Returns:
        float: The mean of the numbers in the list.
    """
    mean = sum(items_list)/len(items_list)
    return mean

def calculate_mode(items_list):
    """
    Calculate the mode of a list of numbers.

    Args:
        items_list (list): A list of numbers.

    Returns:
        float: The mode of the numbers in the list.
    """
    elements = items_list.copy()
    elements = list(set(elements))
    mode = list()
    max_quantity = 0
    for element in elements:
        items_number = items_list.count(element)
        if items_number > max_quantity:
            mode.clear()
            mode.append(element)
            max_quantity = items_number
        elif items_number == max_quantity:
            mode.append(element)
    if max_quantity == 1:
        return 'Not defined'
    if len(mode) == 1:
        return mode[0]
    return mode

def calculate_median(items_list):
    """
    Calculate the median of a list of numbers.

    Args:
        items_list (list): A list of numbers.

    Returns:
        float: The median of the numbers in the list.
    """
    sorted_list = items_list.copy()
    sorted_list.sort()
    half_index = len(sorted_list)//2
    if len(sorted_list)%2 == 0:
        median = (sorted_list[half_index - 1] + sorted_list[half_index]) / 2
        return median
    else:
        median = sorted_list[half_index]
        return median

def calculate_variance(items_list):
    """
    Calculate the variance of a list of numbers.

    Args:
        items_list (list): A list of numbers.

    Returns:
        float: The variance of the numbers in the list.
    """
    mean = calculate_mean(items_list)
    square_diffs = [(element-mean)**2 for element in items_list]
    variance = sum(square_diffs)/len(items_list)
    return variance

def calculate_standard_deviation(variance):
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        variance (float): A float number.

    Returns:
        float: The standard deviation of the numbers in the list.
    """
    return variance**0.5

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
    results_file_name = 'StatisticsResults.txt'
    start_time = time.time()
    with open(file_name, 'r', encoding='utf-8') as read_file:
        numbers_datum = list()
        datum = read_file.readlines()
    read_file.close()
    for data in datum:
        try:
            numbers_datum.append(float(data.rstrip('\n')))
        except ValueError as error:
            print('Error:', str(error))
            continue
    variance = calculate_variance(numbers_datum)
    standard_deviation = calculate_standard_deviation(variance)
    end_time = time.time()
    elapsed_time = end_time - start_time
    results = [f'File [{file_name}] statistics results:\n',
                f'mean = {calculate_mean(numbers_datum)}\n',
                f'mode = {calculate_mode(numbers_datum)}\n',
                f'median = {calculate_median(numbers_datum)}',
                f'variance = {variance}\nstandard deviation = {standard_deviation}',
                f'Elapsed time = {elapsed_time} seconds\n\n']
    with open(results_file_name, 'a', encoding='utf-8') as results_file:
        results_file.write(f'File {file_name} results\n\n')
        for result in results:
            results_file.write(result)
            print(result)

if __name__ == '__main__':
    main()
