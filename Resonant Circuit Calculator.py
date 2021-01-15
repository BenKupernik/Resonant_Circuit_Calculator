##Ben Kupernik
##7/8/2020
##
############################################################################################################################################################################################
##
##README
##
##This program takes the resonant frequency bandwidth and gain of a circuit and ask if it is in series or parallel.
##It then calculates the resistance inductance and capacitance and displays all 6 values to the user.
##There is one superclass called ResonantCircuit which collects the resonant frequency bandwidth and gain,
##and has a display function that prints that information.
##There are also two subclasses called SeriesResonantCircuit and ParallelResonantCircuit that
##calculate the resistance inductance and capacitance depending on which type of circuit it is.
##
##
############################################################################################################################################################################################
##
##Test one
##
##Input
##
##do two loops first for parallel and then for series. For both use resonant frequency =1 bandwidth =1 and gain =1
##
##Output
##
##Program complies correctly the correct function is called depending on the type of circuit and the correct values for resistance inductance and capacitance displayed.
##
##Test two
##
##Input
##
##Try to break it every time the program using the wrong types of input. For example, resonant frequency =1 bandwidth =1 and gain =1 name = 56 don't give any of the option when
##an answer prompt shows up
##
##Output
##
##Program crashed if resonant frequency = q so I added a try expect function and now it works fine. All other odd answers I can think of are handled by while loops
##that force the user to enter an acceptable value.
##
##Test three
##
##Input
##
##Try to crash the program using math. Enter 0 for resonant frequency bandwidth and gain. As they all are used in a denominator if my error handling doesn’t work that will crash the program
##
##Output
##
##The error handling works if 0 is entered for any of the first three initial values the user is simply asked to reenter the values. Upon correct values being entered
##the program run through and produces the correct values with the expected output.
##
##############################################################################################################################################################################################


##Superclass


class ResonantCircuit:

    ##Makes the resonantFrequency, bandwidth and gain variables for later use
    def __init__(self):
        
        self.resonantFrequency = 0
        self.bandwidth = 0
        self.gain = 0

    ##This function askes the user for the resonant frequency, bandwidth and gain values and assigns them to their respective variables
    def getVariables (self):
        while((self.resonantFrequency == 0) or (self.bandwidth == 0) or (self.gain == 0)):##If any of these = 0 it would result in a div by 0 error this makes sure they don't
            while True:##This makes sure the user enters a number and not a letter or something weird
                    try:
                        self.resonantFrequency = float(input("What is the resonant frequency?"))
                        self.bandwidth = float(input("What is the bandwidth?"))
                        self.gain = float(input("What is the gain?"))
                        break
                    except ValueError: #Error handling in case they don't enter a number.
                        print("Uhm that is not a number. try again")

            if((self.resonantFrequency == 0) or (self.bandwidth == 0) or (self.gain == 0)): ##Error message for a 0 value
                print("At least one of the entered values is 0. That is not possable, please try again")
        

        return(self.resonantFrequency,self.bandwidth,self.gain)


    ##This just prints the values the user entered
    def display(self):
        print("")
        print("The resonant frequency is" ,self.resonantFrequency)
        print("The bandwidth is" ,self.bandwidth)
        print("The gain is" ,self.gain)
        print("")

        


##Subclass

##First subclass for series circuits
class SeriesResonantCircuit(ResonantCircuit):

    ##Makes the resistance, capacitance and inductance variables for later use
    def __int__(self):
    
        self.resistance = 0
        self.capacitance = 0
        self.inductance = 0

    ##This function is used to get the values for resistance, capacitance and inductance and calculate the values of resistance, capacitance and inductance
    def getVariables(self):

        ##Three place holders are needed to calculate the values for resistance, capacitance and inductance
        self.tempResonantFrequency = 0
        self.tempBandwidth = 0
        self.tempGain = 0

        ##Calles the super getVariables function and stores the values for resonant frequency bandwidth and gain in the placeholders created above.
        self.tempResonantFrequency, self.tempBandwidth, self.tempGain  = super().getVariables()


        ##Calculation for the resistance, capacitance and inductance variables. The order in which they are calculated is important
        
        self.resistance = 1 / self.tempGain ##Uses the equation R = 1 / k

        self.inductance = self.resistance / self.tempBandwidth ##Uses the equation L = R / B

        self.capacitance = 1 / ((self.tempResonantFrequency ** 2) * self.inductance) ##Uses the equation C = 1 / (w ^ 2 * L)
        
    ##This prints the values of the three user and three calculated variables above
    def display(self):
       
       super().display() ##Calles the super display function
       print("The Capacitance is "+"{:.2f}".format(self.capacitance))
       print("The Resistance is "+"{:.2f}".format(self.resistance))
       print("The Inductance is "+"{:.2f}".format(self.inductance))
       print("")



##Seconed subclass for parallel circuits
class ParallelResonantCircuit(ResonantCircuit):

    ##Makes the resistance, capacitance and inductance variables for later use
    def __int__(self):
    
        self.resistance = 0
        self.capacitance = 0
        self.inductance = 0

    ##This function is used to get the values for resistance, capacitance and inductance and calculate the values of resistance, capacitance and inductance
    def getVariables(self):

        ##Three place holders are needed to calculate the values for resistance, capacitance and inductance
        self.tempResonantFrequency = 0
        self.tempBandwidth = 0
        self.tempGain = 0
        
        ##Calles the super getVariables function and stores the values for resonant frequency bandwidth and gain in the placeholders created above.
        self.tempResonantFrequency, self.tempBandwidth, self.tempGain  = super().getVariables()

        self.resistance = self.tempGain ##Uses the equation R = k

        self.capacitance = 1 / (self.tempBandwidth * self.resistance) ##Uses the equation C = 1 / (B * R)

        self.inductance = 1 / ((self.tempResonantFrequency ** 2) * self.capacitance)##Uses the equation L = 1 / (w ^ 2 * C)

        
     ##This prints the values of the three user and three calculated variables above   
    def display(self):
       
       super().display()##Calles the super display function
       print("The Capacitance is "+"{:.2f}".format(self.capacitance))
       print("The Resistance is "+"{:.2f}".format(self.resistance))
       print("The Inductance is "+"{:.2f}".format(self.inductance))
       print("")

             


##############################################################################################################################################################################################


##Variables
       

answer =""


##############################################################################################################################################################################################


answer = input("Hi there! Do you have a circut today? (yes/no)")

    
while (answer != 'no'):##Master loop, broken when the user has no more circuits
    
    answer = input("Ok great! What’s is it in series or parallel?")
    
    while ((answer != 'series') and (answer != 'parallel')): ##Makes the user enter one of the two possible circuit types
        answer = input("ehr what did you say? (series/parallel?)")

    ##Makes a SeriesResonantCircuit object if they have a series circuit
    if (answer == 'series'):
        answer = input("What's its name?")
        answer = SeriesResonantCircuit()
        
    ##Makes a ParallelResonantCircuit object if they have a parallel circuit
    if (answer == 'parallel'):
        answer = input("What's its name?")
        answer = ParallelResonantCircuit()


    ##Calls the getVariables and display functions. Thanks to polymorphism i don't need to specify which function to use
    answer.getVariables()
    answer.display()

    answer = input("Do you have another circuit? (yes/no)")##alows the user to break the loop and end the program

print("Goodbye.")
        
        
    

    
        
