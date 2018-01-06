# IPND Stage 2 Final Project
# For this project, we shall be building a Fill-in-the-Blanks quiz.
# Our quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help us remember important vocabulary!

blanks = ["___1___", "___2___", "___3___", "___4___"]
easy_quiz = '''___1___ in physics, is the rate of change of velocity of an object 
with respect to time. 
___2___ is any interaction that, when unopposed, will change the motion of an object. 
___3___ of a distribution of mass in space is the unique point where the weighted relative position of
the distributed mass sums to zero, or the point where if a force is applied it moves in the direction of the force without rotating. 
___4___ is the measure of an object's resistance to acceleration (a change in its state of motion) when a net force is applied. Source: Wikipedia and Tutorialspoint'''
medium_quiz = '''___1___ is the rotational analog of linear momentum.
___2___ of a body is the rate of change of its angular displacement with respect to time.
___3___ is a movement of an object along the circumference of a circle or rotation along a circular path.
___4___ is an inertial force (also called a "fictitious" or "pseudo" force) directed away from the axis
of rotation that appears to act on all objects when viewed in a rotating frame of reference. Source: Wikipedia'''
hard_quiz = '''___1___ relates the integrated magnetic field around a closed loop to
the electric current passing through the loop.
___2___ is a law of physics that describes force interacting between static
electrically charged particles.
___3___ is a basic law of electromagnetism predicting how a magnetic field will interact with an electric circuit to produce an
electromotive force (EMF)—a phenomenon called electromagnetic induction.
___4___ indicates that the induced EMF and the change in magnetic flux have opposite signs. is  Source: Wikipedia'''
easy_answers = ["Acceleration", "Force", "Center of mass", "Mass"]
medium_answers = ["Angular Momentum", "Angular Velocity",
                  "Circular Motion", "Centrifugal Force"]
hard_answers = ["Ampere's circuital law", "Coulomb's law",
                "Faraday's law of induction", "Lenz's law"]


def get_name():
    """
    Behavior: This method is get_name method. All names of the users are generated by this method
    :param level:  None
    :return: Name
    """
    name = raw_input("Please enter your name: ")
    if (name == ""):
        print "Name can't be empty.\n"
        get_name()
    else:
        print "Hello " + name + ", "
        return name


def get_level():
    """
    Behavior: This method is get_level method. All levels of the games are generated by this method
    :param level:  None
    :return: Level
    """
    level = raw_input(
        "Please select a difficulty level for your quiz"
        "(easy, medium, or hard):")
    if level.lower() in ["easy", "medium", "hard"]:
        print "You chose " + level.lower() + "\n"
        return level.lower()
    else:
        print "You entered an invalid difficulty level.\n"
        get_level()


def word_in_pos(word, parts_of_speech):
    """
    Behavior: This method is words_in_pos method, which is used to identify whether a substring 
    of word is in the parts_of_speech list.  
    :param level: word,parts_of_speech
    :return: pos or None
    """
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None


def fill_in(quiz, blank, answer):
    """
    Behavior: This method is wfill_in method, which is for users to add answers to the blank spaces.
    :param level: quiz, blank, answer
    :return: replaced
    """
    quiz = quiz.split()
    replaced = []
    for word in quiz:
        if (word == blank):
            word = word.replace(blank, answer)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced


def quiz_check(quiz, answers):
    """
    Behavior: This method is quiz_check method, which is used to check if the answers the users input 
    are correct.
    :param level: quiz, answers
    :return: None(only print things)
    """
    index = 0
    for blank in blanks:
        player_answers = raw_input(
            "\nPlease fill in blank # " + str(index+1) + ": ")
        while player_answers.lower() != answers[index].lower():
            print "\nNah. Bruh, your answer was wrong. Please try again."
            player_answers = raw_input("Type it here again: ")
        print "\nAwesome, that's my homie!\n"
        quiz = quiz.replace(blank, answers[index])
        print "QUIZ\n" + quiz
        index += 1


def setup_quiz(level):
    """
    Behavior: This method is setup_quiz method, which is used to set the difficulty of the quiz.
    :param level: level
    :return: different quizzes and corresponding answers.
    """
    if(level == "easy"):
        print "QUIZ\n" + easy_quiz
        return easy_quiz, easy_answers
    elif(level == "medium"):
        print "QUIZ\n" + medium_quiz
        return medium_quiz, medium_answers
    else:
        print "QUIZ\n" + hard_quiz
        return hard_quiz, hard_answers


def play_quiz():
    """
    Behavior: This method is play_quiz method, which is used to create a general quiz structure 
    by connecting previous functions together. 
    :param level: None
    :return: None(only prints messages when the quiz has been finished)
    """
    name = get_name()
    level = get_level()
    quiz, answers = setup_quiz(level)
    quiz_check(quiz, answers)
    print "\nCongrats, " + name + ", You've finished the quiz!\n"

play_quiz()
