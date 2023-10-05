
def countUp_Down(number_input):  # initial point

    if number_input >= 0:

        print(f">>>> countup({number_input})")  # countup

        while number_input > 0:
            print(number_input)
            number_input -= 1
        print("Blastoff!")
    else:
        print(f">>>> countdown({number_input})")  # countdown

        while number_input < 0:
            print(number_input)
            number_input += 1
        print("Blastoff!")


countUp_Down(-3)  # calling numbers


