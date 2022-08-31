# Gisele T., Yanira M., Mohamed B.
# 11/30/2021
# Hidden Movie Review Survey Final Project

import sys
import pandas as pd

""" Please have the file "pre-Hidden Movie Critic Survey TEST.xlsx"--
under the same folder as your jupyter/pyCharm so it can read """


# Mohamed's Part
hms = pd.read_excel('pre-Hidden Movie Critic Survey TEST.xlsx')

""" Drama/Romance Questions """
def dramaRomance(callback):
    # Central 1 Response Average
    if callback == 1:
        select_range1 = hms.iloc[:1]
        c_avg1a = select_range1.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return c_avg1a
    # Central 2 Response Average
    elif callback == 2:
        select_range2 = hms.iloc[1:2]
        c_avg1b = select_range2.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return c_avg1b
    # Central 3 Response Average
    elif callback == 3:
        select_range3 = hms.iloc[2:3]
        c_avg1c = select_range3.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return c_avg1c
    # Peripheral 1 Response Average
    elif callback == 4:
        select_range4 = hms.iloc[3:4]
        p_avg1a = select_range4.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return p_avg1a
    # Peripheral 2 Response Average
    elif callback == 5:
        select_range5 = hms.iloc[4:5]
        p_avg1b = select_range5.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return p_avg1b
    # Peripheral 3 Response Average
    elif callback == 6:
        select_range6 = hms.iloc[5:6]
        p_avg1c = select_range6.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return p_avg1c
    # Intention 1 Response Average
    elif callback == 7:
        select_range7 = hms.iloc[6:7]
        i_avg1a = select_range7.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return i_avg1a
    # Intention 2 Response Average
    elif callback == 8:
        select_range8 = hms.iloc[7:8]
        i_avg1b = select_range8.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return i_avg1b


""" Action/Sci-Fi Questions """
def actionSciFi(callback):
    # Central 1 Response Average
    if callback == 1:
        select_range9 = hms.iloc[8:9]
        c_avg2a = select_range9.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return c_avg2a
    # Central 2 Response Average
    elif callback == 2:
        select_range10 = hms.iloc[9:10]
        c_avg2b = select_range10.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return c_avg2b
    # Central 3 Response Average
    elif callback == 3:
        select_range11 = hms.iloc[10:11]
        c_avg2c = select_range11.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return c_avg2c
    # Peripheral 1 Response Average
    elif callback == 4:
        select_range12 = hms.iloc[11:12]
        p_avg2a = select_range12.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return p_avg2a
    # Peripheral 2 Response Average
    elif callback == 5:
        select_range13 = hms.iloc[12:13]
        p_avg2b = select_range13.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return p_avg2b
    # Peripheral 3 Response Average
    elif callback == 6:
        select_range14 = hms.iloc[13:14]
        p_avg2c = select_range14.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return p_avg2c
    # Intention 1 Response Average
    elif callback == 7:
        select_range15 = hms.iloc[14:15]
        i_avg2a = select_range15.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return i_avg2a
    # Intention 2 Response Average
    elif callback == 8:
        select_range16 = hms.iloc[15:16]
        i_avg2b = select_range16.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return i_avg2b


""" Horror/Thriller Questions """
def horrorThriller(callback):
    # Central 1 Response Average
    if callback == 1:
        select_range17 = hms.iloc[16:17]
        c_avg3a = select_range17.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return c_avg3a
    # Central 2 Response Average
    elif callback == 2:
        select_range18 = hms.iloc[17:18]
        c_avg3b = select_range18.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return c_avg3b
    # Central 3 Response Average
    elif callback == 3:
        select_range19 = hms.iloc[18:19]
        c_avg3c = select_range19.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return c_avg3c
    # Peripheral 1 Response Average
    elif callback == 4:
        select_range20 = hms.iloc[19:20]
        p_avg3a = select_range20.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return p_avg3a
    # Peripheral 2 Response Average
    elif callback == 5:
        select_range21 = hms.iloc[20:21]
        p_avg3b = select_range21.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return p_avg3b
    # Peripheral 3 Response Average
    elif callback == 6:
        select_range22 = hms.iloc[21:22]
        p_avg3c = select_range22.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return p_avg3c
    # Intention 1 Response Average
    elif callback == 7:
        select_range23 = hms.iloc[22:23]
        i_avg3a = select_range23.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return i_avg3a
    # Intention 2 Response Average
    elif callback == 8:
        select_range24 = hms.iloc[23:24]
        i_avg3b = select_range24.drop(['Movie Genre', 'Question'], axis = 1).mean().mean()
        return i_avg3b



