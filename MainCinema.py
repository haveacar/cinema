from CinematTickets import halls_menu, halls_draw, sell_tickets, return_tickets, reserve_tickets

while True:
    start_menu = input(
        "VIEW HALLS MENU press[1]\nSELL TICKETS MENU press[2]\nRETURN TICKETS MENU press[3]\nRESERVE TICKETS press["
        "4]\nEXIT press[5]\n: ")
    if not start_menu.isdigit() or int(start_menu) not in range(1, 6):
        print("Wrong input")
        continue
    else:
        start_menu = int(start_menu)
        match int(start_menu):
            # view halls
            case 1:
                halls_draw(halls_menu())
            # sell tickets menu
            case 2:
                sell_tickets()
            # return tickets menu
            case 3:
                return_tickets()
            # reserve tickets menu
            case 4:
                reserve_tickets()
            # exit application
            case 5:
                break
            # wrong input
            case _:
                print("wrong input")
                continue
