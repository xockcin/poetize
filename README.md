# POETIZE

## A Python program that writes poems

### 0.Preface

I got the idea for this program from an article I read about a machine learning algorithm that studies Shakespeare and then tries to write sonnets. And it occurred to me: that's exactly how real-life bad poets write their bad poetry. It is often said that bad poets imitate and good poets steal. If you write a program that writes poems through imitation, that program will write bad poetry. If you want your program to write good poetry, you need to program it to steal.

### 1.Problem

The poems this program writes should conform to three criteria:
1. They should scan.
2. They should rhyme.
3. They should be grammatically correct.

The first will be easy to accomplish, the second somewhat harder, the third harder still, but none will be anywhere near impossible.

### 2.Meter

The first task will involve building a database of words, where each line in the database includes a string for the word, a number for the word's syllable count and a boolean for whether the word is stressed or unstressed. Once you have that, the rest is easy.

I should note that the question of which syllable has the emphasis is not important. Polysyllabic words have primary and secondary stresses, and they usually alternate. What matters most is whether the first syllable is stressed or unstressed. 

Think of it like Tetris. The tiles are words and the squares are syllables. In this version of Tetris, the tiles are all just vertical rods of various lengths. Imagine the squares on the tiles alternate between black and white. Your job is to build a wall ten squares wide and fourteen squares tall, with alternating stripes of black and white, starting with the a black stripe. Every time you put a tile down, you would need to know the following things:
1. How many squares you still need to fill in this row.
2. Whether the rightmost square of the previous tile was black or white - which can be inferred from whether the answer to 1 is even or odd.

So really, you only need to know one thing - that is, in order to know what the criteria for the next tile should be. To restate it more clearly: Given the number of squares left to fill in this row, the next tile should be that many squares or fewer. Also, if the number is even, that tile's leftmost square should be black and if the number is odd that tile's leftmost square should be white. If the number is zero, end it and move on to the next row.

Replace "tiles" with "words" and "squares" with "syllables" and those are the rules for how you write blank verse. The first version of this program will simply produce random sequences of words that obey those criteria.

### 3.Rhyming

This will be trickier. The crucial thing to note is that rhyming is strictly transitive. If A rhymes with B and B rhymes with C, then A must rhyme with C. So words that rhyme with each other can be organized into groups. So really it's a simple matter of going through the word database and, for each word, doing the following:
1. Ask if it has a "rhyme group number" yet.
2. If not, look it up in a rhyming dictionary, then assign a number to itself and all the words in the database that match it.

At runtime, it will be a simple matter of requiring, if a word is to be the last word in its line, and there's another line it's supposed to rhyme with, that it have the same rhyme group number as the word it's supposed to rhyme with.

### 4.Syntax

Here's where it gets interesting! Syntax is essentially a set of rules for what word can come next in a sentence given what words have come before. It has nothing to do with how long the word is or what it sounds like. What matters is the part of speech as well as number, person, tense etc. Every word has a part of speech, and many words, although by no means all, have a secondary grammatical category like number or tense.

Let's explore this a little. Say we are starting a sentence. What range of words may be choose from? Articles, yes. Pronouns, nominative or possessive, yes. Adjectives, yes. Nouns, some but not all, because some nouns need an article. "Love" is fine, so is "John," but not "giraffe" or "journey." We will need a way of modelling that. So we choose "The" as our first word. What can our next word be? Not an article, not a pronoun. Adjective, yes. Noun, yes. Verb, yes but only certain forms: participial but not declarative. You can say "The destroying" or "The destroyed" but not "The destroy". However, the declarative form of most common verbs is also a noun: e.g. run, walk, punch, rain, blow. Say we choose a noun: "giraffe." So our sentence is now "The giraffe." What can our next word be? This time, not an adjective. But it could be a declarative present tense or past tense verb. If it's a verb, it has to be the right conjugation, i.e. "runs" not "run." So let's pick "The giraffe runs." What can the next word be? Natural language users such as ourselves, if it were our decision, would probably pick a preposition, e.g. "The giraffe runs across...", and at this point our minds are already groping toward the seemingly inevitable article and noun to bring the sentence to its conclusion: "The giraffe runs across the field."

But hold on! Did the word after "runs" have to be a preposition? Prepositions often go between intransitive verbs and their indirect objects. But is "runs" not also a transitive verb? What if instead of a preposition, we followed it with an article and a noun? Then we would get something like: "The giraffe runs a lawnmower".

Nowadays, a lot of work in NLP seems to be based around statistical analysis. I'm not so interested in that. Instead of the question of, given what words have come so far, what word will probably come next, I am intersted in the question of, given what *types* of words have come so far, what *types* of words are *allowed* to come next, according to the rules of grammar.

I could use statistical analysis, and I probably will play around with it a little bit, but at the end of the day it is mostly unnecessary and potentially misleading.

The first task here is to figure out how to model word type. Let's think about the word "giraffe." It's a noun, first of all. It's a singular noun. Also, it's not a proper noun or a mass noun, so it needs an article. Perhaps it would be enough to say, it needs an article, without specifying why.

I should take a moment to say that at this point I care absolutely not one bit about semantics. All that matters is syntax. This program might produce a sentence like "The giraffe ran across the field," but it also might produce a sentence like "The saxophone voyaged above the salutation," and according to my rules those two sentences would be equally valid.

In order to have a rule-based syntax, it might be wise to begin not with rules for determining what type of word can come next given what types of words have come before, but rather a few scripts that say explicitly, in advance, what the syntax of the sentence will be. Syntactic structures in sentences are like chord progressions in pop songs: In theory there are a potentially infinite number, but in practice there are actually only a few handfuls that people actually use. 

So this part of the program looks like so:
1. Give every word in the database a set of syntactic metadata that includes a required part of speech as well as an optional set of additional categories like number, tense, etc.
2. Put together a compendium of "sentence scripts" that determine the sequence of words in a sentence based on their syntactical metadata.
3. Write a program that selects sequences from the database, according to the given sentence scripts, while also adhering to the strictures of the meter and rhyme rules.

Within those restrictions, it can select words at random.

### 5."Good poets steal"

Eventually I intend to write a stealing function, which will crawl through texts and pick out sections that are in iambic pentameter or whichever other metrical scheme, to incorporate into poems. But I can save that for later.

### 6.Implementation.

The first iteration of this project will be a simple command-line program that prints the completed poem to standard output. The smart thing would be to eventually turn it into a web-app, a sort of workstation for poets. But again, that can come later.

The first task is to create the word database with syllables and stress, which
can begin its life as a simple CSV file. I will create it by putting the CMU
wordlist through a simple Python script.
