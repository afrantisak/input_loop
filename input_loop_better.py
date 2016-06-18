#!/usr/bin/env python2

def main():
    name = raw_input("what is your name: ")
    while True:
        print "welcome, " + name
        print "1. do something"
        print "2. do something else"
        choice = raw_input("make a choice, if you dare!: ")
        choice = int(choice)
        if choice == 1:
            print "I did something."
        elif choice == 2:
            print "I did something else.  Happy?"
        else:
            print "bad choice"
            try_again = raw_input("try again? (y/n): ")
            if try_again == 'y':
                continue
            elif try_again == 'n':
                break
            else:
                print "please learn to follow directions!"
                return
    print "bye, " + name

if __name__ == '__main__':
    main()
