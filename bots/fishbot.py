# -*- coding: utf-8 -*-

import pybots
from fnmatch import fnmatch

class fishbot(pybots.Bot):
	uid = "AAAAAA"
	host = "go.moo.oh.yes.they.do"
	user = "fish"
	real = "Teh f1shb0t <°)))))>< "+open("version","r").read()

	def OnInvite(self, nick, channel):
		self.join(channel)
		self.act(channel, "m00s contentedly on "+nick+".")

	def OnChanMsg(self, nick, chan, msg):
		arg = msg.lower()
		if arg.startswith("fish go "):
			if arg.split()[2] == "moo" or arg.split()[2] == "mo0" or arg.split()[2] == "m0o" or arg.split()[2] == "m00":
				self.act(chan, "notes that "+nick+" is truly enlightened.")
			else:
				self.msg(chan, nick+" LIES! Fish don't go "+' '.join(msg.split()[2:])+"! fish go m00!")
		elif arg.startswith("fishbot doesnt know about "): self.msg(chan, "Perhaps I'm just not telling...")
		elif arg.startswith("!invite fishbot #"): self.msg(chan, "Shan't.")
		elif arg.startswith("you know who else "): self.msg(chan, nick+": YA MUM!")
		elif arg == "aftershock vinegar": self.msg(chan, "Ah, a true connoisseur!")
		elif arg == "aftershock": self.msg(chan, "mmm. Aftershock.")
		elif arg == "ag": self.msg(chan, "Ag, ag ag ag ag ag AG AG AG!")
		elif arg == "ammuu?": self.msg(chan, nick+": fish go m00 oh yes they do!")
		elif arg == "atlanis": self.msg(chan, "Beware the underwater headquarters of the trout and their bass henchmen. From there they plan their attacks on other continents.")
		elif arg == "badger badger badger badger badger badger badger badger badger badger badger badger": self.msg(chan, "mushroom mushroom!")
		elif arg == "bass": self.msg(chan, "Beware of the mutant sea bass and their laser cannons!")
		elif arg == "bounce": self.msg(chan, "moo")
		elif arg == "cake": self.msg(chan, "fish")
		elif arg == "carrots handbags cheese.": self.msg(chan, "...toilets russians planets hamsters weddings poets stalin KUALA LUMPUR! pygmys budgies KUALA LUMPUR!")
		elif arg == "cows go moo": self.msg(chan, nick+": only when they are impersonating fish.")
		elif arg == "crack": self.msg(chan, "Doh, there goes another bench!")
		elif arg == "embenzalmine nitrotomine": self.msg(chan, "A pleasant-tasting, thirst-quenching drink, enjoyed by all.")
		elif arg == "everyone is different": self.msg(chan, "No two people are not on fire.")
		elif arg == "files don't just disappear!": self.msg(chan, "They do if you drop them down an elevator shaft...")
		elif arg == "fishbot: muahahaha. ph33r the dark side. :)": self.msg(chan, nick+": You smell :P.")
		elif arg == "fishbot owns": self.msg(chan, "Aye, I do.")
		elif arg == "fishbot created splidge": self.msg(chan, "omg no! Think I could show my face around here if I was responsible for THAT?")
		elif arg == "hello fishbot": self.msg(chan, "Hi "+nick+"!")
		elif arg == "how much does fishbot cost": self.msg(chan, "Almost a thousand pounds.")
		elif arg == "how old is fishbot?": self.act(chan, "is older than time itself.")
		elif arg == "fishbot": self.msg(chan, "yes?")
		elif arg == "fishcakes": self.msg(chan, "fish")
		elif arg == "fish": self.msg(chan, nick+": fish go m00!")
		elif arg == "flibble": self.msg(chan, "plob")
		elif arg == "hampster": self.msg(chan, nick+": There is no 'p' in hamster you retard.")
		elif arg == "herring": self.msg(chan, "herring(n): Useful device for chopping down tall trees. Also moos (see fish).")
		elif arg == "hundreds and thousands": self.msg(chan, "MEDI.. er.. FISHBOT")
		elif arg == "if there's one thing I know for sure, it's that fish don't m00.": self.msg(chan, nick+": HERETIC! UNBELIEVER!")
		elif arg == "i know kungfu": self.msg(chan, "Show me.")
		elif arg == "imhotep": self.msg(chan, "Imhotep is invisible.")
		elif arg == "i want everything": self.msg(chan, "Would that include a bullet from this gun?")
		elif arg == "just then, he fell into the sea": self.msg(chan, "Ooops!")
		elif arg == "kangaroo": self.msg(chan, "The kangaroo is a four winged stinging insect.")
		elif arg == "martian": self.msg(chan, "Don't run! We are your friends!")
		elif arg == "moo?": self.msg(chan, "To moo, or not to moo, that is the question. Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fish...")
		elif arg == "mr. slim": self.msg(chan, "Mr. Slim can be reached on extension 2754.")
		elif arg == "no it isn't": self.msg(chan, "Yes it is!")
		elif arg == "now there's more than one of them?": self.msg(chan, "A lot more.")
		elif arg == "oh god": self.msg(chan, "fishbot will suffice.")
		elif arg == "sledgehammer": self.msg(chan, "sledgehammers go quack!")
		elif arg == "snaffles a cookie off fishbot.": self.msg(chan, ":(")
		elif arg == "snake": self.msg(chan, "Ah snake a snake! Snake, a snake! Ooooh, it's a snake!")
		elif arg == "some people are about to be run over": self.msg(chan, "Frankie has about 5 seconds.")
		elif arg == "some people are being fangoriously devoured by a gelatinous monster": self.msg(chan, "Hillary's legs are being digested.")
		elif arg == "some people have rigged the enemy base with explosives": self.msg(chan, "Albert has.")
		elif arg == "spoon": self.msg(chan, "There is no spoon.")
		elif arg == "thanks fishbot": self.msg(chan, "Thishbot.")
		elif arg == "trout": self.msg(chan, "Trout are freshwater fish and have underwater weapons.")
		elif arg == "trout go moo": self.msg(chan, "Aye, that's cos they're fish.")
		elif arg == "vinegar": self.msg(chan, "Nope, too sober for vinegar. Try later.")
		elif arg == "vinegar aftershock": self.msg(chan, "Ah, a true connoisseur!")
		elif arg == "we are getting aggravated": self.msg(chan, "Yes, we are.")
		elif arg == "wertle": self.msg(chan, "moo")
		elif arg == "what are birds?": self.msg(chan, "We just don't know.")
		elif arg == "what does maths stand for?": self.msg(chan, "Mathematical Anti Telharsic Harfatum Septomin.")
		elif arg == "what do you need?": self.msg(chan, "Guns. Lots of guns.")
		elif arg == "what is the matrix?": self.msg(chan, "No-one can be told what the matrix is. You have to see it for yourself.")
		elif arg == "where are we?": self.msg(chan, "Last time I looked, we were in "+chan+".")
		elif arg == "where do you want to go today?": self.msg(chan, "anywhere but redmond :(.")
		elif arg == "why are you here?": self.msg(chan, "Same reason. I love candy.")
		elif arg == "would you like to play a game?": self.msg(chan, "The only winning move is not to play.")
		elif arg == "www.outwar.com": self.msg(chan, "would you please GO AWAY with that outwar rubbish!")
		elif arg == "you can't just pick people at random!": self.msg(chan, "I can do anything I like, you, I'm eccentric! Rrarrrrrgh! Go!")

	def OnChanAct(self, nick, chan, msg):
		arg = msg.lower()
		if arg == "has returned from playing counterstrike": self.msg(chan, "like we care fs :(")
		elif arg == "mafipulates fishbot": self.act(chan, "changes colour from invisible to brown.")
		elif arg == "pours water on fishbot": self.msg(chan, "Ruined.")
		elif arg == "strokes fishbot": self.act(chan, "m00s loudly at you.")
		elif arg == "thinks happy thoughts about pretty ladies.": self.act(chan, "has plenty of pretty ladies. Would you like one, you?")
		elif fnmatch(arg, "slaps * around a bit with a large trout"): self.msg(chan, "trouted!")

		if nick == "catbot":
			if arg == "smells fishbot":
				self.send(":"+self.uid+" KICK "+chan+" catbot :smell this!")
