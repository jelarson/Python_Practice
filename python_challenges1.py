# Challenge 1: Find the Length of a String
# ex: "The" => 3

string = "This string is soooooooo long!"
print(len(string)) # -> function that finds length of selected string

#function
def string_length(string):
  return len(string)

print(string_length(string))


# Challenge 2: Create One String From Multiple Strings
  # ex: 
  # string1 = "the"
  # string2 = "dog"
  # output => "the dog"

string1 = 'This string is '
string2 = 'amazing!'
string3 = string1 + string2 # -> combines two selected strings into one
print(string3)

#function
def combine_strings(*args):
  return ''.join(args)

print(combine_strings(string1, string2))

# Challenge 3: Swap first and last characters in a string
# Ex: "the dog" => "ghe doT"
# "ABCD" => "DBCA"
# "WINDOWS" => "SINDOWW"

string = "Hello"
first_let = string[0] # -> Create string with first letter of original string
last_let = string[-1] # -> create string with last letter of original string
new_string = last_let + string[1:] # -> make new string putting last letter in original string (missing it's first letter)
newer_string = new_string[0:-1] + first_let # -> take new string and remove last letter - combine it with string containing first letter
print(newer_string)

#function
def new_str():
  return (string[-1:] + string[1:-1] + string[:1])
print(new_str())

# Challenge 4: Sum all items in a list
# EX: [1, 2, 3] => 6

list1 = [1,2,3,4,5]
print(sum(list1))  # -> function that adds up the numbers in a list

#function
def sum_items(*args):
  return (sum(list1))
print(sum_items(list1))

# Challenge 5: Take list of words and return the longest one along with its length:
# EX: ["PHP", "Backend", "Exercises"]
# output => Longest Word: Exercises, Length: 9

list1 = ['Jess', 'E', 'Larson']
list2 = max(list1) # -> find longest word in list
list3 = len(list2) # -> find length of list2 - which is longest word in list
print("Longest string: " + str(list2) + " - Longest string length: " + str(list3))

#function
def long_short_word(words):
  longest_word = words[0]
  shortest_word = words[0]

  for word in words:
    if len(word) >= len(longest_word):
      longest_word = word
      longest_len = len(word)
    

  return ("Longest string: " + str(longest_word) + " - longest string length: " + str(longest_len)) 

print(long_short_word(list1))   

# Challenge 6: Replace all occurrences of the first letter in string with '$' EXCEPT for the first letter itself.
# EX: "racecar" => "raceca$"
# "retrofit" => "ret$ofit"
# "talkative" => "talka$ive"
# "bobby" => "bo$$y"

string = 'sassy'
first_let = string[0] # -> create string of first letter of original string
new_string = string[1:] # -> creat new_string that doesn't include first letter
newer_string = new_string.replace(first_let, '$') # -> take new_string and replace antything that matches first_let with a $
print(first_let + newer_string)

#function

def character_replace(string):
  replacement_list = []

  for letter in string[1:]:
    if letter == string [0]:
      replacement_list.append("$")
    else:
      replacement_list.append(letter)

  return f'{string[0]}{"".join(replacement_list)}'
print(character_replace('racecar'))  

 

# Do your best. Challenge yourselves and try to make all of these their own functions (optional). Good Luck, and great job today!