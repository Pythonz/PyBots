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
