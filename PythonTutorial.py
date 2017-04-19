# ~/usr/bin/python

# Kadhir Manickam - 04/19/17
# Coding Workshop

# Introduction to Python Exercises

# To run your code use the following:
# 1. Open a terminal window
# 2. type in 'cd ~/Desktop/CodingWorkshop'
# 3. Now run the code with 'python ./PythonTutorial'

##############################################
########## Exercise 1 - Hello World ##########
# Instructions:                              #
# Tell the world you're starting to code in  #
# python! Make 'Hello World' print to the    #
# terminal                                   #
##############################################

print('------------- Exercise 1 -------------')
# Your Code Here #
print('------------- End of Exercise 1 -------------\n')


##############################################
########## Exercise 2 - Storing Values  ######
# Instructions:                              #
# Oh no, someone wrote some vile stuff       #
# about SigEp in python. Make it more        #
# positive by adjusting the variables        #
##############################################

print('------------- Exercise 2 -------------')
percent_of_sigeps = '100.0%'
fraternity = 'SigEp'
adjective = 'poopoo-heads'

print( percent_of_sigeps + ' of ' + fraternity + 's are ' + adjective)

print('------------- End of Exercise 2 -------------\n')

##############################################
#------------        STOP        ------------#
##############################################

##############################################
########## Exercise 3 - Basic Math  ##########
# Instructions:                              #
# Here's a logic puzzle: can you make the    #
# variable 'e' equal 9 using basic math?     #
# Feel free to use any of the basic math     #
# operators: +, -, /, * plus parenthesis ()  #
# The terminal will print out the current    #
# value of e.                                #
##############################################

print('------------- Exercise 3 -------------')
a = 10
b = 10
c = 10
d = 10
e = a + b + c + d #Change me!
print('E equals ' + str(e))

print('------------- End of Exercise 3 -------------\n')

##############################################
########## Exercise 3.5 - Printing  ##########
# Instructions:                              #
# Print the following statement using just   #
# the variables provided:                    #
# '45 SigEps went to drink, and only 44      #
# returned.'                                 #
##############################################

print('------------- Exercise 3 -------------')
total_sigeps = 45
print('Your code here' + ' SigEps went to drink, and only ' + 'Your code here' + ' returned')

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# means that python doesn't like strings and ints
# in the same print statement. Look at exercise 3,
# line 64 for guidance

print('------------- End of Exercise 3 -------------\n')

##############################################
#------------        STOP        ------------#
##############################################

##############################################
########## Exercise 4 - Conditionals  ########
# Instructions:                              #
# Ugh, someone called us silly looking on    #
# the street the other day. Fix the code so  #
# that it says 'Suave gentlemen' without     #
# changing the print statements              #
##############################################

print('------------- Exercise 4 -------------')
fraternity = 'SigEp'
house = 'New House'

# print( house == 'New House' )
# print( house == 'Old House' )
# print( house != 'New House' )
# print( house != 'Old House' )

# Go ahead and uncomment lines 105 to 108 one at
# a time and see what prints out in the terminal.

if fraternity == 'SigEp':
	print('Silly looking fellows')
else:
	print('Suave gentlemen')

print('------------- End of Exercise 4 -------------\n')

##############################################
########## Exercise 5 - Looping     ##########
# Instructions:                              #
# Oh my god, those annoying sororities       #
# robotos are practicing their 'songs' for   #
# rush already. They sing on constant repeat #
# all day. Can you make some adjustments to  #
# their programming to make them say:        #
# 'SigEp is the coolest' 10 times?           #
##############################################

print('------------- Exercise 5 -------------')

# This a loop, in another words a piece of code
# that runs a predesignated number of times.
# Try replacing the print statement with
# print(index) and see what pops out. Then try
# adjusting the numbers inside range() and see what changes.

for index in range(0, 5):
	print('*insert generic sorority rush song here*')

print('------------- End of Exercise 5 -------------\n')

##############################################
#------------        STOP        ------------#
##############################################

##############################################
########## Exercise 6 - Strings  #############
# Instructions:                              #
# There by buried treasure inside this       #
# string. See if you can dig it out by       #
# getting the print statement to print       #
#'SigEp' instead of the foul stuff it's      #
# printing now.                              #
##############################################

print('------------- Exercise 6 -------------')
buried_treasure = 'shitSigEpshit'
test_string = '0123456789'

