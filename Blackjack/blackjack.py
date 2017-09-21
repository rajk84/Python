import random
import tkinter


def load_images(card_images): # loads all images to cards list along with its values
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6: # version dependency on image extensions to be loaded
        extension = 'png'
    else:
        extension = 'ppm'

    # for each suit, retrieve image for the cards
    for suit in suits:
        # first the number cards from 1 to 10
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))
        # next the face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame): # gets a card from deck list to dealer/player whoever calls for it
    # pop the next card from the pack of cards
    next_card = deck.pop(0)
    # add image to label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left') # adds image of extracted card to frame
    return next_card[0] # return card value extracted


def deal_dealer(): # called when dealer button is pressed
    # make sure to mention global variables to be used
    global dealer_score
    card_value = deal_card(dealer_card_frame) # card value extracted from deck for dealer
    dealer_hand.append(card_value) # add card value to dealer_hand list
    dealer_score = score_hand(dealer_hand) # gets score from dealer_hand list
    dealer_score_label.set(dealer_score) # sets dealer score to dealer score label
    set_msg('D') # set message as if dealer is still playing


def deal_player(): # called when player button is pressed
    # make sure to mention global variables to be used
    global player_score
    card_value = deal_card(player_card_frame) # card value extracted from deck for player
    player_hand.append(card_value) # add card value to player_hand list
    player_score = score_hand(player_hand) # gets score from player_hand list
    player_score_label.set(player_score) # sets player score to player score label
    set_msg('P') # set message as if player is still playing


def score_hand(hand): # check score of dealer or player cards in hand
    score = sum(hand)
    if 1 in hand and (score + 10) <= 21: # check if Ace is in hand and that total score is <=21
        score += 10
    return score


def set_msg(from_where): # set message and disable buttons from where it is called
    if from_where == 'P': # player is playing
        if player_score < 21:
            result_txt.set('Player Turn!')
        elif player_score == 21:
            result_txt.set('Player Black Jack!')
            disable_all_buttons()
        else:
            result_txt.set('Dealer wins!')
            disable_all_buttons()
    elif from_where == 'D': # dealer is playing
        if dealer_score < 21:
            result_txt.set('Dealer Turn!')
        elif dealer_score == 21:
            result_txt.set('Dealer Black Jack!')
            disable_all_buttons()
        else:
            result_txt.set('Player wins!')
            disable_all_buttons()
    else: # dealer ended the game to check for final results
        if dealer_score < player_score:
            result_txt.set('Player wins!')
            disable_all_buttons()
        elif player_score < dealer_score:
            result_txt.set('Dealer wins!')
            disable_all_buttons()
        else:
            result_txt.set("It's a Tie!")
            disable_all_buttons()


def player_done(): # player clicked done button
    # enable dealer buttons and disable player buttons
    dealer_button.configure(state='active')
    dealer_done_button.configure(state='active')
    player_button.configure(state='disabled')
    player_done_button.configure(state='disabled')
    set_msg('D') # set message as dealer is playing


def dealer_done(): # dealer clicked done button
    disable_all_buttons() # disable all buttons
    set_msg('X') # set message as dealer chose to end the game


def disable_all_buttons(): # disable all buttons except restart button
    dealer_button.configure(state='disabled')
    dealer_done_button.configure(state='disabled')
    player_button.configure(state='disabled')
    player_done_button.configure(state='disabled')


def reset_game(): # reset the game
    # define global variables to be used
    global deck
    global player_score
    global dealer_score
    global player_hand
    global dealer_hand
    # Load deck and shuffle the cards
    deck = list(cards)
    random.shuffle(deck)
    # reset dealer and player card frames to clear all cards
    for loaded_cards in dealer_card_frame.winfo_children():
        loaded_cards.destroy()
    for loaded_cards in player_card_frame.winfo_children():
        loaded_cards.destroy()
    player_score = 0
    dealer_score = 0
    player_hand = []
    dealer_hand = []
    player_score_label.set(player_score)
    dealer_score_label.set(dealer_score)
    # reveal 2 player cards and 1 dealer card to start with
    deal_player()
    deal_player()
    deal_dealer()
    dealer_button.configure(state='disabled')
    dealer_done_button.configure(state='disabled')
    player_button.configure(state='active')
    player_done_button.configure(state='active')
    set_msg('P')

mainwindow = tkinter.Tk()

# setup screen frame for dealer and player
mainwindow.title('BlackJack')
mainwindow.geometry('640x480')
mainwindow.configure(background='green')

# global variables for the game
dealer_hand = []  # holds values of cards for dealer
player_hand = []  # holds values of cards for player

# first row to hold game messages
result_txt = tkinter.StringVar()
result = tkinter.Label(mainwindow, textvariable=result_txt)
result.grid(row=0, column=0, columnspan=3)

# second row to hold card frame for scores and card images to show on screen
card_frame = tkinter.Frame(mainwindow, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

# Dealer string and his score
dealer_score_label = tkinter.IntVar()
dealer_score = 0
tkinter.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)

# embed dealer card frame within card frame to hold card images for dealer
dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

# player string and his score
player_score_label = tkinter.IntVar()
player_score = 0
tkinter.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)

# embed player card frame within card frame to hold card image for player
player_card_frame = tkinter.Frame(card_frame, background='green')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# button frame to hold buttons for dealer and player
button_frame = tkinter.Frame(mainwindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

# dealer button with command to call deal_dealer function
dealer_button = tkinter.Button(button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)

# player button with command to call deal_player function
player_button = tkinter.Button(button_frame, text='Player', command=deal_player)
player_button.grid(row=0, column=1)

# reset/restart button
restart_button = tkinter.Button(button_frame, text='Restart', command=reset_game)
restart_button.grid(row=0, column=2,rowspan=2,sticky='ns')

# done buttons for player and dealer to finish pulling cards from deck
dealer_done_button = tkinter.Button(button_frame, text='Done', command=dealer_done)
dealer_done_button.grid(row=1, column=0,sticky='ew')
player_done_button = tkinter.Button(button_frame, text='Done', command=player_done)
player_done_button.grid(row=1, column=1,sticky='ew')


# load cards
cards = []
load_images(cards)
deck = []

reset_game()

mainwindow.mainloop()
