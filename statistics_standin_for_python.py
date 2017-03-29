import statistics


def mean(data):
    # return 0

    total = 0.0
    count = 0

    for x in data:
        count += 1
        total += x

        print('the count is {:,}'.format(count))
        print('the total is {:,}'.format(total))

        Ttal = total / max(1, count)
        print(' The total is: {}'.format(Ttal))
        return Ttal



# users = get_active_customers() - data
#
# paying_usernames = [] - create a blank list
# for u in users: - loop
#     if u.last_purchase == today: - test
#         paying_usernames.append(u.name) - output



# paying_usernames = [
#     u.name
#     for u in get_active_customers()
#     if u.last_purchase == today
# ]

''' Sample below for project 9'''


prices = []  # list
for pur in data:
    prices.append(pur.price)
    # statistics.mean(prices)

ave_price = statistics.mean(prices)
print("The average house price is ${:,}".format(int(ave_price)))


prices = [  # list
    p.price  # projection or items
    for p in data  # the set to process
]

ave_price = statistics.mean(prices)
print("The average house price is ${:,}".format(int(ave_price)))



'''Sample 2'''

# average price of 2 bedroom houses

'''1st format'''
price = []
for pur in data:
    if pur.beds == 2:
        prices.append(pur.price)

ave_price = statistics.mean(prices)
print("the average price for 2 bedroom home is ${:,}".format(int(ave_price)))

'''2nd format'''

prices = [
    p.price  # projection or items
    for p in data  # the set to process
    if p.beds == 2
]

ave_price = statistics.mean(prices)
print("the average price for 2 bedroom home is ${:,}".format(int(ave_price)))



'''List comprehension'''

two_bed_homes = [
    p  # projection or items
    for p in data  # the set to process - source
    if p.beds == 2  # test condition
]
#

ave_price = statistics.mean([p.price for p in two_bed_homes])
ave_baths = statistics.mean([p.baths for p in two_bed_homes])
ave_sq__ft = statistics.mean([p.sq__ft for p in two_bed_homes])

# ave_price = statistics.mean(prices)
print("the average price for 2 bedroom home is ${:,}, baths={}, sq ft {:,} "
      .format(int(ave_price), round(ave_baths, 1), round(ave_sq__ft, 1)))



# generator expressions

paying_usernames = (
    u.name
    for u in get_active_customer()
    if u.last_purchase == today

)


# Data pipelines + generators

# task1. find all house that are match my requirements (3 bedrom, near a city,etc)
# task2. Find all houses that are for sale that might in theory buy
# task3. find all houses i might buy near me
#
#
# all_transactions = get_tx_stream()
#
# interesting_tx = (
#     tx
#     for tx in all_transactions
#     if is_interesting(tx)
# )


    # potentially_sellable_tx = (
    #     tx
    #     for tx in interesting_tx
    #     if is_sellable(tx)
    # )

        # nearly_sellable_interesting_tx = (
        #     tx
        #     for tx in otentially_sellable_tx
        #     if is_nearby(tx)
        # )