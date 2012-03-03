# -*- coding: utf-8 -*-

import pybots
from time import sleep
from random import randint
from os import remove

class catbot(pybots.Bot):
	uid = "AAAAAB"
	host = "\0034,1nyan\0037nyan\0038nyan\0033nyan\00311nyan\00310nyan\00312nyan\00313nyan\003"
	user = "catbot"
	real = "nyan catbot "+open("version","r").read()

	def OnInvite(self, nick, channel):
		self.join(channel)
		self.act(channel, "bites "+nick)
		sleep(5)
		if not self.onchan(channel, "fishbot"):
			self.act(channel, "looks sad because he can't see fishbot")
			sleep(2)
			self.part(channel, ":(")
		else:
			self.act(channel, "smells fishbot")
			sleep(20)
			if self.onchan(channel):
				self.act(channel, "pounces")

	def OnChanAct(self, nick, channel, msg):
		arg = msg.lower()
		if arg == "gets the water squirter":
			possibility = randint(0, 1)
			if possibility == 0:
				self.act(channel, "hisses")
				self.part(channel, "!")
			else:
				if nick != "fishbot":
					self.act(channel, "scratches " + nick)
					self.send(":" + self.uid + " KICK " + channel + " " + nick + " :*scratch*")
				else:
					self.act(channel, "hisses")
					self.part(channel, "!")
		if nick == "fishbot":
			if arg == "dodges":
				sleep(3)
				self.part(channel, ":(")
			if arg == "is scared :(" or arg == "flaps desperately trying to escape!":
				self.send(":" + self.uid + " KICK " + channel + " " + ubots["fishbot"] + " :*bite* *munch* *munch*")
				remove("bots/" + ubots["fishbot"] + "/"+channel+".chan")
				sleep(3)
				self.act(channel, "licks his chops")
				sleep(4)
				self.part(channel, "yum")
