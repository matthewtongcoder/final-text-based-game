#note the game's "code order" is backwards in chronological order, because in Python, we need to define certain things before using them.

#here we are importing time for the stopwatch and playsound for all music and sound effects in the game.
import time
from playsound import playsound

#defining some ASCII Art to be used in other parts of the program.
(Welcome) = """
 _    _      _                              _____ _           _                     _            _                     
| |  | |    | |                            |  __ \ |         | |                   ( )          | |                    
| |  | | ___| | ___ ___  _ __ ___   ___    | |  \/ | __ _  __| |  _   _  ___  _   _|/ _ __ ___  | |__   ___ _ __ ___   
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \   | | __| |/ _` |/ _` | | | | |/ _ \| | | | | '__/ _ \ | '_ \ / _ \ '__/ _ \  
\  /\  /  __/ | (_| (_) | | | | | |  __/_  | |_\ \ | (_| | (_| | | |_| | (_) | |_| | | | |  __/ | | | |  __/ | |  __/_ 
 \/  \/ \___|_|\___\___/|_| |_| |_|\___(_)  \____/_|\__,_|\__,_|  \__, |\___/ \__,_| |_|  \___| |_| |_|\___|_|  \___(_)
                                                                   __/ |                                               
                                                                  |___/ 
"""

(Correct) = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⡿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠺⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠻⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣿⣷⣤⡀⠀⠀⣰⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣦⣼⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

(Congrats) = """
 .----------------. .----------------. .-----------------..----------------. .----------------. .----------------. .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |     ______   | | |     ____     | | | ____  _____  | | |    ______    | | |  _______     | | |      __      | | |  _________   | | |    _______   | | |              | |
| |   .' ___  |  | | |   .'    `.   | | ||_   \|_   _| | | |  .' ___  |   | | | |_   __ \    | | |     /  \     | | | |  _   _  |  | | |   /  ___  |  | | |      _       | |
| |  / .'   \_|  | | |  /  .--.  \  | | |  |   \ | |   | | | / .'   \_|   | | |   | |__) |   | | |    / /\ \    | | | |_/ | | \_|  | | |  |  (__ \_|  | | |     | |      | |
| |  | |         | | |  | |    | |  | | |  | |\ \| |   | | | | |    ____  | | |   |  __ /    | | |   / ____ \   | | |     | |      | | |   '.___`-.   | | |     | |      | |
| |  \ `.___.'\  | | |  \  `--'  /  | | | _| |_\   |_  | | | \ `.___]  _| | | |  _| |  \ \_  | | | _/ /    \ \_ | | |    _| |_     | | |  |`\____) |  | | |     | |      | |
| |   `._____.'  | | |   `.____.'   | | ||_____|\____| | | |  `._____.'   | | | |____| |___| | | ||____|  |____|| | |   |_____|    | | |  |_______.'  | | |     |_|      | |
| |              | | |              | | |              | | |              | | |              | | |              | | |              | | |              | | |     (_)      | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------'
"""

(TheEnd) = """                                                                               
                                                                                 _______       
           .              __.....__                     __.....__        _..._   \  ___ `'.    
         .'|          .-''         '.               .-''         '.    .'     '.  ' |--.\  \   
     .| <  |         /     .-''"'-.  `.            /     .-''"'-.  `. .   .-.   . | |    \  '  
   .' |_ | |        /     /________\   \          /     /________\   \|  '   '  | | |     |  ' 
 .'     || | .'''-. |                  |          |                  ||  |   |  | | |     |  | 
'--.  .-'| |/.'''. \\    .-------------'          \    .-------------'|  |   |  | | |     ' .' 
   |  |  |  /    | | \    '-.____...---.           \    '-.____...---.|  |   |  | | |___.' /'  
   |  |  | |     | |  `.             .'             `.             .' |  |   |  |/_______.'/   
   |  '.'| |     | |    `''-...... -'                 `''-...... -'   |  |   |  |\_______|/    
   |   / | '.    | '.                                                 |  |   |  |              
   `'-'  '---'   '---'                                                '--'   '--'               
"""

