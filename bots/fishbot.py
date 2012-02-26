# -*- coding: utf-8 -*-

import pybots

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
		if arg.find("aftershock") != -1: self.msg(chan, "mmm. Aftershock.")
		elif arg.startsiwith("fish go"):
			if arg.split()[2] == "moo" or arg.split()[2] == "mo0" or arg.split()[2] == "m0o" or arg.split()[2] == "m00":
				self.act(chan, "notes that "+nick+" is truly enlightened.")
			else:
				self.msg(chan, nick+" LIES! Fish don't go "+' '.join(msg.split()[2:])+"! fish go m00!")
