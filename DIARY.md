### 2/12/21

In order to create my word database, I need to do the following things:

1. Make a sublist of words I want to include. The CMU list has far too many - I will find and use a list of say the 3000 most common words. First task is to find this list and set aside just the lines representing the words I want. There are clever ways of doing this; I will probably use a simple for loop.

2. Once we have just the lines we want, we go through them one by one. For each one, we split it at the spaces, record the zero index in the ensuing list as the word, record the number of occurences of 0 or 1 in the remainder of the line as the number of syllables, and record the Boolean "stressed" as false if the first number that occurs is 0 or true if it is something other than zero.

3. Write it to a file! Then make it into a SQL database. I will have to remind myself of the CSV and SQL Python libraries.