#this is the question that will be asked when the player finishes playing one of the modes.
def askagain():
    print("")    
    playagain = input("Do you want to play one of the modes again? Enter t for Timed or f for Free Play if so. If not, exit the game by pressing the spacebar and then clicking enter.")
    if playagain == "Timed" or playagain == "timed" or playagain == "t" or playagain == "T":
        time.sleep(2)
        timedMode()
    elif playagain == "Free Play" or playagain == "free play" or playagain == "Free play" or playagain == "f" or playagain == "F":
        time.sleep(2)
        freeplayMode()
    elif playagain == " ":
        time.sleep(2)
        print("We're sad to see you go, but thanks for playing! Hope you enjoyed.")
        time.sleep(2)
        print(TheEnd)
        time.sleep(2)
        exit()
    else:
        print("That's not a valid answer. Please try again.")
        askagain()

#starting here, we are defining "if statements" for the correct answers to all twenty questions in the game.
def question1():
    print("")
    print("\033[1m" + "Question 1: Of what race is Nadia?" + "\033[0m")
    print("")
    print("a. Pakistani-American")
    print("b. Indian-American")
    print("c. Swedish-American")
    response1 = input("")

    if response1 == "a":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! Nadia is Pakistani-American.")
        time.sleep(2)
        question2()

    elif response1 == "b" or response1 == "c":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question1()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question1()

def question2():
    print("")
    print("\033[1m" + "Question 2: Why doesn't Nadia want the mehndi at first?" + "\033[0m")
    print("")
    print("a. Because she thinks it will feel bizarre and unknown on her")
    print("b. Because she's worried about how others might view her")
    print("c. Because she thinks that she doesn't deserve it")
    response2 = input("")

    if response2 == "b":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! Nadia is worried about her friends seeing her mehndi at school on Monday.")
        time.sleep(2)
        question3()

    elif response2 == "a" or response2 == "c":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question2()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question2()

def question3():
    print("")
    print("\033[1m" + "Question 3: How did the mehndi feel on Nadia's hands?" + "\033[0m")
    print("")
    print("a. No different than without mehndi")
    print("b. Warm and soothing")
    print("c. Cold and pasty")
    response3 = input("")

    if response3 == "c":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! The mehndi feels cold and pasty on Nadia's hands.")
        time.sleep(2)
        question4()

    elif response3 == "a" or response3 == "b":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question3()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question3()

def question4():
    print("")
    print("\033[1m" + "Question 4: How do Uncle Omar and Uncle Abdul Raheem react to Nadia's mehndi?" + "\033[0m")
    print("")
    print("a. They disapprove")
    print("b. They approve")
    print("c. They present no opinion")
    response4 = input("")

    if response4 == "b":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! Both Uncle Omar and Uncle Abdul Raheem are happy to see Nadia's mehndi.")
        time.sleep(2)
        question5()

    elif response4 == "a" or response4 == "c":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question4()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question4()

def question5():
    print("")
    print("\033[1m" + "Question 5: After looking down at her hands when receiving her gold ring, what does Nadia think about them?" + "\033[0m")
    print("")
    print("a. They look like her hands")
    print("b. They don't look like hands anymore")
    print("c. They look foreign and as if they belong to a stranger")
    response5 = input("")

    if response5 == "c":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! Nadia thinks the mehndi makes her hands look foreign; she thinks they no longer look like her hands.")
        time.sleep(2)
        question6()

    elif response5 == "a" or response5 == "b":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question5()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question5()

def question6():
    print("")
    print("\033[1m" + "Question 6: What is Nadia's role in the wedding?" + "\033[0m")
    print("")
    print("a. Flower girl")
    print("b. Bride")
    print("c. Housemaid")
    response6 = input("")

    if response6 == "a":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! Nadia is the flower girl for this wedding.")
        time.sleep(2)
        question7()

    elif response6 == "b" or response6 == "c":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question6()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question6()

def question7():
    print("")
    print("\033[1m" + "Question 7: As a flower girl, what does Nadia do with her basket of flowers?" + "\033[0m")
    print("")
    print("a. Toss the flowers along the carpet as she walks")
    print("b. Toss all of the flowers over the bride and groom")
    print("c. Toss some flowers on one side of the aisle, then the other")
    response7 = input("")

    if response7 == "c":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! As a flower girl, Nadia needs to toss flowers on one side of the aisle, and then the other.")
        time.sleep(2)
        question8()

    elif response7 == "a" or response7 == "b":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question7()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question7()