# print(test_string[3])
# print(test_string[3:7])
# print(test_string[5:])
# print(test_string[:5])
# print(test_string[:])

# You can access individual characters in a
# string in python using the syntax above!
# Try uncommenting one of those print statements
# in lines 158 - 163 one at a time and see what
# gets printed.

print(buried_treasure[0:4])

print('------------- End of Exercise 6 -------------\n')

##############################################
########## Exercise 7 - Lists    #############
# Instructions:                              #
# Wow, sometimes exec needs to learn to      #
# watch their mouths while AVC is around.    #
# They're about to give a speech, help them  #
# by bleeping out all the bad words in their #
# speech!                                    #
##############################################

print('------------- Exercise 7 -------------')
bad_words_dictionary = [ 'bad boy', 'garbage', 'loser', 'crap' ]
exec_speech = [ 'bad boy', 'hello world', 'loser', 'yellow' ]

# print( 'bad boy' in input_words)
# if 'stuff' in [ 'stuff' ]:
# 	print('There is stuff in here!')
# else:
# 	print('There is no stuff in here')

# Think of a list (like bad_words_dictionary, or
# exec_speech) as nothing more than a collection of
# strings. You can loop through them and print out
# all their contents like we do below. Try
# uncommenting lines 188 to 192 above to see how conditional
# logic like exercise 4 could be applied here!

for word in exec_speech:
	# Your Code Here #
	print(word)

print('------------- End of Exercise 7 -------------\n')

##############################################
########## Exercise 8 - Dictionaries  ########
# Instructions:                              #
# Rats, the VPP stuck you with the Costco    #
# list for the upcoming baby themed party.   #
# Sum all the individual supply costs        #
# and print 'We have enough money for        #
# everything', if there's money in the       #
# budget, or print out how much extra money  #
# is needed                                  #
##############################################

print('------------- Exercise 8 -------------')
# Your Code Here #
costco_list = { 'Cups': 10, 'PBR': 100, 'Rum': 150, 'Lights': 120, 'Binkies': 15 }
total_budget = 375

# A dictionary, is like a list, except instead of
# calling on index values, like exec_speech[2] to
# access the values, we call on keys, like costco_list['Cups'].
# This is referred to as a key, value pairing. You
# should have all the tools you need from the previous
# exercises to solve this puzzle. Don't worry about
# the .iteritems(), it isn't important for now

for key, value in costco_list.iteritems():
	print(key, value)

#insert conditional here
print('We have enough money for everything!')

print('------------- End of Exercise 8 -------------\n')

##############################################
#------------        STOP        ------------#
##############################################

##############################################
########## Exercise 9 - Challenge  ###########
# Instructions:                              #
# Shucks, looks like the SigEp roster got    #
# messed up again. Can you sort the Sigmas,  #
# Phis, and Epsilons back into               #
# sorted_sigep_members? Ultimately we want a #
# list just filled with names of brothers    #
# belonging to each class. Eg:               #
# { 'Sigma': ['0', '4', '6', '8'],           #
#    'Phi': ['1', '3', '10'],                #
#    'Epsilon': ['2', '5', '7', '9']         #
# }                                          #
##############################################

print('------------- Exercise 9 -------------')
sorted_sigep_members = { 'Sigma': [], 'Phi': [], 'Epsilon': [] }
all_members = [ 
	{ 'Name': '0', 'Class': 'Sigma' },
	{ 'Name': '1', 'Class': 'Phi' },
	{ 'Name': '2', 'Class': 'Epsilon' }, 
	{ 'Name': '3', 'Class': 'Phi' },
	{ 'Name': '4', 'Class': 'Sigma' },
	{ 'Name': '5', 'Class': 'Epsilon' },
	{ 'Name': '6', 'Class': 'Sigma' },
	{ 'Name': '7', 'Class': 'Epsilon' },
	{ 'Name': '8', 'Class': 'Sigma' },
	{ 'Name': '9', 'Class': 'Epsilon' },
	{ 'Name': '10', 'Class': 'Phi' },
]

# temp = {}
# temp['test'] = 10
# temp['test'] += 10
# temp['1'] = []
# temp['1'].append('10')
# temp['1'].append('20')
# print(temp)
# Uncomment lines 269 - 272 for a hint!

# Your Code Here #

print('------------- End of Exercise 9 -------------\n')
