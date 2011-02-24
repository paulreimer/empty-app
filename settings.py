import copy
import logging

default_settings = {
  'debug':             False,
	'MEDIA_URL':         '/',
	}

production = copy.deepcopy(default_settings)
production.update({
	})

testing = copy.deepcopy(default_settings)
testing.update({
	})

dev = copy.deepcopy(default_settings)
dev.update({
  'debug': True,
	})

settings = dev

