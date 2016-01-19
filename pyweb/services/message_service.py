from ..models.message import Message
import uuid
import base64
import operator
import unicodedata
from collections import defaultdict
from pattern import web
import numpy as np
from sklearn import svm
import random as random

class MessageService():
	db = None

	def __init__(self, database):
		self.db = database

	def load_messages_by_login(self, login):
		collection = self.db.Messages.find({'user': login})
		if collection.count() > 0:
			document = collection[0]
			user = Message(document['id'])
			user.first_name = document['first_name']
			user.last_name = document['last_name']
			user.email = document['email']
			user.password = document['password']
			return user
		else:
			return User('')

	def create(self, message):
		json_data = message.to_json()
		self.db.Messages.insert(json_data)

	def parseFileChunks(self, fileChunks):
		messages = []
		position = 0
		fileChunks.sort()

		processingContent = False
		content = ""
		for chunk in fileChunks:
			lines = chunk.data.splitlines()			
			for line in lines:
				if line.strip() == "":
					if processingContent:						
						messageContent = self.parseContent(content)
						message = Message(str(uuid.uuid1()), chunk.fileId, messageContent, "subject", "sender", "to", "user")
						messages.append(message)

					content = ""
					processingContent = not processingContent
				if processingContent:
					content += line		

		return messages

	def parseMessage(self, html):
		dom = web.Element(html)
		divs = dom('div')
		result = defaultdict(str)
	    
		email = [{div('label')[0].content: div('span')[0].content} for div in divs if len(div('label')) > 0 and len(div('span')) > 0]
		subject = [{div('label')[0].content: div('div')[0].content} for div in divs if len(div('div')) > 0]

		[email.append(s) for s in subject]

		for field in email:      
			for k,v in field.iteritems():
				result[k] = v

		return result

	def parseContent(self, message):
		result = ""
		try:
			result = self.parseMessage(base64.b64decode(message))[u'Mensagem:'].replace(',','').lower().strip().encode('ascii','ignore')
		except:
			pass
		return result