def question8():
    print("")
    print("\033[1m" + "Question 8: What stops Nadia in the middle of her flower-tossing procedure?" + "\033[0m")
    print("")
    print("a. She catches the eyes of her cousins giggling")
    print("b. Her eyes catch the ring and mehndi on her hands")
    print("c. She trips over a brick stuck in the carpet")
    response8 = input("")

    if response8 == "b":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! Nadia suddenly stops as her eyes catch the ring and mehndi on her hands. One again, she is insecure about how they look.")
        time.sleep(2)
        question9()

    elif response8 == "a" or response8 == "c":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question8()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question8()

def question9():
    print("")
    print("\033[1m" + "Question 9: What motivates/allows Nadia to continue her procedures?" + "\033[0m")
    print("")
    print("a. She recovers from her fall over the brick and continues")
    print("b. Her family smiles at her with affection and tenderness")
    print("c. Nadia wants to take revenge on her cousins")
    response9 = input("")

    if response9 == "b":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! Nadia is able to continue her procedures after she sees her family smiling at her with great affection and tenderness.")
        time.sleep(2)
        question10()

    elif response9 == "a" or response9 == "c":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question9()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question9()

def question10():
    print("")
    print("\033[1m" + "Question 10: What made Nadia change her opinion about her hands?" + "\033[0m")
    print("")
    print("a. Her family was happy about her hands so she was happy")
    print("b. The mehndi suddenly turned blue - Nadia's favourite colour")
    print("c. Nadia saw someone else's mehndi and really liked it")
    response10 = input("")

    if response10 == "a":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! Nadia's family expressed their happiness, and so, Nadia became happy and proud of her mehndi!")
        time.sleep(2)
        #since the questions after this are only used in the freeplay option, answering question 10 correctly will not always connect directly to question 11.

    elif response10 == "b" or response10 == "c":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question10()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question10()

#starting from here, questions 11-20 are used only in the freeplay option.
def question11():
    print("")
    print("\033[1m" + "Question 11: Do you think Nadia's cousins want Nadia to do well as a flower girl?" + "\033[0m")
    print("")
    print("a. Yes")
    print("b. No")
    print("c. Unsure")
    response11 = input("")

    if response11 == "b":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! Nadia's cousins don't want Nadia to do well; they try to make her worried and nervous about being a flower girl, and they snicker when Nadia suddenly stops her flower-tossing procedure.")
        time.sleep(2)
        question12()

    elif response11 == "a" or response11 == "c":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question11()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question11()

def question12():
    print("")
    print("\033[1m" + "Question 12: What do you think mehndi might represent?" + "\033[0m")
    print("")
    print("a. Good health and prosperity")
    print("b. Serenity and amusement")
    print("c. Sadness and boredom")
    response12 = input("")

    if response12 == "a":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! Since mehndi seems to be used in a wedding, at least for this story, we might infer that mehndi represents good health and prosperity.")
        time.sleep(2)
        question13()

    elif response12 == "b" or response12 == "c":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question12()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question12()

def question13():
    print("")
    print("\033[1m" + "Question 13: Why is it important that Nadia shows sabr, or patience, as she waits?" + "\033[0m")
    print("")
    print("a. The adults could make a mistake with her mehndi because Nadia could be a distraction for them")
    print("b. It's not important; the adults are asking for too much")
    print("c. Nadia must respect her elders, and patience is an important skill to develop")
    response13 = input("")

    if response13 == "c":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! It's important that Nadia respects her elders, and those elders want her to learn patience - an important real-world skill!")
        time.sleep(2)
        question14()

    elif response13 == "a" or response13 == "b":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question13()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question13()

def question14():
    print("")
    print("\033[1m" + "Question 14: Compare Uncle Omar and Uncle Abdul Raheem." + "\033[0m")
    print("")
    print("a. Uncle Abdul Raheem seems to be closer with Nadia than Uncle Omar")
    print("b. Uncle Abdul Raheem doesn't care about mehndi while Uncle Omar does")
    print("c. Nadia dislikes Uncle Abdul Raheem and tolerates Uncle Omar")
    response14 = input("")

    if response14 == "a":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! This was one of the harder ones. Uncle Abdul Raheem seems to be slightly more kind and caring with Nadia.")
        time.sleep(2)
        question15()

    elif response14 == "b" or response14 == "c":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question14()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question14()

