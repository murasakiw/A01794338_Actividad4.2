import time
import sys

def read_data(file_name):
    """
    Read data from a text file and convert to integers.

    This function reads data from a text file specified by the file_name parameter.
    It converts data items to integers and returns a list containing the integers.

    Args:
        filename (str): The path to the text file to be read.

    Returns:
        list of int: A list containing the integers read from the text file.
    """
    with open(file_name, 'r', encoding='utf-8') as read_file:
        numbers_datum = []
        datum = read_file.readlines()
    read_file.close()
    for data in datum:
        try:
            numbers_datum.append(int(data.rstrip('\n')))
        except ValueError as error:
            print('Error:', str(error))
            continue
    return numbers_datum

def convert_to_binary(items_list):
    """
    Convert decimal numbers to binary.

    This function takes a list of decimal numbers and converts numbers to binary.
    The binary representation of each number is returned as a list of strings.

    Args:
        numbers (list of int): A list containing decimal numbers to be converted to binary.

    Returns:
        list of str: A list containing the binary representation of each decimal number.

    """
    results = []
    for item in items_list:
        positive = True if item >= 0 else False
        quotient = 1
        binary = []
        while quotient > 0:
            quotient = abs(item) // 2
            remainder = abs(item) % 2
            binary.append(str(remainder))
            item = quotient
        if positive:
            binary.reverse()
            binary_number = ''.join(binary)
            results.append(binary_number)
        else:
            for _ in range(len(binary)-1, 31):
                binary.append('0')
            binary_negative = []
            for bit in binary:
                if bit == '0':
                    binary_negative.append('1')
                elif bit == '1':
                    binary_negative.append('0')
            binary_negative.reverse()
            carry = 1
            for i in range(32 - 1, -1, -1):
                if binary_negative[i] == '1' and carry == 1:
                    binary_negative[i] = '0'
                elif binary_negative[i] == '0' and carry == 1:
                    binary_negative[i] = '1'
                    carry = 0

            binary_number = ''.join(binary_negative)
            results.append(binary_number)

    return results

def convert_to_hex(items_list, binaries_list):
    """
    Convert decimal numbers to hexadecimal.

    This function takes a list of decimal numbers and converts numbers to hexadecimal.
    The hexadecimal representation of each number is returned as a list of strings.

    Args:
        items_list (list of int): A list containing decimal numbers to be converted to hexadecimal.
        binaries_list (list of str): A list containing the binary numbers as str.

    Returns:
        list of str: A list containing the hexadecimal representation of each decimal number.

    """
    results = []
    conversion_dict = {'0000': '0','0001': '1','0010': '2','0011': '3',
                       '0100': '4','0101': '5','0110': '6','0111': '7',
                       '1000': '8','1001': '9','1010': 'A','1011': 'B',
                       '1100': 'C','1101': 'D','1110': 'E','1111': 'F'
                       }
    hexadecimal_digits = {0:'0', 1:'1', 2:'2', 3:'3',
                          4:'4', 5:'5', 6:'6', 7:'7',
                          8:'8', 9:'9', 10:'A', 11:'B',
                          12:'C', 13:'D', 14:'E', 15:'F'
                          }
    for i, item in enumerate(items_list):
        hex_digits = []
        if item >= 0:
            quotient = 1
            while quotient > 0:
                quotient = item // 16
                remainder = item % 16
                hex_representation = hexadecimal_digits[remainder]
                hex_digits.append(str(hex_representation))
                item = quotient
            hex_digits.reverse()
            hex_number = ''.join(hex_digits)
            results.append(hex_number)
        else:
            binary_number = binaries_list[i]
            for j in range(0,32,4):
                hex_digits.append(conversion_dict[binary_number[j:j+4]])
            hex_number = ''.join(hex_digits)
            results.append(hex_number)

    return results

def print_results(converted_results, elapsed_time, file_name, origin_file):
    """
    Print conversion results to screen and save them to a text file.

    This function takes the conversion results, the execution time, and the filename
    where the results will be saved. 
    It prints the conversion results to the screen and writes them to a text file.

    Args:
        results (list): A list containing the conversion results.
        execution_time (float): The execution time of the conversion process.
        output_filename (str): The filename to save the results to.

    Returns:
        None
    """
    str_results = 'Decimal'.ljust(15) + 'Binary'.ljust(35) + 'Hexadecimal\n\n'
    for result in converted_results:
        str_results+=f'{str(result[0]).ljust(15)} {result[1].ljust(35)} {result[2]}\n'
    str_results += f'\nElapsed time = {elapsed_time} seconds\n\n'
    print(str_results)
    with open(file_name, 'a', encoding='utf-8') as results_file:
        results_file.write(f'File {origin_file} results\n')
        results_file.write(str_results)



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
    results_file_name = 'ConvertionResults.txt'
    start_time = time.time()
    numbers_datum = read_data(file_name)
    binary_results = convert_to_binary(numbers_datum)
    hex_results = convert_to_hex(numbers_datum, binary_results)
    results = [[numbers_datum[i], binary_results[i], hex_results[i]]
               for i in range(len(hex_results))
               ]
    end_time = time.time()
    elapsed_time = end_time - start_time
    print_results(results, elapsed_time, results_file_name, file_name)

if __name__ == '__main__':
    main()
