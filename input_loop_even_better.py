#!/usr/bin/env python2

def ask_user_to_choose(question, allowed_responses):
    tries = 0
    while tries < 5:
        value = raw_input(question + ': ')
        if value in allowed_responses:
            return value
        print "That's not what I asked you for."
        tries = tries + 1
    print "Please try to follow directions.  I can't read your mind (yet)."

def main():
    name = raw_input("what is your name: ")
    while True:
        print "Welcome, " + name
        print "1. Do something"
        print "2. Do something else"
        print "3. quit"
        choice = ask_user_to_choose("Make a choice, if you dare!", ['1', '2', '3'])
        if not choice:
            return
        choice = int(choice)
        if choice == 1:
            print "I did something."
        elif choice == 2:
            print "I did something else.  Happy?"
            print "1. Happy"
            print "2. Not happy"
            happy = ask_user_to_choose("well?", ['1', '2'])
            if happy == '1':
                print "Excellent.  Lets continue!"
            elif happy == '2':
                print "I'm sorry to hear that.  I won't bother you any more."
                break
            else:
                return
        else:
            break   
    print "bye, " + name

if __name__ == '__main__':
    main()
