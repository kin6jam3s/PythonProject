import csv
import os


def main():
    print_header()

    ''' Getting data file'''
    filename = get_data_file()
    print(filename)

    '''Load the data'''
    data = load_file(filename)
    # print(data)

    '''Query Data'''
    query_data(data)


def print_header():
    print('--------------------')
    print(' REAL STATE APP')
    print('--------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data','Sacramentorealestatetransactions.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        for row in reader:
            print(type(row), row)
            print("Bed count: {}".format(row['beds']))

        #
        # header = fin.readline().split()
        # reader = csv.reader(fin, delimiter=',')
        # for row in reader:
        #     print(type(row), row)
        #




# def load_file_basic(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline()
#         print('Found header: ' + header)
#
#         lines = []
#         for line in fin:
#             line_data = line.split(',')
#             lines.append(line_data)
#
#         print(lines[:5])


def query_data(data):
    pass


if __name__ == "__main__":
    main()
