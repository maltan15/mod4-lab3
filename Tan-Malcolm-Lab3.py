#!/usr/bin/env python
# coding: utf-8

# # Assignment: Playing with Functions
# 
# ## Instructions
# 
# This is the template file for the assignment of Module 4 called "Lab 3." Please carefully follow the instructions below.
# 
# 1. Rename this file by filling out your surname and first name in the file name. For example, if your surname is Ilagan and if your first name is Joben, then rename the file to ILAGAN-JOBEN-lab3.ipynb.
# 2. Fill out the markdown cell just above `Problem 1` with your student details as indicated.  
# 3. To submit this file, first, upload your file to your GitHub repository and, second, submit your repository link to the assignment on Canvas.
# 

# ## Student Details
# 
# ID Number: 204957
# Surname: Tan, Malcolm
# Year and Course: 2 BS ITE

# ## Problem 1: Caesar Cipher (11 points) 
# 
# A _cipher_ is a way of disguising a message by encoding it.  
# 
# One of the simplest ciphers is a "shift cipher" known as the _Caesar cipher_. The way it works is very simple.  
# 
# 1. Start with a message, such as "ATTACK AT DAWN".
# 2. Choose a number, such as 3.
# 3. _Shift_ all letters in the message to the right by the chosen number. In this case, shifting all letters in "ATTACK AT DAWN" by 3 results in the message "DWWDFN DW GDZQ".
# 
# **Write a function called `problem_1` that takes two positional arguments `message` and `shift`. It should apply the Caesar cipher to a message and _return_ the result.**  
# 
# Example input/output:  
# `problem_1("ATTACK AT DAWN", 3)` => `"DWWDFN DW GDZQ"`  
# `problem_1("MEAMORE", 42)` => `"CUQCEHU"`
# 
# For full credit:
# 
# 1. The function must ignore spaces.
# 2. The function must be able to "wrap around" if it reaches the end of the alphabet. (e.g., shifting Z by 1 should result in A, shifting Z by 2 should result in B, etc.)
# 
# For your convenience:
# 1. Assume that all letters will be uppercase.
# 2. Be aware of the `chr()` function. `chr()` takes an Unicode code number and returns the character associated with that number (e.g., chr(65) => "A").
# 3. Be aware of the `ord()` function. `ord()` takes a Unicode character and returns the Unicode code associated with that character (e.g., ord("A") => 65).
# 4. Be aware that the Unicode codes of the uppercase English alphabet are Unicode codes 65 to 90, where 65 = A, 66 = B, ..., 90 = Z.
# 5. The shift will always be a positive integer.

# In[1]:


def problem_1(message, shift):
    new_word = ''
    for i in message:
        if ord(i) >= 65 and ord(i) <= 90:
            i = chr((ord(i) + shift - 65) % 26 + 65)
            if ord(i) == 32:
                None
        new_word = new_word + i

    return(new_word)


# In[3]:


problem_1("MEAMORE", 42)


# ## Problem 2: Social Media Relationships (13 points) 
# 
# Let us pretend that you are building a new app. Your app supports social media functionality, which means that users can have _relationships_ with other users.  
# 
# There are two guidelines for describing relationships on this social media app:  
# 1. Any user can _follow_ any other user.  
# 2. If two users follow each other, they are considered _friends_.  
# 
# Data about your users and their followers is stored in a dictionary that adheres to this structure:  

# In[1]:


# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}


# **Write a function called `relationship_status` that takes three positional arguments: (str) `from_member`, (str) `to_member`, and (dict) `social_graph`. The function should determine the _relationship status_ of the first member to the second member based on the data stored in the social graph. The function should _return_ one of these values depending on what is appropriate:**  
# - "follower", if `from_member` follows `to_member`
# - "followed by", if `from_member` is followed by `to_member`
# - "friends", if `from_member` and `to_member` follow each other
# - None if none of the above scenarios are applicable  
# 
# Specifications:  
# 1. `from_member` and `to_member` are user IDs (e.g. "@jobenilagan").
# 2. `social_graph` is a dictionary that adheres to the specification demonstrated in the demo cell.

# In[ ]:


social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}


def relationship_status(from_member, to_member):
    from_following = social_graph[from_member]["following"]
    to_following = social_graph[to_member]["following"]
    if to_member in from_following and from_member in to_following:
        return "friends"
    elif from_member in to_following:
        return "followed by"
    elif to_member in from_following:
        return "follower"
    else:
        return "None"


