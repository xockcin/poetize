### 2/12/21

In order to create my word database, I need to do the following things:

1. Make a sublist of words I want to include. The CMU list has far too many - I will find and use a list of say the 3000 most common words. First task is to find this list and set aside just the lines representing the words I want. There are clever ways of doing this; I will probably use a simple for loop.

2. Once we have just the lines we want, we go through them one by one. For each one, we split it at the spaces, record the zero index in the ensuing list as the word, record the number of occurences of 0 or 1 in the remainder of the line as the number of syllables, and record the Boolean "stressed" as false if the first number that occurs is 0 or true if it is something other than zero.

3. Write it to a file! Then make it into a SQL database. I will have to remind myself of the CSV and SQL Python libraries.


### 2/15/21

The "makewordlist.py" script now writes its output to a CSV file, which I now have. Given the small number of items in the database, I think getting into SQL would be unnecessary. What I will do instead is this:

1. Import the CSV file and turn it into a list of lists, where each list is a word, its syllable count and its stress.
2. Divide the list into two: stressed and unstressed.
3. Make the two lists into dictionaries, where the word is the key and the syllable count is the value.

OK, that's done. The next task is to write the function that actually writes a line of poetry. But first, a few interesting insights:

1. Of the 998 words in my list, only 174 are unstressed.
2. Among the stressed words, 470 (more than half) are one syllable, 247 are two syllables and 85 are three syllables.
3. Unstressed words are mostly two syllables, although 40 are three syllables and 26 are two syllables.
4. The one six syllable word is "responsibility".

OK, I have written the function to write a line. The first line it wrote:
"AVAILABLE COMPUTER START MACHINE"

What hath God wrought??

OK, now my program has written its first poem, and I am seeing a few bugs that I will need to deal with:
1. 1000 words is not enough words! Even in the space of fourteen lines I am getting some awkward repeats.
2. Some of the words are misclassified - "DECADE", for instance, is listed under "unstressed".
3. The writeline function is written so that, if a word is to be the last word in the line, it is not constrained to the correct number of syllables. That will be easy to fix.
4. The two-dictionary approach is awkward. I will be better off finding a way to organize all the words into a single entity.

Still, this is great progress! I'm excited to keep working on this project.
