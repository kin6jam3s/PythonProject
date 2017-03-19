def main():
    print_header()
    run_event_loop()


def print_header():
    print("--------------------------")
    print(" PERSONAL JOURNAL  APP    ")
    print("--------------------------")


def run_event_loop():

    print('What do you want to do with your journal')
    cmd = None

    while cmd != 'x':
        cmd = input('[L]ist entry, [A]add entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries()
        elif cmd == 'a':
            add_entries()
        elif cmd != 'x':
            print("Sorry, We don't understand '{}'.".format(cmd))
        else:
            print('Exit')
    print('Good Bye')


def list_entries():
    print('Listing...')


def add_entries():
    print('Adding')

main()