#Yanira/Gisele's Part
def main_menu():
    menu = 0
    option = 0
    back_menu = 0
    run = True

    '''General Menu'''
    while menu != 4:
        print("-"*50)
        print(f"\033[95mWelcome to Hidden Movie Review results!\n"
              f"Please select which review result you would like to see:\n"
              f"\033[94m1)Hidden Movie Review 1\n"
              f"2)Hidden Movie Review 2\n"
              f"3)Hidden Movie Review 3\n"
              f"4)Exit")
        menu = int(input("\033[92m>>"))

        '''Drama/Romance Responses'''
        if menu == 1:
            print("-"*50)
            print(f"Hidden Movie Review 1\n"
                  f"\033[95mGenre: Drama, Romance\n"
                  f"Which question would you like to see?\n"
                  f"\033[94m1)Were these reviews informative for them?\n"
                  f"2)Were these reviews helpful to them?\n"
                  f"3)Did these reviews persuaded them?\n"
                  f"4)Did this movie catch their interest?\n"
                  f"5)How do they felt about the credibility of the reviews?\n"
                  f"6)To what extent do the reviewers' opinions matter to them?\n"
                  f"7)Would they watch this movie?\n"
                  f"8)Would they recommend movie this to someone else? \n"
                  f"9) Main Menu")
            option = int(input("\033[92m>>"))
            if option == 1:
                print(f'Were these reviews informative for them?:\n'
                      f'Average response: {dramaRomance(1)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 2:
                print(f'Were these reviews helpful to them?:\n'
                      f'Average response: {dramaRomance(2)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 3:
                print(f'Did these reviews persuaded them?:\n'
                      f'Average response: {dramaRomance(3)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 4:
                print(f'Did this movie catch their interest?:\n'
                      f'Average response: {dramaRomance(4)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 5:
                print(f'How do they felt about the credibility of the reviews?:\n'
                      f'Average response: {dramaRomance(5)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 6:
                print(f"To what extent do the reviewers' opinions matter to them?:\n"
                      f'Average response: {dramaRomance(6)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 7:
                print(f"Would they watch this movie?:\n"
                      f'Average response: {dramaRomance(7)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 8:
                print(f"Would they recommend movie this to someone else?:\n"
                      f'Average response: {dramaRomance(8)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 9:
                menu = ()

        '''Action/Sc-fi Responses'''
        if menu == 2:
            print("-"*50)
            print(f"Hidden Movie Review 2\n"
                  f"\033[95mGenre: Action, Sci-fi, Adventure\n"
                  f"Which question would you like to see?\n"
                  f"\033[94m1)Were these reviews informative for them?\n"
                  f"2)Were these reviews helpful to them?\n"
                  f"3)Did these reviews persuaded them?\n"
                  f"4)Did this movie catch their interest?\n"
                  f"5)How do they felt about the credibility of the reviews?\n"
                  f"6)To what extent do the reviewers' opinions matter to them?\n"
                  f"7)Would they watch this movie?\n"
                  f"8)Would they recommend movie this to someone else? \n"
                  f"9) Main Menu")
            option = int(input("\033[92m>>"))
            if option == 1:
                print(f'Were these reviews informative for them?:\n'
                      f'Average response: {actionSciFi(1)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 2:
                print(f'Were these reviews helpful to them?:\n'
                      f'Average response: {actionSciFi(2)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 3:
                print(f'Did these reviews persuaded them?:\n'
                      f'Average response: {actionSciFi(3)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 4:
                print(f'Did this movie catch their interest?:\n'
                      f'Average response: {actionSciFi(4)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 5:
                print(f'How do they felt about the credibility of the reviews?:\n'
                      f'Average response: {actionSciFi(5)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 6:
                print(f"To what extent do the reviewers' opinions matter to them?:\n"
                      f'Average response: {actionSciFi(6)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 7:
                print(f"Would they watch this movie?:\n"
                      f'Average response: {actionSciFi(7)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 8:
                print(f"Would they recommend movie this to someone else?:\n"
                      f'Average response: {actionSciFi(8)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 9:
                menu = ()

        '''Horror/Thriller Responses'''
        if menu == 3:
            print("-"*50)
            print(f"Hidden Movie Review 3\n"
                  f"Genre: Horror, Mystery, Thriller\n"
                  f"Which question would you like to see?\n"
                  f"\033[94m1)Were these reviews informative for them?\n"
                  f"2)Were these reviews helpful to them?\n"
                  f"3)Did these reviews persuaded them?\n"
                  f"4)Did this movie catch their interest?\n"
                  f"5)How do they felt about the credibility of the reviews?\n"
                  f"6)To what extent do the reviewers' opinions matter to them?\n"
                  f"7)Would they watch this movie?\n"
                  f"8)Would they recommend movie this to someone else? \n"
                  f"9) Main Menu")
            option = int(input("\033[92m>>"))
            if option == 1:
                print(f'Were these reviews informative for them?:\n'
                      f'Average response: {horrorThriller(1)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 2:
                print(f'Were these reviews helpful to them?:\n'
                      f'Average response: {horrorThriller(2)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 3:
                print(f'Did these reviews persuaded them?:\n'
                      f'Average response: {horrorThriller(3)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 4:
                print(f'Did this movie catch their interest?:\n'
                      f'Average response: {horrorThriller(4)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 5:
                print(f'How do they felt about the credibility of the reviews?:\n'
                      f'Average response: {horrorThriller(5)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 6:
                print(f"To what extent do the reviewers' opinions matter to them?:\n"
                      f'Average response: {horrorThriller(6)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 7:
                print(f"Would they watch this movie?:\n"
                      f'Average response: {horrorThriller(7)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 8:
                print(f"Would they recommend movie this to someone else?:\n"
                      f'Average response: {horrorThriller(8)} out of 5\n'
                      f'Input anything to go Main Menu\n')
                back_menu = int(input(">>"))
            elif option == 9:
                menu = ()

        '''Exit'''
        if menu == 4:
            print("-"*50)
            print("Alright! See you soon!")
            sys.exit()


main_menu()