def question15():
    print("")
    print("\033[1m" + "Question 15: During the wedding, which of the following quotes best shows Nadia's nervousness?" + "\033[0m")
    print("")
    print("a. 'saw a sea of eyes following her'")
    print("b. 'the flutter of butterflies'")
    print("c. 'it wasn't so hard'")
    response15 = input("")

    if response15 == "b":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! The quote 'the flutter of butterflies' best shows Nadia's nervousness during the wedding, out of the three options provided.")
        time.sleep(2)
        question16()

    elif response15 == "a" or response15 == "c":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question15()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question15()

def question16():
    print("")
    print("\033[1m" + "Question 16: What might Nadia's grandma mean by 'When I look at your hands, it's as if I'm looking at my past and my future at the same time'?" + "\033[0m")
    print("")
    print("a. She is telling Nadia that mehndi has always been very important to her and the Pakistani culture")
    print("b. She’s confused about whether Nadia is her grandaughter or if Nadia is her mother")
    print("c. She is telling Nadia that she used to have mehndi as a young girl")
    response16 = input("")

    if response16 == "a":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! This was another hard question. Nadia's grandma is trying to tell her granddaughter the true importance of mehndi for her and her culture.")
        time.sleep(2)
        question17()

    elif response16 == "b" or response16 == "c":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question16()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question16()

def question17():
    print("")
    print("\033[1m" + "Question 17: What emotion did Nadia feel most at the end of the book?" + "\033[0m")
    print("")
    print("a. Recklessness")
    print("b. Arrogance")
    print("c. Pride")
    response17 = input("")

    if response17 == "c":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! Nadia is very proud of her mehndi and her culture at the end of the book.")
        time.sleep(2)
        question18()

    elif response17 == "a" or response17 == "b":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question17()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question17()

def question18():
    print("")
    print("\033[1m" + "Question 18: What might be one theme of the book Nadia's Hands?" + "\033[0m")
    print("")
    print("a. Perseverance/bravery")
    print("b. Revenge")
    print("c. Respect/loyalty")
    response18 = input("")

    if response18 == "c":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! Respect and loyalty are two of the most important and recurring themes in Nadia's Hands.")
        time.sleep(2)
        question19()

    elif response18 == "a" or response18 == "b":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question18()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question18()

def question19():
    print("")
    print("\033[1m" + "Question 19: Which of the following ideas do you think Nadia’s Hands might relate most to?" + "\033[0m")
    print("")
    print("a. Clean water and sanitation")
    print("b. No poverty")
    print("c. Reduced inequalities")
    response19 = input("")

    if response19 == "c":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! This was probably the hardest question. Nadia's Hands might relate to the United Nations Sustainable Development Goal #10: Reduced Inequalities. The expression of different cultures can help reduce unjust differences between groups of people!")
        time.sleep(2)
        question20()

    elif response19 == "a" or response19 == "b":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question19()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question19()

def question20():
    print("")
    print("\033[1m" + "Question 20: What message should be taken away from Nadia's Hands?" + "\033[0m")
    print("")
    print("a. Compare yourself to others")
    print("b. Be proud of your culture and your family")
    print("c. Be true to yourself")
    response20 = input("")

    if response20 == "b":
        playsound("CorrectAnswer.mp3",0)
        print(Correct)
        print("Great job! It's really important that you are proud of your own personal culture and your family!")
        #this is the last question (in the freeplay mode), so no other questions follow this one.
        
    elif response20 == "a" or response20 == "c":
        print("Good try, but unfortunately, that is not right. Please try again!")
        time.sleep(2)
        question20()

    else:
        print("Sorry, this is not a valid answer. Please try again.")
        time.sleep(2)
        question20()

