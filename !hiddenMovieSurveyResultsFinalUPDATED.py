# Gisele T., Yanira M., Mohamed B.
# 12/06/2021
# Hidden Movie Review Survey Final Project

import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

""" Please have the file "pre-Hidden Movie Critic Survey TEST.xlsx" along with the images --
under the same folder as your jupyter/pyCharm so this program can read the necessary files """

hms = pd.read_excel('pre-Hidden Movie Critic Survey TEST.xlsx')


def findMean(number1, number2):
    return hms.iloc[number1:number2].drop(['Movie Genre', 'Question'], axis=1).mean().mean()


# Image Sets
img1 = mpimg.imread('dR1.PNG')
img2 = mpimg.imread('dR2.PNG')
img3 = mpimg.imread('dR3.PNG')
img4 = mpimg.imread('aS1.PNG')
img5 = mpimg.imread('aS2.PNG')
img6 = mpimg.imread('aS3.PNG')
img7 = mpimg.imread('hT1.PNG')
img8 = mpimg.imread('hT2.PNG')
img9 = mpimg.imread('hT3.PNG')


def displayReviews(img_name1, img_name2, img_name3):
    # Figure Size
    fig = plt.figure(figsize=(5, 5))
    # Rows/Column Values
    rows = 2
    columns = 2
    # First Image
    fig.add_subplot(rows, columns, 1)
    plt.imshow(img_name1)
    plt.axis('off')
    plt.title("First Review")
    # Second Image
    fig.add_subplot(rows, columns, 2)
    plt.imshow(img_name2)
    plt.axis('off')
    plt.title("Second Review")
    # Third Image
    fig.add_subplot(rows, columns, 3)
    plt.imshow(img_name3)
    plt.axis('off')
    plt.title("Third Review")
    # Show Window
    plt.show()


""" Drama/Romance Questions """
def dramaRomance(callback):
    if callback == callback:
        return findMean(callback - 1, callback)
    else:
        print("Error")


""" Action/Sci-Fi Questions """
def actionSciFi(callback):
    if callback == callback:
        return findMean(callback + 7, callback + 8)
    else:
        print("Error")


""" Horror/Thriller Questions """
def horrorThriller(callback):
    if callback == callback:
        return findMean(callback + 15, callback + 16)
    else:
        print("Error")


'''Questions Functions'''
Q1 = "1) Were these reviews informative for them?"
Q2 = "2) Were these reviews helpful to them?"
Q3 = "3) Did these reviews persuaded them?"
Q4 = "4) Did this movie catch their interest?"
Q5 = "5) How do they felt about the credibility of the reviews?"
Q6 = "6) To what extent do the reviewers' opinions matter to them?"
Q7 = "7) Would they watch this movie?"
Q8 = "8) Would they recommend movie this to someone else?"
N9 = "9) Main Menu"
m_exit = 'Input a number to go back to main menu'
Questions_Menu = f"""Which questions' results would you like to see?
 {Q1}\n {Q2}\n {Q3}\n {Q4}\n {Q5}\n {Q6}\n {Q7}\n {Q8}\n {N9}"""


""" Graph """
def barGraph(Question, questionNumber):
    x_values = ["Drama/Romance", "Action/Sci-Fi", "Horror/Thriller"]
    y_values = [dramaRomance(questionNumber), actionSciFi(questionNumber), horrorThriller(questionNumber)]

    plt.bar(x_values, y_values)
    plt.title(Question)
    plt.xlabel('***Movie Genres***')
    plt.ylabel('***Average***')
    return plt.show()


def avg_result(genre, Question, questionNumber):
    print("*"*25, 'RESULTS', "*"*25)
    print(f'{Question}:\n'
          f'Average response: {genre} out of 5\n'
          f'Would you like to compare this to all genres?\n'
          f'1=Yes / 2=No')
    compare = int(input(">> "))
    if compare == 1:
        barGraph(Question, questionNumber)
        print(m_exit)
    elif compare == 2:
        print(m_exit)
    back_menu = int(input(f">>"))


def main_menu():
    '''Int Variables'''
    menu = 0
    option = 0
    back_menu = 0
    run = True

    '''General Menu'''
    print(f"\033[95mWelcome to Hidden Movie Review results! v.2")
    while menu != 4:
        print("-" * 50)
        print(f"Please select which reviews you would like to see:\n"
              f"\033[94m 1) Hidden Movie Review 1\n"
              f" 2) Hidden Movie Review 2\n"
              f" 3) Hidden Movie Review 3\n"
              f" 4) Exit")
        menu = int(input("\033[92m>> "))

        '''Drama/Romance Responses'''
        if menu == 1:
            print("-" * 50)
            displayReviews(img1, img2, img3)
            print(f"Hidden Movie Review 1\n"
                  f"\033[95mGenre: Drama, Romance\n"
                  f"{Questions_Menu}")
            option = int(input("\033[92m>> "))
            if option == 1:
                avg_result(dramaRomance(option), Q1, option)
            elif option == 2:
                avg_result(dramaRomance(option), Q2, option)
            elif option == 3:
                avg_result(dramaRomance(option), Q3, option)
            elif option == 4:
                avg_result(dramaRomance(option), Q4, option)
            elif option == 5:
                avg_result(dramaRomance(option), Q5, option)
            elif option == 6:
                avg_result(dramaRomance(option), Q6, option)
            elif option == 7:
                avg_result(dramaRomance(option), Q5, option)
            elif option == 8:
                avg_result(dramaRomance(option), Q7, option)
            elif option == 9:
                menu = ()

        '''Action/Sc-fi Responses'''
        if menu == 2:
            print("-" * 50)
            displayReviews(img4, img5, img6)
            print(f"Hidden Movie Review 2\n"
                  f"{Questions_Menu}")
            option = int(input("\033[92m>> "))
            if option == 1:
                avg_result(actionSciFi(option), Q1, option)
            elif option == 2:
                avg_result(actionSciFi(option), Q2, option)
            elif option == 3:
                avg_result(actionSciFi(option), Q3, option)
            elif option == 4:
                avg_result(actionSciFi(option), Q4, option)
            elif option == 5:
                avg_result(actionSciFi(option), Q5, option)
            elif option == 6:
                avg_result(actionSciFi(option), Q6, option)
            elif option == 7:
                avg_result(actionSciFi(option), Q7, option)
            elif option == 8:
                avg_result(actionSciFi(option), Q8, option)
            elif option == 9:
                menu = ()

        '''Horror/Thriller Responses'''
        if menu == 3:
            print("-" * 50)
            displayReviews(img7, img8, img9)
            print(f"Hidden Movie Review 3\n"
                  f"Genre: Horror, Mystery, Thriller\n"
                  f"{Questions_Menu}\n")
            option = int(input("\033[92m>> "))
            if option == 1:
                avg_result(horrorThriller(option), Q1, option)
            elif option == 2:
                avg_result(horrorThriller(option), Q2, option)
            elif option == 3:
                avg_result(horrorThriller(option), Q3, option)
            elif option == 4:
                avg_result(horrorThriller(option), Q4, option)
            elif option == 5:
                avg_result(horrorThriller(option), Q5, option)
            elif option == 6:
                avg_result(horrorThriller(option), Q6, option)
            elif option == 7:
                avg_result(horrorThriller(option), Q7, option)
            elif option == 8:
                avg_result(horrorThriller(option), Q8, option)
            elif option == 9:
                menu = ()

        '''Exit'''
        if menu == 4:
            print("-" * 50)
            print("Alright! See you soon!")
            sys.exit()


main_menu()
