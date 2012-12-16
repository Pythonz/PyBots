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
		if self.find(args, "bbq"): self.msg(chan, "omg")
		elif self.find(args, "bo!"): self.msg(chan, "selecta!")
		elif self.find(args, "cake"): self.msg(chan, "it's so delicious and moist ^_^")
		elif self.find(args, "car"): self.msg(chan, "no, sry, menocare")
		elif self.find(args, "connoisseur"): self.msg(chan, "cats go moo")
		elif self.find(args, "CS"): self.msg(chan, "BOOOM! HEADSHOT!")
		elif self.find(args, "fish"): self.msg(chan, "carrots handbags cheese.")
		elif self.find(args, "fish go moo"): self.msg(chan, "like fuck they to ¬_¬")
		elif self.find(args, "garg"): self.msg(chan, "\002\0033HULK GARG SOUP SMASH\003\002")
		elif self.find(args, "grammer"): self.msg(chan, "IT'S 'GRAMMAR' YOU RETARD")
		elif self.find(args, "gtfo"): self.msg(chan, "yes "+nick+", gtfo :p")
		elif self.find(args, "ham"): self.msg(chan, "(=^;^=) pika pi")
		elif self.find(args, "headshot"): self.msg(chan, "fps doug > "+nick)
		elif self.find(args, "hi snailbot"): self.msg(chan, "hey "+nick+" :)")
		elif self.find(args, "impersonating fish"): self.msg(chan, "do you know who else goes moo?")
		elif self.find(args, "kenya"): self.msg(chan, "is better than norway ¬_¬")
		elif self.find(args, "knife"): self.msg(chan, "what? everyone knows you run faster with a knife")
		elif self.find(args, "KUALA LUMPUR"): self.msg(chan, "i went to kuala lumpur once, didn't like it much. they served vinegar in my aftershock.")
		elif self.find(args, "moo"): self.msg(chan, "moo!")
		elif self.find(args, "mushroom mushroom!"): self.msg(chan, "dude, that was SO 2003")
		elif self.find(args, "norway"): self.msg(chan, "was peed on \o/")
		elif self.find(args, "omg"): self.msg(chan, "wtf")
		elif self.find(args, "quake"): self.act(chan, "bunnyhops")
		elif self.find(args, "salt"): self.msg(chan, "your pathetic sodium-based preservative has no effect on my ultraslime skin, puny human, now cower beforce your molluscy masters")
		elif self.find(args, "science"): self.msg(chan, "lets make neat gun")
		elif self.find(args, "shell"): self.msg(chan, "my shell is impenetrable, you will fail in your attacks")
		elif self.find(args, "slug"): self.act(chan, "fluffles on "+nick)
		elif self.find(args, "slurm"): self.msg(chan, "*slurm slurm slurm*")
		elif self.find(args, "#snailbot"): self.msg(chan, "my home! :D")
		elif self.find(args, "snailbot"):  self.msg(chan, "yes?")
		elif self.find(args, "snails"): self.msg(chan, "@\037\"\037 @\037\"\037 @\037\"\037")
		elif self.find(args, "snail"): self.msg(chan, "@\037\"\037")
		elif self.find(args, "!stoptrivia"): self.msg(chan, "!trivia")
		elif self.find(args, "thanks"): self.msg(chan, "np")
		elif self.find(args, "the answer"):  self.msg(chan, "42")
		elif self.find(args, "the question"): self.msg(chan, "i'll have to think about it")
		elif self.find(args, "wtf"): self.msg(chan, "bbq")
		elif self.find(args, "xD"): self.msg(chan, ":D :D :D")
		elif self.find(args, "YA MUM"): self.msg(chan, "well bite me!")
		elif args.isupper() and len(args.split()) > 1: self.msg(chan, "OMG SHOUTING")

	def OnChanAct(self, nick, chan, args):
		if self.find(args, "slaps snailbot"): self.act(chan, "slurms on "+nick+" angrily")
		elif self.find(args, "strokes snailbot"): self.act(chan, "waggles antennae with glee")
