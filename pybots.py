#!/usr/bin/env python

import os
import sys
import time
import socket
import __builtin__
import ConfigParser
import thread

__version__ = open("version", "r").read()

import bots

class PyBots:
	def __init__(self, conffile):
		self.config = dict()
		self.nicklist = dict()
		config = ConfigParser.RawConfigParser()
		config.read(conffile)
		self.conffile = conffile
		for section in config.sections():
			for item in config.items(section):
				self.config[section,item[0]] = item[1]
		self.id = self.config["SERVICES", "id"]
		self.bots = dict()

	def run(self):
		self.con = socket.socket()
		self.con.connect((self.config["SERVER", "address"], int(self.config["SERVER", "port"])))
		self.send("SERVER %s %s 0 %s :%s" % (self.config["SERVICES", "name"], self.config["SERVER", "password"], self.config["SERVICES", "id"], self.config["SERVICES", "description"]))
		self.send(":%s BURST" % self.id)
		self.send(":%s ENDBURST" % self.id)
		__builtin__.con = self.con
		__builtin__.nicklist = self.nicklist
		for bot in dir(bots):
			if os.access("bots/"+bot+".py", os.F_OK):
				exec("bot_uid = bots."+bot+"."+bot+".uid")
				exec("bot_host = bots."+bot+"."+bot+".host")
				exec("bot_user = bots."+bot+"."+bot+".user")
				exec("bot_real = bots."+bot+"."+bot+".real")
				self.send(":%s UID %s %s %s %s %s %s 0.0.0.0 %s + :%s" % (self.id, self.id+bot_uid, time.time(), bot, bot_host, bot_host, bot_user, time.time(), bot_real))
				self.bots[self.id+bot_uid] = bot
				if not os.access("bots/"+self.id+bot_uid, os.F_OK):
					os.mkdir("bots/"+self.id+bot_uid)
				else:
					for file in os.listdir("bots/"+self.id+bot_uid):
						os.remove("bots/"+self.id+bot_uid+"/"+file)
		while 1:
			try:
				recv = self.con.recv(25600)
				if not recv:
					self.con.close()
					sys.exit(0)
				for line in recv.splitlines():
					print("<< "+line)
					lined = line.split()
					if len(lined) > 2:
						if lined[1] == "PING":
							self.send(":%s PONG %s %s" % (self.id, self.id, lined[2]))
							self.send(":%s PING %s %s" % (self.id, self.id, lined[2]))
						if lined[1] == "UID":
							self.nicklist[lined[2]] = lined[4]

						if lined[1] == "INVITE":
							nick = self.nicklist[lined[0][1:]]
							if self.bots.has_key(lined[2]):
								exec("""bots.%s.%s("%s", "%s").OnInvite("%s", "%s")""" % (self.bots[lined[2]], self.bots[lined[2]], lined[2], self.conffile, nick, lined[3]))
						if lined[1] == "KICK":
							if self.bots.has_key(lined[3]):
								if os.access("bots/"+lined[3]+"/"+lined[2]+".chan", os.F_OK):
									os.remove("bots/"+lined[3]+"/"+lined[2]+".chan")
						if lined[1] == "IDLE" and len(lined) == 3:
							if self.bots.has_key(lined[2]):
								self.send(":"+lined[2]+" IDLE "+lined[0][1:]+" 0 0")
						if lined[1] == "PRIVMSG":
							nick = self.nicklist[lined[0][1:]]
							for bot in self.bots.keys():
								if os.access("bots/"+bot+"/"+lined[2]+".chan", os.F_OK):
									text = ' '.join(lined[3:])[1:]
									if text.startswith("\001ACTION") and text.endswith("\001"):
										exec("""thread.start_new_thread(bots.%s.%s("%s", "%s").OnChanAct,("%s", "%s", "%s"))""" % (self.bots[bot], self.bots[bot], bot, self.conffile, nick, lined[2], text[8:-1]))
									else:
										exec("""thread.start_new_thread(bots.%s.%s("%s", "%s").OnChanMsg,("%s", "%s", "%s"))""" % (self.bots[bot], self.bots[bot], bot, self.conffile, nick, lined[2], text.replace("\"", "\\\"")))
			except:
				self.con.close()
				return 1


	def send(self, message):
		self.con.send(message+"\n")
		print(">> "+message)

class Bot:
	uid = ""
	user = ""
	host = ""
	real = ""

	def __init__(self, uid="", conffile=""):
		self.config = dict()
		self.nicklist = nicklist
		config = ConfigParser.RawConfigParser()
		config.read(conffile)
		for section in config.sections():
			for item in config.items(section):
				self.config[section,item[0]] = item[1]
		self.id = self.config["SERVICES", "id"]
		self.con = con
		self.uid = uid

	def OnPrivMsg(self, sNick, sMessage):
		pass

	def OnChanMsg(self, sNick, sChannel, sMessage):
		pass

	def OnChanAct(self, sNick, sChannel, sMessage):
		pass

	def OnInvite(self, sNick, sChannel):
		pass

	def send(self, message):
		self.con.send(message+"\n")
		print(">> "+message)

	def msg(self, target, message):
		if target.startswith("#"):
			self.send(":"+self.uid+" PRIVMSG "+target+" :"+message)
		else:
			self.send(":"+self.uid+" NOTICE "+target+" :"+message)

	def act(self, target, message):
		self.send(":"+self.uid+" PRIVMSG "+target+" :\001ACTION "+message+"\001")

	def join(self, channel):
		self.send(":"+self.uid+" JOIN "+channel)
		open("bots/"+self.uid+"/"+channel+".chan", "w").write("")

	def part(self, channel):
		self.send(":"+self.uid+" PART "+channel)
		os.remove("bots/"+self.uid+"/"+channel+".chan")

	def find(self, string, term):
		if string.find(term) != -1:
			return True
		return False

if __name__ == "__main__":
	if len(sys.argv) == 1:
		while True:
			print("PyBots (" + __version__ + ") started")
			PyBots("config.cfg").run()
			print("PyBots (" + __version__ + ") stopped")
			time.sleep(5)
	else:
		while True:
			print("PyBots (" + __version__ + ") started")
			PyBots(sys.argv[1]).run()
			print("PyBots (" + __version__ + ") stopped")
			time.sleep(5)

