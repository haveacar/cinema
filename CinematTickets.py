"""list comprehension"""
# hall for 30 people
green_hall = [x for x in range(1, 31)]
# hall for 50 people
blue_hall = [n for n in range(1, 51)]
# hall for 80 people
yellow_hall = [l for l in range(1, 81)]

# colors of print
RED_COLOR = "\u001b[48;5;8m"  # background

SELL_COLOR = "\u001b[38;5;12m"
RESERVE_COLOR = "\u001b[38;5;11m"
RESET_COLOR = "\u001b[0m"


def halls_menu():
    """
    input func halls choice and check input
    :return: n
    """

    while True:
        hall_menu = input("PRINT GREEN HALL(30) press[1]"
                          "\nPRINT BLUE HALL(50) press [2]\nPRINT YELLOW HALL(80) press [3]\n: ")
        # check correct input
        if not hall_menu.isdigit() or int(hall_menu) not in range(1, 4):
            print("Wrong input")
            continue
        else:
            # choice hall
            hall_menu = int(hall_menu)
            if hall_menu == 1:
                n = green_hall
            elif hall_menu == 2:
                n = blue_hall
            elif hall_menu == 3:
                n = yellow_hall
        return n


def halls_draw(n):
    """
    func to print hall
    :param n:
    :return:
    """
    line = 38 * "*"
    star1 = 6 * "*"
    # choice Hall name
    if len(n) < 31:
        hall_name = "Green Hall 1 (30 people)"
    elif len(n) < 51:
        hall_name = "Blue  Hall 2 (50 people)"
    else:
        hall_name = "Yellow Hall 2(80 people)"

    print(f"{RESERVE_COLOR}{line}\n{star1} {hall_name} {star1}{RESET_COLOR}".center(35))
    print(line)
    # print hall
    a = 0
    for j in range(len(n)):
        a += 1
        print(n[j], end="\t")
        if a % 10 == 0:  # multiple operator
            print("\n")
    print(line)
    print(F"{SELL_COLOR}SOLD-S{RESET_COLOR}\n{RESERVE_COLOR}RESERVE-R{RESET_COLOR}")


def sell_tickets():
    """
    func to sell tickets
    sold ticket return in console color blur
    :return:
    """
    star2 = 10 * "*"
    while True:
        hall_sell = halls_menu()
        halls_draw(hall_sell)
        # green hall sell
        if len(hall_sell) < 31:
            index_num = num_ticket()
            green_hall[index_num] = SELL_COLOR + "S" + RESET_COLOR
            print(f"{RED_COLOR}{star2}{'DONE'}{star2}{RESET_COLOR}")
            halls_draw(hall_sell)

        # blue hall sell
        elif len(hall_sell) < 51:
            index_num = num_ticket()
            blue_hall[index_num] = SELL_COLOR + "S" + RESET_COLOR
            print(f"{RED_COLOR}{star2}{'DONE'}{star2}{RESET_COLOR}")
            halls_draw(hall_sell)
        # yellow hall sell
        else:
            print(f"{RED_COLOR}{star2}{'DONE'}{star2}{RESET_COLOR}")
            index_num = num_ticket()
            yellow_hall[index_num] = SELL_COLOR + "S" + RESET_COLOR
            halls_draw(hall_sell)
        break


def num_ticket():
    """
    func to check input number ticket
    :return: int input
    """
    while True:
        sell_t = input("Number of Ticket #: ")
        # check correct input
        if not sell_t.isdigit() or int(sell_t) not in range(1, 80):
            print("Wrong input")
            continue
        else:
            sell_t = int(sell_t) - 1
        return sell_t


def return_tickets():
    """
    func to return tickets
    sold ticket return in console reset color
    :return:
    """
    star2 = 10 * "*"
    while True:
        hall_sell = halls_menu()

        halls_draw(hall_sell)
        # green hall reserve
        if len(hall_sell) < 31:
            index_num = num_ticket()
            green_hall[index_num] = RESET_COLOR + str(index_num + 1) + RESET_COLOR
            print(f"{RED_COLOR}{star2}{'DONE'}{star2}{RESET_COLOR}")
            halls_draw(hall_sell)

        # blue hall reserve
        elif len(hall_sell) < 51:
            index_num = num_ticket()
            blue_hall[index_num] = RESET_COLOR + str(index_num + 1) + RESET_COLOR
            print(f"{RED_COLOR}{star2}{'DONE'}{star2}{RESET_COLOR}")
            halls_draw(hall_sell)
        # yellow hall reserve
        else:
            print(f"{RED_COLOR}{star2}{'DONE'}{star2}{RESET_COLOR}")
            index_num = num_ticket()
            yellow_hall[index_num] = RESET_COLOR + str(index_num + 1) + RESET_COLOR
            halls_draw(hall_sell)
        break


def reserve_tickets():
    """
        func to reserve tickets
        reserve ticket return in console yellow color
        :return:
        """
    star2 = 10 * "*"
    while True:
        hall_sell = halls_menu()
        halls_draw(hall_sell)
        # green hall reserve
        if len(hall_sell) < 31:
            index_num = num_ticket()
            green_hall[index_num] = RESERVE_COLOR + "R" + RESET_COLOR
            print(f"{RED_COLOR}{star2}{'DONE'}{star2}{RESET_COLOR}")
            halls_draw(hall_sell)
        # blue hall reserve
        elif len(hall_sell) < 51:
            index_num = num_ticket()
            blue_hall[index_num] = RESERVE_COLOR + "R" + RESET_COLOR
            print(f"{RED_COLOR}{star2}{'DONE'}{star2}{RESET_COLOR}")
            halls_draw(hall_sell)
        # yellow hall reserve
        else:
            print(f"{RED_COLOR}{star2}{'DONE'}{star2}{RESET_COLOR}")
            index_num = num_ticket()
            yellow_hall[index_num] = RESERVE_COLOR + "R" + RESET_COLOR
            halls_draw(hall_sell)
        break
