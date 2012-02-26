# -*- coding: utf-8 -*-

import pybots

class fishbot(pybots.Bot):
	uid = "AAAAAA"
	host = "go.moo.oh.yes.they.do"
	user = "fish"
	real = "Teh f1shb0t <°)))))><"

	def OnInvite(self, nick, channel):
		self.join(channel)
		self.act(channel, "m00s contentedly on "+nick+".")
