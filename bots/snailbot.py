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
		if args.find("xD") != -1:
			self.msg(chan, ":D :D :D")
		if args.find("ham") != -1:
			self.msg(chan, "(=^;^=) pika pi")
