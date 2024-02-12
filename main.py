from pprint import pprint


def read_sneakers_data(file_name):
    sneakers_data = []
    with open(file_name, 'r') as file:
        for line in file:
            sneaker_info = line.strip().split(',')
            sneaker_dict = {
                'title': sneaker_info[0],
                'color': sneaker_info[1],
                'full_price': sneaker_info[2],
                'current_price': sneaker_info[3],
                'publish_date': sneaker_info[4]
            }
            sneakers_data.append(sneaker_dict)
    return sneakers_data


def sort_and_display_sneakers(sneakers, key_func):
    sorted_sneakers = sorted(sneakers, key=key_func)
    pprint(sorted_sneakers)


def main():
    file_name = 'sneakers.csv'
    sneakers = read_sneakers_data(file_name)

    print(
        "Válasz, melyik szempont alapján rendezzem a cipőket? \n 1 - title, \n 2 - color, \n 3 - full price, \n 4 - current price,  \n 5 - publish date ")
    choice = input("Add meg a lehetőség számát! ")

    if choice == '1':
        answer = 'title'
    elif choice == '2':
        answer = 'color'
    elif choice == '3':
        answer = 'full_price'
    elif choice == '4':
        answer = 'current_price'
    elif choice == '5':
        answer = 'publish_date'
    else:
        print("Helytelen megadott érték.")
        return

    key_func = lambda x: x[answer]

    sort_and_display_sneakers(sneakers, key_func)


main()
