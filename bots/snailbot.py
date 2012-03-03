# -*- coding: utf-8 -*-

import pybots

class snailbot(pybots.Bot):
	uid = "AAAAAC"
	host = "il"
	user = "sn"
	real = "slurm slurm slurm "+open("version","r").read()

	def OnInvite(self, nick, channel):
		self.join(channel)
		self.act(channel, "waves feelers at "+nick)

	def OnChanMsg(self, nick, chan, args):
		if args.find("bbq") != -1: self.msg(chan, "omg")
		elif args.find("bo!") != -1: self.msg(chan, "selecta!")
		elif args.find("cake") != -1: self.msg(chan, "it's so delicious and moist ^_^")
		elif args.find("car") != -1: self.msg(chan, "no, sry, menocare")
		elif args.find("connoisseur") != -1: self.msg(chan, "cats go moo")
		elif args.find("CS") != -1: self.msg(chan, "BOOOM! HEADSHOT!")
		elif args.find("fish") != -1: self.msg(chan, "carrots handbags cheese.")
		elif args.find("fish go moo") != -1: self.msg(chan, "like fuck they to ¬_¬")
		elif args.find("garg") != -1: self.msg(chan, "\002\0033HULK GARG SOUP SMASH\003\002")
		elif args.find("grammer") != -1: self.msg(chan, "IT'S 'GRAMMAR' YOU RETARD")
		elif args.find("gtfo") != -1: self.msg(chan, "yes "+nick+", gtfo :p")
		elif args.find("ham") != -1: self.msg(chan, "(=^;^=) pika pi")
		elif args.find("headshot") != -1: self.msg(chan, "fps doug > "+nick)
		elif args.find("hi snailbot") != -1: self.msg(chan, "hey "+nick+" :)")
		elif args.find("impersonating fish") != -1: self.msg(chan, "do you know who else goes moo?")
		elif args.find("kenya") != -1: self.msg(chan, "is better than norway ¬_¬")
		elif args.find("knife") != -1: self.msg(chan, "what? everyone knows you run faster with a knife")
		elif args.find("KUALA LUMPUR") != -1: self.msg(chan, "i went to kuala lumpur once, didn't like it much. they served vinegar in my aftershock.")
		elif args.find("moo") != -1: self.msg(chan, "moo!")
		elif args.find("mushroom mushroom!") != -1: self.msg(chan, "dude, that was SO 2003")
		elif args.find("norway") != -1: self.msg(chan, "was peed on \o/")
		elif args.find("omg") != -1: self.msg(chan, "wtf")
		elif args.find("quake") != -1: self.act(chan, "bunnyhops")
		elif args.find("salt") != -1: self.msg(chan, "your pathetic sodium-based preservative has no effect on my ultraslime skin, puny human, now cower beforce your molluscy masters")
		elif args.find("science") != -1: self.msg(chan, "lets make neat gun")
		elif args.find("shell") != -1: self.msg(chan, "my shell is impenetrable, you will fail in your attacks")
		elif args.find("slug") != -1: self.act(chan, "fluffles on "+nick)
		elif args.find("slurm") != -1: self.msg(chan, "*slurm slurm slurm*")
		elif args.find("snailbot") != -1:  self.msg(chan, "yes?")
		elif args.find("#snailbot") != -1: self.msg(chan, "my home! :D")
		elif args.find("snails") != -1: self.msg(chan, "@\037\"\037 @\037\"\037 @\037\"\037")
		elif args.find("snail") != -1: self.msg(chan, "@\037\"\037")
		elif args.isupper(): self.msg(chan, "OMG SHOUTING")
		elif args.find("!stoptrivia") != -1: self.msg(chan, "!trivia")
		elif args.find("thanks") != -1: self.msg(chan, "np")
		elif args.find("the answer") != -1:  self.msg(chan, "42")
		elif args.find("the question") != -1: self.msg(chan, "i'll have to think about it")
		elif args.find("wtf") != -1: self.msg(chan, "bbq")
		elif args.find("xD") != -1: self.msg(chan, ":D :D :D")
		elif args.find("YA MUM") != -1: self.msg(chan, "well bite me!")

	def OnChanAct(self, nick, chan, args):
		if args.find("slaps snailbot") != -1: self.act(chan, "slurms on "+nick+" angrily")
		elif args.find("strokes snailbot") != -1: self.act(chan, "waggles antennae with glee")
