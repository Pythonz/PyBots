# -*- coding: utf-8 -*-

import pybots

class catbot(pybots.Bot):
	uid = "AAAAAB"
	host = u"\0034,1nyan\0037nyan\0038nyan\0033nyan\00311nyan\00310nyan\00312nyan\00313nyan\003"
	user = "catbot"
	real = "nyan catbot "+open("version","r").read()

	def OnInvite(self, nick, channel):
		self.join(channel)
		self.act(channel, "bites "+nick)
