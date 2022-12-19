"""
This is the starting screen of monopoly electric banking version 0.1

This part includes Add players, remove players, set start money, start game functionalities.
It also shows current players in green backround and free slots with red backrounds. It  has also visual error screen
There will be red markings if user tries to do stupid things.

Creator: Samuli Tolvanen
"""

from tkinter import *  # Importing tkinter


class PlayerMenu:

    def __init__(self):
        """
        Set basic GUI.
        """

        # creating an ampty list for all the players:
        self.__all_players = []

        # Defining menu_window
        self.__menu_window = Tk()

        # Creating header:
        self.__header = Label(self.__menu_window, text="Monopoly Electric Banking System v.0.1", font=12,
                              background="yellow", relief=RAISED, borderwidth=5)

        # Creating add player inputs
        self.__info_txt_addplayer = Label(self.__menu_window, text="Add playername here:", borderwidth=3, relief=RAISED)
        self.__addplayer = Entry(self.__menu_window, borderwidth=5)

        # Creating buttons for add new player
        self.__addplayer_button = Button(self.__menu_window, text=" + Add player + ", font=10, background="Blue",
                                         foreground="white", command=self.add_player)

        #   creating new button functionality that allows removing players
        self.__removeplayer_button = Button(self.__menu_window, text="- Remove player -", font=8, background="Red",
                                            foreground="white", command=self.remove_player)

        # Creating start game button!!
        self.__start_game_button = Button(self.__menu_window, text="** Start game **", font=8, background="navy",
                                          foreground="white", command=self.start_game)

        # Creating error screen for user: Contains header and info box.
        self.__show_error = Label(self.__menu_window, text="", borderwidth=2, relief=RAISED, foreground="Red",
                                  width=20)
        self.__show_error_info = Label(self.__menu_window, text="This is the problem:", width=20)

        # Placements in grid:
        self.__header.grid(row=0, column=0, sticky=W+N+E, columnspan=4)  # Main header in first row and col

        self.__info_txt_addplayer.grid(row=1, column=0, sticky=W+N+E)  # Info text in second row and first col
        self.__addplayer.grid(row=1, column=2, sticky=W+N+E)  # Place for name in second row and third col
        self.__show_error_info.grid(row=9, column=2, sticky=W+E+S, columnspan=2)
        self.__show_error.grid(row=10, column=2, sticky=W+E+N, columnspan=2)

        # All the buttons
        self.__addplayer_button.grid(row=2, column=0, sticky=N+W+E, columnspan=4, rowspan=2)
        self.__removeplayer_button.grid(row=4, column=2, sticky=W+N+E, columnspan=2, rowspan=1)
        self.__start_game_button.grid(row=11, column=2, sticky=W+S+E, columnspan=2, rowspan=1)

        # First running creates 8 empty boxes with numbers for names. When something is to added runs again from button
        self.show_players()

        # Create dropdown menu:
        self.set_startmoney()

        self.__menu_window.mainloop()

    def add_player(self):
        """
        This is used to save player name in a list where it can be. Activated by add player button.
        :return: None
        """
        # Getting user's input and clearing the error message:
        player_name = self.__addplayer.get()
        self.__show_error.configure(text="")

        # Checking if there is any empty inputs and ignoring them. Also checks if input is alredy there.
        # Also makes sure that maxium number of players is not higher than 8
        if player_name == "":
            self.__show_error.configure(text="Field is empty")

        elif player_name in self.__all_players:
            self.__show_error.configure(text="Player is already there")

        elif len(self.__all_players) == 8:
            self.__show_error.configure(text="Max players: 8")

        else:
            # Saving user's input in the list:
            self.__all_players.append(player_name)

            # Show players/ Refresh players
            self.show_players()

        # Clear input always
        self.__addplayer.delete(0, END)

    def remove_player(self):
        """
        Removes chosen player from player's input, from button.
        :return: None
        """
        # Getting user's input and clearing the error message:
        player_name = self.__addplayer.get()
        self.__show_error.configure(text="")

        # If field is empty show error message below
        if player_name == "":
            self.__show_error.configure(text="Field is empty")

        # If user tries to remove user that is not in the system show error message below
        elif player_name not in self.__all_players:
            self.__show_error.configure(text="Player not found")

        # Otherwise all is well and remove chosen user
        else:
            self.__all_players.remove(player_name)  # Remove this user
            self.show_players()  # Update list

        # Clear input always
        self.__addplayer.delete(0, END)

    def start_game(self):
        """
        This closes this current window and opens banking window.
        :return: None
        """

        # Checks if there is only one player and prevents user from starting game
        if len(self.__all_players) < 2:
            self.__show_error.configure(text="Minium players: 2")

        # If user has not set money it has to be set
        elif self.__clicked_txt.get() == "Choose start money":
            self.__show_error.configure(text="Missing start money")

        # If all is well let the banking begin!
        else:
            self.__menu_window.destroy()

    def show_players(self):
        """
        Prints current players in GUI. Also presents slots for players Activated by add player button.
        Refreshes base and players every time when it is activated.
        :return:None
        """

        # Here we create a loop that repeats 8 times and creates empty boxes with numbers
        for i in range(0, 8):

            # The first describes what to draw. (i + 1 for upping line numbers)
            player_line_numbers = Label(self.__menu_window, text=f"{i + 1}.", relief=RAISED, borderwidth=1,
                                               width=18, height=2, background="light salmon")
            # Placing them from 1 to 8. rows 5-13
            player_line_numbers.grid(row=4 + i, column=0, sticky=N + E + W, columnspan=2)

        # Printing name box on top of number box. Choosing this that we don't need to customize values
        # when we add and remove names.
        for current_name in self.__all_players:

            # Getting index value for lining label correctly.
            index_value = self.__all_players.index(current_name)

            # Creating new players list label and and placing it acording index.

            show_players = Label(self.__menu_window, text=f"{index_value + 1}. {current_name}"
                                        , relief=RAISED, borderwidth=1, width=18, height=2, background="lawn green")
            # Placing from 1 to 8
            show_players.grid(row=4+index_value, column=0, sticky=N+E+W, columnspan=2)

    def set_startmoney(self):
        """
        This method is printing drop menu in user interface. It has variable options from 10 million to 20 million.
        :return: None
        """

        # Options for the menu setting. Contains diffrent amount of money peresets. First is standard monopoly:
        menu_options = ["Choose start money", "15 000 000M", "20 000 000M", "10 000 000M"]

        # Setting datatype of the menu:
        self.__clicked_txt = StringVar()

        # Setting initial text:
        self.__clicked_txt.set(menu_options[0])

        # Create dropdown itself:
        money_menu = OptionMenu(self.__menu_window, self.__clicked_txt, *menu_options)

        # Placing drop menu accordingly.
        money_menu.grid(row=8, column=2, columnspan=2, sticky=W+N+E)

    def get_key_values(self):
        """
        This method gets all the key values from this scripts outputs.
        :return: List of all players, chosen money amount
        """

        # Here we are exporting important values to the main program.
        return self.__all_players, self.__clicked_txt.get()

