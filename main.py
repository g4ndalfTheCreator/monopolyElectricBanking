"""
This is my project:
Monopoly electric banking 0.01

COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       Samuli Tolvanen

This was my first programming project made for the first programming course at
the university.

Monopoly electric banking system uses Tkinter libraries to build a
GUI that allows keeping logs of money transfers in monopoly the boardgame.
"""

from tkinter import *
import setting_menu
import winner_screen


class GameGraphics:

    def __init__(self, player_wallet):

        # Setting up values:
        self.__player_wallet = player_wallet
        self.__player_names = list(self.__player_wallet)
        self.__player_numbers = len(self.__player_names)

        # Adding bank in names list
        self.__player_names.append("Bank")

        # Creating a window for player:
        self.__game_window = Tk()

        # Setting up elements
        self.__header = Label(self.__game_window, text="Monopoly Electric Banking System v.0.1", font=20,
                              background="yellow", relief=RAISED, borderwidth=5, width=60, height=2)  # Header is this.

        # Setting up header texts for money amount and player names:
        self.__header_player = Label(self.__game_window, text="Playername:", background="cyan", relief=RAISED,
                                     width=20, height=2)
        self.__header_money = Label(self.__game_window, text="Funds available:", background="cyan", relief=RAISED,
                                    width=20, height=2)

        # Creating button for transaction and input field for amount and header for input field
        self.__transaction_amount_header = Label(self.__game_window, text="Enter amount of funds:", background="coral",
                                                 relief=RAISED, width=20, height=2)

        self.__transfer_amount = Entry(self.__game_window, borderwidth=8, width=20)

        self.__transaction_transfer_button = Button(self.__game_window, text="↔ Make payment ↔", background="light green",
                                                    relief=RAISED, width=20, height=1, command=self.transfer_funds)

        # Creating rotational money add button:
        self.__rotational_money_add_button = Button(self.__game_window, text="→ Rotational funds 2M →", relief=RAISED,
                                                    width=20, height=1, command=self.add_rotational_money,
                                                    background="yellow")
        # Creating error message field
        self.__error_message = Label(self.__game_window, background="white", relief=RAISED, width=40, height=2,
                                     foreground="red")

        # Creating Label and entry and button: for remove player:
        self.__remove_label = Label(self.__game_window, text="Type quitting player:", background="cyan", relief=RAISED,
                                    width=20, height=2)
        self.__choose_player_removed = Entry(self.__game_window, borderwidth=8, width=20)
        self.__remove_chosen = Button(self.__game_window, text="Remove ⌫", relief=RAISED,
                                      width=20, height=1, command=self.remove_player,
                                      background="Black", foreground="white")

        # Placing the elements
        # Placing the header on the top
        self.__header.grid(row=0, column=0, sticky=W+N+E, columnspan=10, rowspan=1)

        # Placing all the headers: (Receiver and giver are placed in method)
        self.__header_player.grid(row=1, column=0, sticky=E+N, columnspan=2, rowspan=1)
        self.__header_money.grid(row=1, column=2, sticky=N, columnspan=2, rowspan=1)
        self.__transaction_amount_header.grid(row=3, column=4, columnspan=2, sticky=E+N+W)
        self.__remove_label.grid(row=1, column=8, sticky=E+N+W, columnspan=2, rowspan=1)

        # Place entrybox
        self.__transfer_amount.grid(row=3, column=6, columnspan=2, sticky=E+N+W)
        # Place entrybox for player to be removed
        self.__choose_player_removed.grid(row=2, column=8, sticky=E + N + W,
                                          columnspan=2, rowspan=1)
        # Place removal button
        self.__remove_chosen.grid(row=3, column=8, sticky=E + N + W,
                                  columnspan=2, rowspan=1)

        # Buttons for money interactions
        self.__transaction_transfer_button.grid(row=4, column=6, columnspan=2, sticky=E+N+W)
        self.__rotational_money_add_button.grid(row=4, column=4, columnspan=2, sticky=E+N+W)

        self.__error_message.grid(row=5, column=4, columnspan=4, sticky=E+N+W)
        # Using methods for building
        # Using player names printer and money amount printer to point out staring situation:
        self.player_names_printer()

        self.funds_available()

        # Player dropdown manus printer:

        self.__funds_giver = self.player_drop_menus(4, 1)  # Creating giver menu. Placing in 4. column
        self.__funds_receiver = self.player_drop_menus(6, 1)  # Creating receiver menu. Placing in 6. column

        self.__game_window.mainloop()

    def player_names_printer(self):
        """
        Prints out all the player names:
        :return: None
        """
        # Printing 8 empty boxes for players:
        for i in range(0, self.__player_numbers):

            # The first describes what to draw. (i + 1 for upping line numbers)
            player_line_numbers = Label(self.__game_window, text="", background="light yellow", relief=RAISED,
                                        width=20, height=2)
            # Placing them from 1 to amount of players. rows 2-10
            player_line_numbers.grid(row=2 + i, column=0, sticky=N + E + W, columnspan=2)

        # Printing all player names in window.
        for current_player in self.__player_wallet:

            index = list(self.__player_wallet.keys()).index(current_player)  # Getting index for placements

            show_player = Label(self.__game_window, text=current_player, background="light yellow", relief=RAISED,
                                width=20, height=2)  # Draw playername

            show_player.grid(row=2+index, column=0, sticky=N, columnspan=2, rowspan=1)  # Placing according to index

    def funds_available(self):
        """
        Prints out total of player's funds
        :return:
        """
        for i in range(0, self.__player_numbers):

            # The first describes what to draw. (i + 1 for upping line numbers)
            player_line_numbers = Label(self.__game_window, text="", background="light yellow", relief=RAISED,
                                        width=20, height=2)
            # Placing them from 1 to amount of players. rows 2-10
            player_line_numbers.grid(row=2 + i, column=2, sticky=N + E + W, columnspan=2)

        # Creating a loop that prints money per player
        for current_player in self.__player_wallet:
            index = list(self.__player_wallet).index(current_player)  # Getting index number here.

            current_players_funds = f"{self.__player_wallet[current_player]:,} "  # Creating str format in variable
            show_player = Label(self.__game_window, text=current_players_funds,
                                background="light yellow", relief=RAISED, width=20, height=2)  # Print data

            show_player.grid(row=2+index, column=2, sticky=N, columnspan=2, rowspan=1)  # Where to print. + 1 per player

    def player_drop_menus(self, l_col, l_row):
        """
        Creating drop menu that contains all players and bank option
        :param l_col: Placement in column for grid
        :param l_row: Placement in row for grid
        :return: Chosen option bunker
        """
        # Finding bank name
        bank_index_number = self.__player_names.index("Bank")

        # Setting datatype of the menu:
        clicked_txt = StringVar()

        # Setting initial value to menu:
        clicked_txt.set(self.__player_names[bank_index_number])

        # Setting menu itself
        player_menu = OptionMenu(self.__game_window, clicked_txt, *self.__player_names)
        player_menu.configure(width=20, background="red")

        # setting headers. If header location is 4 set up giver and if it is 6 set up receiver
        header_txt = Label(self.__game_window, background="cyan", relief=RAISED, width=20, height=2)

        if l_col == 6:
            header_txt.configure(text="Receiver:")

        elif l_col == 4:
            header_txt.configure(text="Payer:")

        # Placing the menu in the grid according to given values:
        header_txt.grid(column=l_col, row=l_row, columnspan=2, sticky=E+N+W)
        player_menu.grid(column=l_col, row=l_row+1, columnspan=2, sticky=E+N+W)

        return clicked_txt

    def transfer_funds(self):
        """
        Transfer funds between players and the bank
        :return: None
        """
        # Zeroing error message
        self.__error_message.configure(text="")

        # Getting amount of money to be transferred
        # Firstly we have to check if money is given in correctional form:
        try:
            # Remove possible spaces and commas from given sum
            money_tbm_without_spaces_a_commas = self.__transfer_amount.get().replace(" ", "").replace(",", "")

            money_to_be_moved = int(money_tbm_without_spaces_a_commas)  # If money is in int form save it to variable
        except ValueError:
            self.__error_message.configure(text="Input has to be integer")
            return

        # Setting receiver, giver and the bank
        receiver = self.__funds_receiver.get()
        giver = self.__funds_giver.get()
        bank = "Bank"

        # Checking if bank is giver and receiver
        if giver == bank and receiver == bank:
            self.__error_message.configure(text="Bank cant be giver and donor")

        # Checking if giver=receiver are not the same:
        elif giver == receiver:
            self.__error_message.configure(text="Giver cant be receiver")

        # if giver is bank just add the money no necessary things to be done
        elif giver == bank:
            self.__player_wallet[receiver] += money_to_be_moved

        # After bank has possibly given away the money. Need to check if player
        # Has sufficient funds
        elif self.__player_wallet[giver] < money_to_be_moved:
            self.__error_message.configure(text=f"{giver} has insufficient funds")

        # If receiver is bank just remove the money from the pool
        elif receiver == bank:
            self.__player_wallet[giver] -= money_to_be_moved

        # If player has no problems in making transaction make it true:
        else:
            self.__player_wallet[giver] -= money_to_be_moved
            self.__player_wallet[receiver] += money_to_be_moved

        # Print available funds:
        self.funds_available()

    def add_rotational_money(self):
        """
        Adds rotational money 2 millions to receiver player
        :return:
        """
        # Zeroing error message
        self.__error_message.configure(text="")

        # Get values for receiver and giver(It has to be bank)
        receiver = self.__funds_receiver.get()
        giver = self.__funds_giver.get()
        bank = "Bank"
        money_to_be_added = 2000000

        # Checks if bank is accidentally receiving rotational:
        if receiver == bank:
            self.__error_message.configure(text="Bank can't be receiving rotational funds")

        # Checks if rotational payer is anybody else than the bank
        elif giver != bank:
            self.__error_message.configure(text="Bank is the only source of rotational funds")

        # Add received money if everything else is okay
        else:
            self.__player_wallet[receiver] += money_to_be_added

        # Prints out diffrences after adding the money
        self.funds_available()

    def remove_player(self):
        """
        Removes chosen player from player's input, from button.
        :return: None
        """

        # Getting user's input and clearing the error message:
        player_name = self.__choose_player_removed.get()
        self.__error_message.configure(text="")

        # If field is empty show error message below
        if player_name == "":
            self.__error_message.configure(text="Field is empty")

        # If user tries to remove user that is not in the system show error message below
        elif player_name not in list(self.__player_wallet):
            self.__error_message.configure(text="Player not found")

        # Otherwise all is well and remove chosen user
        else:
            self.__player_wallet.pop(player_name)  # Remove this user
            self.__player_names.remove(player_name)  # Remove player from drop menus list also
            self.player_names_printer()  # Update list
            self.funds_available()  # Remove players funds as well

            # Upgrade drop menus:
            self.__funds_giver = self.player_drop_menus(4, 1)  # Upgrading giver menu. Placing in 4. column
            self.__funds_receiver = self.player_drop_menus(6, 1)  # Upgrading receiver menu. Placing in 6. column

            # Clear input always
            self.__choose_player_removed.delete(0, END)

        # This option also checks if somebody has won the game:
        if len(list(self.__player_wallet)) == 1:
            winner_txt = f"WINNER IS {list(self.__player_wallet)[0]}"

            # ENDS THIS SCREEN!
            self.__game_window.destroy()
            # Show up winner screen
            winner_screen.Display_winner(winner_txt)


def form_player_wallet(players_in_list, money_in_str):
    """
    This function gets values and forms a dict from them
    :param players_in_list: All added players in list form
    :param money_in_str: Chosen default money to all the players
    :return: Dict: Keys: Players and values: Money
    """

    player_wallet = {}  # Creating empty dict for data

    money_amount = money_in_str.replace(" ", "").replace("M", "")  # Replacing empty chars and "M" with no space
    money_amount_int = int(money_amount)  # Transforming into int

    # This loop goes through all the players and add chosen money in their values
    for current_player in players_in_list:
        player_wallet[current_player] = money_amount_int

    return player_wallet  # Final dict


def main():
    # Starting intro screen:

    intro_gui = setting_menu.PlayerMenu()
    players_in_list, money_in_str = intro_gui.get_key_values()  # Importing values
    # This is just meant for main program debugging
    """
    players_in_list = ["Jaakko", "Martti", "Meiju", "Miina"]
    money_in_str = "15 000 000M"
    """

    player_wallet = form_player_wallet(players_in_list, money_in_str)  # Forming wallet with dict.
    # Starting the main program:
    GameGraphics(player_wallet)  # Use graphicps


if __name__ == "__main__":
    main()