# In[ ]:


relationship_status("@chums", "@joeilagan")


# ## Problem 3: Tic Tac Toe (13 points)  
# 
# Tic Tac Toe is a common paper-and-pencil game. Players must attempt to successfully draw a straight line of their symbol across a grid. The player that does this first is considered the winner.  
# 
# Here are several possible board configurations:

# In[1]:


# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]


# **Write a function called `tic_tac_toe` that takes one positional argument (list) `board`. The function should _return_ the winner of the board if there is one, and it should return `None` if there is no winner on the board.**  
# 
# Specifications:
# 1. Each player is represented by their symbol. Example: if the player using 'X' won the board, then simply return the string 'X'.
# 2. The board may be 3x3, 4x4, 5x5, or 6x6.
# 3. The game will only ever be player X vs player O. No other symbols will be used.
# 4. There may be no winner, and there may be 1 winner, but there will never be a situation where there is more than 1 winner.

# In[ ]:


board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

def tic_tac_toe(board):
    if [board[0][i]for i in range (3)] == ['X', 'X', 'X'] or [board[0][i]for i in range (3)] == ['O', 'O', 'O']:
        return "winner"
    elif [board[1][i]for i in range (3)] == ['X', 'X', 'X'] or [board[1][i]for i in range (3)] == ['O', 'O', 'O']:
        return "winner"
    elif [board[2][i]for i in range (3)] == ['X', 'X', 'X'] or [board[2][i]for i in range (3)] == ['O', 'O', 'O']:
        return "winner"
    elif [board[i][0]for i in range (3)] == ['X', 'X', 'X'] or [board[i][0]for i in range (3)] == ['O', 'O', 'O']:
        return "winner"
    elif [board[i][1]for i in range (3)] == ['X', 'X', 'X'] or [board[i][1]for i in range (3)] == ['O', 'O', 'O']:
        return "winner"
    elif [board[i][2]for i in range (3)] == ['X', 'X', 'X'] or [board[i][2]for i in range (3)] == ['O', 'O', 'O']:
        return "winner"
    elif [board[i][i]for i in range (3)] == ['X', 'X', 'X'] or [board[i][i]for i in range (3)] == ['O', 'O', 'O']:
        return "winner"
    elif [board[2-i][i]for i in range (3)] == ['X', 'X', 'X'] or [board[2-i][i]for i in range (3)] == ['O', 'O', 'O']:
        return "winner"
    else:
        return "None"


# In[ ]:


tic_tac_toe(board3)


# ## Problem 4: Routing (13 points)
# 
# During the pandemic, a shuttle van service is tasked to travel along a predefined circular route as follows:
# 
# - UP Diliman -> Ateneo de Manila (Estimated Time: 10 mins)
# - Ateneo de Manila -> De La Salle Taft (Estimated Time: 35 mins)
# - De La Salle Taft -> UP Diliman (Estimated Time: 55 mins)
# 
# The route is one-way only. So, the van cannot go back directly to UP Diliman from Ateneo de Manila; rather, it will have to drop by De La Salle Taft first before going to UP Diliman.
# 
# 

# In[ ]:


# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}


# **Write a function called `eta` that takes three positional arguments: (dict) `legs`, (str) `source`, and (str) `destination`. The function should _return_ the estimated number of minutes it will take to reach the destination from the source based on the data stored in the `legs` dictionary.**  
# 
# Specifications:
# 1. The `legs` dictionary adheres to the schema followed in the demo cell.  
# 2. There may be more legs than shown in the demo cell.
# 3. Any destination can be reached from any source.  
# 
# Please note that you **should not hardcode this problem to only work on the example `legs` dictionary!** A secret `legs` dictionary with an unknown number of legs will be used to test this function. This secret `legs` dictionary will still represent a one-way roundabout.

# In[1]:


legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}


def eta(legs, source, destination):
    destination = False
    distance = 0

    while destination == False:
        for key in legs:
            CurrentSource = key[0]
            CurrentDest = key[1]
            LegDist = legs[key]['travel_time_mins']

            if CurrentSource == source:
                source = CurrentDest
                distance += LegDist

            if source == destination:
                destination = True
                break

    return dist 


# In[ ]:


eta(legs,"dlsu", "upd")

