print("Welcome to the reality of learning a new skill after entering the Vortex!")
Name = (input("What is your name? "))

Begin = str(input("Rate how much you agree with these statements about your experence of learning something new on a scale of 1 to 10, with 1 'being not at all' and 10 'being very much so' Enter y to begin: "))
if Begin == "y":
    for counter in range(4):
        if counter ==0: 
            Answer = (int(input("The challenge makes me feel exhilerated. Enter any number from 1 - not at all, to 10 - very much so: ")))

        if counter ==1:
            Answer = (int(input("This learning adventure is so much fun! Enter any number from 1 - not at all, to 10 - very much so: ")))

        if counter ==2:
            Answer = (int(input("This is just the kind of fabulous experience I attracted. Enter any number from 1 - not at all, to 10 - very much so: ")))

        if counter ==3:
            Answer = (int(input("It feels so exciting to put in effort for something I want, that I enjoy and can have so much fun with. Enter any number from 1 - not at all, to 10 - very much so: ")))

        if Answer == 10:
            print(f"You {Name} are trully tuned in, tapped in and turned on.")
        else:
            if Answer <7:
                    print (f"Create a new belief by practicing a new thought {Name}")
            elif Answer <3:
                print (f"Are you resisting or following the flow {Name}? Nap, meditate and repeat until the frequency has changed.")
            else:
                print (f"Keep riding the momentum {Name}.")