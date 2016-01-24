from ..models.message import Message
import uuid
import base64
import operator
import unicodedata
from collections import defaultdict
from pattern import web
import random as random

class MessageService():
	db = None

	def __init__(self, database):
		self.db = database

	def getMessagesByUser(self, user, start, count):
		messages = []
		collection = self.db.Messages.find({'user': user}).skip(start).limit(count)
		for document in collection:
			message = Message(document['_id'], document['fileId'], document['originalContent'], document['content'], document['subject'], document['sender'], document['date'], document['user'])
			messages.append(message)
		return messages		

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
				if line.strip() == "" or (lines.index(line) == len(lines) - 1 and fileChunks.index(chunk) == len(fileChunks) - 1):
					if line.strip() != "":
						content += line
					if processingContent:
						messageOriginalContent = self.parseOriginalContent(content)
						messageContent = self.parseContent(content)
						messageSubject = self.parseSubject(content)
						messageSender = self.parseSender(content)
						messageDate = self.parseDate(content)
						message = Message(str(uuid.uuid1()), chunk.fileId, messageOriginalContent, messageContent, messageSubject, messageSender, messageDate, chunk.user)
						messages.append(message)

					content = ""
					processingContent = not processingContent
				if processingContent:
					content += line		

		for message in messages:
			self.create(message)
			
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

	def parseOriginalContent(self, message):
		result = ""
		try:
			result = self.parseMessage(base64.b64decode(message))[u'Mensagem:'].encode('ascii','ignore')
		except:
			pass
		return result

	def parseContent(self, message):
		result = ""
		try:
			result = self.parseMessage(base64.b64decode(message))[u'Mensagem:'].replace(',','').lower().strip().encode('ascii','ignore')
		except:
			pass
		return result

	def parseSubject(self, message):
		result = ""
		try:
			result = self.parseMessage(base64.b64decode(message))[u'Assunto:'].lower().strip().encode('ascii','ignore')
		except:
			pass
		return result

	def parseSender(self, message):
		result = ""
		try:
			result = self.parseMessage(base64.b64decode(message))[u'E-mail do remetente:'].lower().strip().encode('ascii','ignore')
		except:
			pass
		return result

	def parseDate(self, message):
		result = ""
		try:
			result = self.parseMessage(base64.b64decode(message))[u'data de envio:'].strip().encode('ascii','ignore')
		except:
			pass
		return result

