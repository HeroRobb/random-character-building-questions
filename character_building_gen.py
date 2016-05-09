#!/usr/bin/env python
#########################################################
# You'll want to edit num_of_players and out_path
# num_of_players is the amount of questions you'll generate
# out_path is where you want the .txt file saved
#
# character_building_gen.py creates a .txt file consisting of
# several randomly generated questions to get people into character
# prior to a pen and paper fantasy rpg session
#
# Do whatever you want to the script. Have fun! <3

import random, datetime, os, subprocess

num_of_players = 5
out_path = '/home/herorobb/character_building_%s.txt' % (str(datetime.datetime.now())[:10])

#character builder consists of a quantifier, an event, a reaction, and a question
quantifiers = [
	'When you were a child ',
	'During a very dry summer ',
	'On a full moon night ',
	'In the middle of your favorite holiday ',
	'During a recurring dream you used to have, ',
	'While walking through the forest one day ',
	'In an abandoned mine shaft on a tall mountain ',
	'Outside of your home while it was raining ',
	'During a particularly bitter winter ',
	'Shortly after coming into a small amount of money ',
	'On a night you couldn\'t sleep ',
	'When your best friend at the time died, ',
	'Things were particularly dry the season that ',
	'After a particularly intense night of drinking at a local tavern ',
	'During an ordinary, but cloudy, day ',
	'While you were hiding ',
	'One day, while you were gasping for breath, ',
	'On the darkest night of the year ',
	'The morning after a night you had terrible sleep paralysis ',
	'A few hours before the first time you saw a person die ',
	'The earliest memory you have was when ',
	'Early in the morning, while a church bell was tolling ']
events = [
	'a bee stung your mother\'s throat ',
	'a man you trusted implicitly disappeared ',
	'you believe you witnessed a dead woman crawling from her grave ',
	'a stranger approached you and seemed to know exactly who you are ',
	'you were not in control of your anger ',
	'you suddenly realized you needed to move to a town you had never been to ',
	'a group of elven thugs mugged you in an alley ',
	'the farms nearby your home failed to produce crops ',
	'a woman that you hated brought you a gift ',
	'the person you feared the most begged for your help ',
	'you believed you would starve to death ',
	'people around you consistently woke you up, claiming you were chanting in your sleep ',
	'you found a seeping green fog that seemed to follow you ',
	'an important leader of a remote and exotic culture came to find you ',
	'you woke up and didn\'t remember falling asleep ',
	'you realized that no one has ever truly known you ',
	'your home was destroyed ',
	'you felt a very strong desire to relax and let everything go ',
	'you felt like you could not move for several hours ',
	'someone discretely handed you a bundle of herbs ',
	'you screamed that you knew something was wrong ',
	'you watched a public execution, not quite understanding what was happening ',
	'you heard a voice whisper into your ear ']
reactions = [
	'and that night you hurt someone. ',
	'and you try not to remember it. ',
	'and you have not had a full night\'s sleep since. ',
	'and now you can no longer do the thing that you love the most. ',
	'and you wish you could change the actions you took then. ',
	'and you have had moments of \'missing time\' occasionally since then. ',
	'and now can never eat your favorite meal again. ',
	'and you have always gorged yourself whenever possible during meals since. ',
	'and now you always check the exits of every building as soon as you enter. ',
	'and you refused to give someone something they desparately needed the next day. ',
	'and occasionally you feel the same as you did then. ',
	'but now you are not sure if this actually happened. ',
	'and you made it a point to let everyone know. ',
	'and what you did afterwards bothers you every day. ',
	'and you ended up associating with less than savory characters. ',
	'and you realized that this doesn\'t bother you as much as it would others. ',
	'and you cannot quite piece together what happened afterwards. ',
	'but you decided to run away. ',
	'and people seem to find out about this even though you wish they didn\'t. ',
	'but, despite what most people think, you honestly had no idea what was happening. ',
	'but no one seemed to react at all. ',
	'but you just told yourself it had to be that way. ',
	'but that\'s all behind you now. ']
questions = [
	'What caused this?',
	'Why was this important to you?',
	'What made this the darkest event in your life?',
	'How is your life different since then?',
	'Why do you still remember this?',
	'Why do you smile when you think of this?',
	'How do you remember this differently than others who were there?',
	'Why has nothing been the same since?',
	'If you could go back in time, how would you change this?',
	'Why is this reassurring to you? ',
	'Who would be upset if they found out about this?',
	'What was the last thing that reminded you of this?',
	'What is the most troubling thing about this?',
	'Does this memory come up often for you?',
	'Would you say this changed who you are?',
	'Who haven\'t you personally told about this?',
	'Do you feel like this was fair?']
character_builders = []
rQuant = []
rEvent = []
rReact = []
rQuest = []


#generate a key for each section of the character builder and check for uniqueness
for i in range(num_of_players):
	new_add = random.randint(0, len(quantifiers)-1)
	while new_add in rQuant:
		new_add = random.randint(0, len(quantifiers)-1)
	rQuant.append(new_add)
			
	new_add = random.randint(0, len(events)-1)
	while new_add in rEvent:
		new_add = random.randint(0, len(events)-1)
	rEvent.append(new_add)
		
	
	new_add = random.randint(0, len(reactions)-1)
	while new_add in rReact:
		new_add = random.randint(0, len(reactions)-1)
	rReact.append(new_add)
		
	new_add = random.randint(0, len(questions)-1)
	while new_add in rQuest:
		new_add = random.randint(0, len(questions)-1)
	rQuest.append(new_add)

#use the keys to find a unique character building question for each player
for j in range(num_of_players):
	character_builders.append(str(j + 1) + ": " + quantifiers[rQuant[j]] + events[rEvent[j]] + reactions[rReact[j]] + questions[rQuest[j]] + '\n\n')

# open gedit and paste the character building questions
outFile = open(out_path, 'w')

for entry in character_builders:
	outFile.write(entry)

print("Currently can generate %s possible questions" % (str(len(quantifiers) * len(events) * len(reactions) * len(questions))))

outFile.close()
#try:
	#subprocess.Popen(['start', out_path], shell=False)
#except Exception as err:
	#print 'unable to find windows default program ' + str(err)
#try:
	#subprocess.Popen(['open', out_path], shell=False)
#except Exception as err:
	#print 'unable to find osx default program ' + str(err)
#try:
	#subprocess.Popen(['see', out_path], shell=False)
#except Exception as err:
	#print 'unable to find linux default program ' + str(err)
os.system("gedit " + out_path)
