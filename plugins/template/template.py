#!/usr/bin/python
# -*- coding: cp1252 -*-

#########
# USAGE
#
#	Config
# ======
# to read a option from config File
# VALUE = globals.config.get("SECTION", "OPTION")
#
# Data from boswatch.py
# =====================
# use data["KEY"] for Alarm Data from boswatch.py
# for usable KEYs in different Functions (FMS|ZVEI|POC) see interface.txt
#
# LOG Messages
# ============
# send Log Messages with logging.LOGLEVEL("MESSAGE")
# usable Loglevels debug|info|warning|error|exception|critical
# if you use .exception in Try:Exception: Construct, it logs the Python EX.message too

import logging # Global logger

from includes import globals  # Global variables

##
#
# Main function of plugin
# will be called by the alarmHandler
#
def run(typ,freq,data):
	"""
	This function is the implementation of the Plugin.
	
	If necessary the configuration hast to be set in the config.ini.

	@type    typ:  string (FMS|ZVEI|POC)
	@param   typ:  Typ of the dataset
	@type    data: map of data (structure see interface.txt)
	@param   data: Contains the parameter for dispatch
	@type    freq: string
	@keyword freq: frequency of the SDR Stick

	@requires:  If necessary the configuration hast to be set in the config.ini.
	
	@return:    nothing
	"""
	try:
		#
		# ConfigParser
		#
		logging.debug("reading config file")
		try:
			for key,val in globals.config.items("template"):
				logging.debug(" - %s = %s", key, val)
		except:
			logging.error("cannot read config file")
			logging.debug("cannot read config file", exc_info=True)
			# Without config, plugin couldn't work
			return
			
########## User Plugin CODE ##########		
		if typ == "FMS":
			logging.warning("%s not supported", typ)
		elif typ == "ZVEI":
			logging.warning("%s not supported", typ)
		elif typ == "POC":
			logging.warning("%s not supported", typ)
		else:
			logging.warning("Invalid Typ: %s", typ)	
########## User Plugin CODE ##########
		
	except:
		logging.error("unknown error")
		logging.debug("unknown error", exc_info=True)