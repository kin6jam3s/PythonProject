import csv
import os
import statistics

from data_types import Purchase


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
    return os.path.join(base_folder, 'data', 'Sacramentorealestatetransactions.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        purchases = []

        for row in reader:
            # print(type(row), row)
            # print("Bed count: {}, type: {}".format(row['beds'], type(row['beds'])))
            # print(row)
            # print('----------------------------')
            p = Purchase.create_from_dict(row)
            # print(p.__dict__)
            purchases.append(p)

        print(purchases[0].__dict__)
        return purchases

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

    data.sort(key=lambda p: p.price)

    # most expensive house
    high_purchase = data[-1]
    print("the most expensive house is {} with {} beds and {} baths in {} {}".format(high_purchase.price,
                                                                           high_purchase.beds, high_purchase.baths,
                                                                            high_purchase.street, high_purchase.city))
    # least expensive house
    low_purchase = data[0]
    print("the least expensive house is {} with {} beds and {} baths in {} {} ".format(low_purchase.price,
                                                                           low_purchase.beds, low_purchase.baths,
                                                                                       low_purchase.street, low_purchase.city))

    # average price house

    prices = []
    for pur in data:
        prices.append(pur.price)
        # statistics.mean(prices)

    ave_price = statistics.mean(prices)
    print("The everage house price is ${:,}".format(int(ave_price)))

    # average price of 2 bedroom houses

    price = []
    for pur in data:
        if pur.beds == 2:
            prices.append(pur.price)

    ave_price = statistics.mean(prices)
    print("the average home price for 2 bedroom hours is ${:,}".format(int(ave_price)))



    # price_count = 0
    # for u in data:
    #     price_count += 1
    #
    #     print(u.price)
    #     print("{}, House in {} {} {} with {}, {} {} is {}".format(price_count, u.street, u.city, u.state, u.sq__ft,
    #                                                               u.beds, u.baths, u.price))

# test

    # testing for merge
    
if __name__ == "__main__":
    main()
