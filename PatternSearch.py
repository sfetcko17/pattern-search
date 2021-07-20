import re

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''


regex = '[^a-zA-Z\d]' # create a regular expression excluding all alphanumeric characters

result = re.findall(regex,lorem_ipsum) # use the RE to find non-alphanumeric characters

print(len(result)) # print the number of non-alphanumeric characters

regex = 'sit[-:]amet' #create a regular expression to find all instances of sit-amet or sit:amet

occurrance_sit_amet = re.findall(regex,lorem_ipsum) # find all of the occurences of sit-amet or sit:amet in the string

print(len(occurrance_sit_amet)) # print the amount of instances found in the string

regex = 'sit[-:]amet' #create a regular expression to find all instances of sit-amet or sit:amet

replace_results = re.sub(regex, 'sit amet', lorem_ipsum) # create a replacement for all instances of sit-amet or sit:amet in the string

occurrance_sit_amet = re.findall(regex, lorem_ipsum) # find all of the new instances in the string and assign a variable

print(len(occurrance_sit_amet)) # print the amount of instances found of the new variable in the string
