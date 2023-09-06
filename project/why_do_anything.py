import time


def do_nothing_about_it():
    print("")
    print("<<<<<<<<Nihilism>>>>>>>")
    time.sleep(1)
    print("*" * 30)
    print("sorrow, despair and meaninglessness")
    print("")


def suicide():
    print("")
    print("thw end of a poor and useless soul!!!!")
    print("")


def religion():
    print("")
    print("A world of lie and desperate search for a certain way of salvation")
    print("")


def rebelling():
    print("")
    print("remembering that you promised yourself that you  will not be a victim of despair and absurdity")
    print("")


def fill_that_void():
    print("<<<<<<power and control>>>>>>>>")
    time.sleep(2)
    print("*" * 30)
    print("meaningful action (Responsibility)")
    print("")
    choose = input("but it is hard:\ngive up or fight: ")
    if choose == "give up":
        print("")
        print("fleeting pleasure, comfort and distractions")
        time.sleep(0.9)
        print("")
        do_nothing_about_it()
    elif choose == "fight":
        print("")
        print(" > there is joy and deeper meaning in overcoming obstacles.\n"
              " > you have an obligation to it. it is you mission and vocation.\n"
              " > you have made a promise and your actions reflect how you image humanity.\n"
              " > only meaninglessness and despair is the alternative option in other \
words suffering is inevitable in life.")
        print("")
        time.sleep(0.9)
        print("<<<<<<<<<ABSURD HERO>>>>>>>>>>>")
        print("*" * 30)


print("why do anything!!")
choose = input("Because there is an existential void and emptiness\nso what will you do about it: ").lower()
if choose == "do nothing":
    do_nothing_about_it()
    choose = input("suicide or religion ")
    if choose == "suicide":
        suicide()
    elif choose == "religion":
        religion()
    else:
        rebelling()
        time.sleep(1)
        fill_that_void()
elif choose == "fill that void":
    fill_that_void()