#this section is the program for the freeplay option.
def freeplayMode():
    print("Welcome to the free play mode! There will be some easy questions, and then some harder ones.")
    time.sleep(2)
    question1()
    print("Great job for making it past the first 10 questions! Moving on now to some harder questions - try your best.")
    time.sleep(2)
    question11()
    time.sleep(2)
    print(Congrats)
    time.sleep(2)
    print("Congratulations for making it through all twenty questions! You have mastered Nadia's Hands.")
    time.sleep(2)
    print("Thanks for playing!")
    time.sleep(2)
    askagain()

#this section is the program for the timed mode option.
def timedMode():
    start = input("Please press enter to start the stopwatch.")
    time.sleep(2)
    print("The timer starts in 3...2...1...")
    time.sleep(2)
    print("Go!")
    #the timer starts here.
    begin = time.time()
    question1()
    endtimer = input("Please press enter again to end the stopwatch.")
    end = time.time()
    #the timer ends here.
    print("The timer has stopped!")
    elapsed = end - begin
    elapsed = int(elapsed)
    time.sleep(2)
    print(Congrats)
    playsound("EndofGame.mp3",0)
    time.sleep(2)
    print("You used", elapsed, "seconds to complete these 10 questions! Well done - this is your new timed score.")
    time.sleep(2)
    print("Thanks for playing!")
    time.sleep(2)
    askagain()

#this section is the program for asking which gameplay option the player wants.
def gameplay():
    choiceofgame = input("Do you want a 10-question timed quiz for a high score, or a 20-question “free play” game that gives you unlimited time? Enter t for Timed or f for Free Play. ")
    if choiceofgame == "Timed" or choiceofgame == "timed" or choiceofgame == "t" or choiceofgame == "T":
        time.sleep(2)
        timedMode()
    elif choiceofgame == "Free Play" or choiceofgame == "free play" or choiceofgame == "Free play" or choiceofgame == "f" or choiceofgame == "F":
        print("")
        freeplayMode()
    else:
        print("That's not a valid answer. Please enter Timed or Free Play.")
        time.sleep(2)
        print("")
        gameplay()

#this section is the program for the sample question in the tutorial that allows the player to understand how to input their answer.  
def sample():
    print("")
    print("Sample Question 1: What is the first letter in the alphabet?")
    print("a. the letter a")
    print("b. the letter z")
    print("c. the letter m")
    print("")
    samplequestion1 = input("What is your answer? (remember, just write the letter option and press enter) ")
    if samplequestion1 == "a":
        playsound("CorrectAnswer.mp3",0)
        print("Well done! Moving on.")
        time.sleep(2)
    else:
        print("Good try, but please re-attempt the question.")
        print("")
        time.sleep(2)
        sample()

#this section is the program for the tutorial.
def tutorial():
    print("")
    time.sleep(2)
    print("Welcome to the tutorial!")
    time.sleep(2)
    print("I will show you how to answer questions in this game.")
    time.sleep(2)
    print("If you are given multiple choice questions, please enter the correct answer by typing in the letter corresponding to the answer, and then press enter.")
    time.sleep(2)
    print("Let's try a sample question.")
    time.sleep(2)
    sample()
    time.sleep(2)
    print("Great job for making it through this short tutorial! Now, you're ready to play the game.")
    time.sleep(2)
    print("")
    gameplay()

#this section is the program for asking whether the player wants to skip the tutorial or not.
def skiptutorial():
    choicetutorial = input("Do you want to skip the tutorial? (y or n) ")
    if choicetutorial == "y":
        print("Excellent! Let's get started with the game.")
        gameplay()
    elif choicetutorial == "n":
        tutorial()
    else:
        time.sleep(2)
        print("This is not a valid answer. Please enter y or n. ")
        skiptutorial()

#this section is the program for the first question - whether the player has played the game before.
def introquestion():
    pastgameplay = input("Have you played this game before? (y or n) ")
    if pastgameplay == "y":
        time.sleep(2)
        skiptutorial()
    elif pastgameplay == "n":
        tutorial()
    else:
        time.sleep(2)
        print("This is not a valid answer. Please enter y or n. ")
        introquestion()

#this is where the game officially begins.
playsound("BackMusic.mp3",0)
print(Welcome)
time.sleep(2)
print("This game is based on the book Nadia's Hands by Karen English.")
time.sleep(2)
userName = input("What is your name? ")
print("Nice to meet you, " + userName + "!")
time.sleep(2)
introquestion()