# -*- coding: iso-8859-15 -*-
import unittest
import base64
from collections import defaultdict
from pyweb.services.message_service import MessageService
from pyweb.models.fileChunk import FileChunk
from pyweb.models.message import Message
from pyweb.fakes.fakeDB import FakeDB

class MessageServiceTests(unittest.TestCase):
    def setUp(self):
        db = FakeDB()
        self.messageService = MessageService(db)

    def test_should_process_message(self):
        expected = defaultdict(str,{u'Respondida:': u'Sim', u'Mensagem:': u'Boa noite, por favor eu quero participar de O Exame Nacional de Revalida\xe7\xe3o de Diplomas M\xe9dicos Expedidos por Institui\xe7\xf5es de Educa\xe7\xe3o Superior Estrangeiras \u2013 REVALIDA 2014, mais n\xe3o posso fazer minha inscri\xe7\xe3o por que no ano passado quis fazer minha inscri\xe7\xe3o pero foi tarde demais e o cadastro que fiz foi com um e-mail que perdi (perdi a conta)e n\xe3o lembro a senha, PORFAVOR COMO POSSO FAZER PARA-ME CADASTRAR NOVAMENTE COM OUTRO E-MAIL, POR FAVOR ME AJUDE, EU QUERO MUITO MESMO PARTICIPAR DA PROVA. eu pe\xe7o sua ajuda e grata antecipadamente pela sua ajuda PORFAVOR.<br />Ou por favor me diga como eu posso falar com voc\xeas.<br />Meu e-mail atual mi_angel_espejo@hotmail.com', u'E-mail do remetente:': u'mi_angel_espejo@hotmail.com', u'Nome do remetente:': u'VIRGINIA CONDORI CHOQUE', u'data de envio:': u'24/06/2014 01:19:33', u'Assunto:': u'Eu quero participar de O Exame Nacional de Revalida\xe7\xe3o de Diplomas M\xe9dicos 2014', u'Mensagem Externa:': u'Sim', u'Tipo:': u'Outro'})
        
        html = """
            <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="pt-br" lang="pt-br">
              <head>
                <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
              </head>

              <body>
                <div style="margin: 10px;">            
                  <label style="font-weight: bold;">Nome do remetente:</label>
                  <span>VIRGINIA CONDORI CHOQUE</span>    
                </div>
                <div style="margin: 10px;">            
                  <label style="font-weight: bold;">E-mail do remetente:</label>
                  <span>mi_angel_espejo@hotmail.com</span>    
                </div>
                <div style="margin: 10px;">            
                  <label style="font-weight: bold;">Assunto:</label>
                  <span>Eu quero participar de O Exame Nacional de Revalidação de Diplomas Médicos 2014</span>    
                </div>
                <div style="margin: 10px;">            
                  <label style="font-weight: bold;">Tipo:</label>
                  <span>Outro</span>
                </div>     
                <div style="margin: 10px;">            
                  <label style="font-weight: bold;">data de envio:</label>
                  <span>24/06/2014 01:19:33</span>    
                </div>
                <div style="margin: 10px;">            
                  <label style="font-weight: bold;">Respondida:</label>
                  <span>Sim</span>
                </div>
                <div style="margin: 10px;">            
                  <label style="font-weight: bold;">Mensagem Externa:</label>
                  <span>Sim</span>
                </div>
                <div style="margin: 10px;">            
                  <label style="font-weight: bold;">Mensagem:</label><br /><br />
                  <div>Boa noite, por favor eu quero participar de O Exame Nacional de Revalidação de Diplomas Médicos Expedidos por Instituições de Educação Superior Estrangeiras – REVALIDA 2014, mais não posso fazer minha inscrição por que no ano passado quis fazer minha inscrição pero foi tarde demais e o cadastro que fiz foi com um e-mail que perdi (perdi a conta)e não lembro a senha, PORFAVOR COMO POSSO FAZER PARA-ME CADASTRAR NOVAMENTE COM OUTRO E-MAIL, POR FAVOR ME AJUDE, EU QUERO MUITO MESMO PARTICIPAR DA PROVA. eu peço sua ajuda e grata antecipadamente pela sua ajuda PORFAVOR.<br/>Ou por favor me diga como eu posso falar com vocês.<br/>Meu e-mail atual mi_angel_espejo@hotmail.com</div>    
                </div>
              </body>
            </html>"""

        actual = self.messageService.parseMessage(html)
        self.assertEqual(actual, expected)

    def test_should_parse_content(self):
        content = """PGh0bWwgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHhtbDpsYW5nPSJwdC1i
ciIKICAgICAgbGFuZz0icHQtYnIiPgoKICAKICA8aGVhZD4KICAgIDxtZXRhIGNvbnRlbnQ9InRl
eHQvaHRtbDtjaGFyc2V0PXV0Zi04IiBodHRwLWVxdWl2PSJDb250ZW50LVR5cGUiPgogIDwvaGVh
ZD4KCiAgPGJvZHk+CiAgICA8ZGl2IHN0eWxlPSJtYXJnaW46IDEwcHg7Ij4gICAgICAgICAgICAK
ICAgICAgPGxhYmVsIHN0eWxlPSJmb250LXdlaWdodDogYm9sZDsiPk5vbWUgZG8gcmVtZXRlbnRl
OjwvbGFiZWw+CiAgICAgIDxzcGFuPlZJUkdJTklBIENPTkRPUkkgQ0hPUVVFPC9zcGFuPiAgICAK
ICAgIDwvZGl2PgogICAgPGRpdiBzdHlsZT0ibWFyZ2luOiAxMHB4OyI+ICAgICAgICAgICAgCiAg
ICAgIDxsYWJlbCBzdHlsZT0iZm9udC13ZWlnaHQ6IGJvbGQ7Ij5FLW1haWwgZG8gcmVtZXRlbnRl
OjwvbGFiZWw+CiAgICAgIDxzcGFuPm1pX2FuZ2VsX2VzcGVqb0Bob3RtYWlsLmNvbTwvc3Bhbj4g
ICAgCiAgICA8L2Rpdj4KICAgIDxkaXYgc3R5bGU9Im1hcmdpbjogMTBweDsiPiAgICAgICAgICAg
IAogICAgICA8bGFiZWwgc3R5bGU9ImZvbnQtd2VpZ2h0OiBib2xkOyI+QXNzdW50bzo8L2xhYmVs
PgogICAgICA8c3Bhbj5FdSBxdWVybyBwYXJ0aWNpcGFyIGRlIE8gRXhhbWUgTmFjaW9uYWwgZGUg
UmV2YWxpZGHDp8OjbyBkZSBEaXBsb21hcyBNw6lkaWNvcyAyMDE0PC9zcGFuPiAgICAKICAgIDwv
ZGl2PgogICAgPGRpdiBzdHlsZT0ibWFyZ2luOiAxMHB4OyI+ICAgICAgICAgICAgCiAgICAgIDxs
YWJlbCBzdHlsZT0iZm9udC13ZWlnaHQ6IGJvbGQ7Ij5UaXBvOjwvbGFiZWw+CiAgICAgIDxzcGFu
Pk91dHJvPC9zcGFuPgogICAgPC9kaXY+ICAgICAKICAgIDxkaXYgc3R5bGU9Im1hcmdpbjogMTBw
eDsiPiAgICAgICAgICAgIAogICAgICA8bGFiZWwgc3R5bGU9ImZvbnQtd2VpZ2h0OiBib2xkOyI+
ZGF0YSBkZSBlbnZpbzo8L2xhYmVsPgogICAgICA8c3Bhbj4yNC8wNi8yMDE0IDAxOjE5OjMzPC9z
cGFuPiAgICAKICAgIDwvZGl2PgogICAgPGRpdiBzdHlsZT0ibWFyZ2luOiAxMHB4OyI+ICAgICAg
ICAgICAgCiAgICAgIDxsYWJlbCBzdHlsZT0iZm9udC13ZWlnaHQ6IGJvbGQ7Ij5SZXNwb25kaWRh
OjwvbGFiZWw+CiAgICAgIDxzcGFuPlNpbTwvc3Bhbj4KICAgIDwvZGl2PgogICAgPGRpdiBzdHls
ZT0ibWFyZ2luOiAxMHB4OyI+ICAgICAgICAgICAgCiAgICAgIDxsYWJlbCBzdHlsZT0iZm9udC13
ZWlnaHQ6IGJvbGQ7Ij5NZW5zYWdlbSBFeHRlcm5hOjwvbGFiZWw+CiAgICAgIDxzcGFuPlNpbTwv
c3Bhbj4KICAgIDwvZGl2PgogICAgPGRpdiBzdHlsZT0ibWFyZ2luOiAxMHB4OyI+ICAgICAgICAg
ICAgCiAgICAgIDxsYWJlbCBzdHlsZT0iZm9udC13ZWlnaHQ6IGJvbGQ7Ij5NZW5zYWdlbTo8L2xh
YmVsPjxiciAvPjxiciAvPgogICAgICA8ZGl2PkJvYSBub2l0ZSwgcG9yIGZhdm9yIGV1IHF1ZXJv
IHBhcnRpY2lwYXIgZGUgTyBFeGFtZSBOYWNpb25hbCBkZSBSZXZhbGlkYcOnw6NvIGRlIERpcGxv
bWFzIE3DqWRpY29zIEV4cGVkaWRvcyBwb3IgSW5zdGl0dWnDp8O1ZXMgZGUgRWR1Y2HDp8OjbyBT
dXBlcmlvciBFc3RyYW5nZWlyYXMg4oCTIFJFVkFMSURBIDIwMTQsIG1haXMgbsOjbyBwb3NzbyBm
YXplciBtaW5oYSBpbnNjcmnDp8OjbyBwb3IgcXVlIG5vIGFubyBwYXNzYWRvIHF1aXMgZmF6ZXIg
bWluaGEgaW5zY3Jpw6fDo28gcGVybyBmb2kgdGFyZGUgZGVtYWlzIGUgbyBjYWRhc3RybyBxdWUg
Zml6IGZvaSBjb20gdW0gZS1tYWlsIHF1ZSBwZXJkaSAocGVyZGkgYSBjb250YSllIG7Do28gbGVt
YnJvIGEgc2VuaGEsIFBPUkZBVk9SIENPTU8gUE9TU08gRkFaRVIgUEFSQS1NRSBDQURBU1RSQVIg
Tk9WQU1FTlRFIENPTSBPVVRSTyBFLU1BSUwsIFBPUiBGQVZPUiBNRSBBSlVERSwgRVUgUVVFUk8g
TVVJVE8gTUVTTU8gUEFSVElDSVBBUiBEQSBQUk9WQS4gZXUgcGXDp28gc3VhIGFqdWRhIGUgZ3Jh
dGEgYW50ZWNpcGFkYW1lbnRlIHBlbGEgc3VhIGFqdWRhIFBPUkZBVk9SLjxici8+T3UgcG9yIGZh
dm9yIG1lIGRpZ2EgY29tbyBldSBwb3NzbyBmYWxhciBjb20gdm9jw6pzLjxici8+TWV1IGUtbWFp
bCBhdHVhbCBtaV9hbmdlbF9lc3Blam9AaG90bWFpbC5jb208L2Rpdj4gICAgCiAgICA8L2Rpdj4K
ICA8L2JvZHk+CjwvaHRtbD4K"""
        expected = """boa noite por favor eu quero participar de o exame nacional de revalidao de diplomas mdicos expedidos por instituies de educao superior estrangeiras  revalida 2014 mais no posso fazer minha inscrio por que no ano passado quis fazer minha inscrio pero foi tarde demais e o cadastro que fiz foi com um e-mail que perdi (perdi a conta)e no lembro a senha porfavor como posso fazer para-me cadastrar novamente com outro e-mail por favor me ajude eu quero muito mesmo participar da prova. eu peo sua ajuda e grata antecipadamente pela sua ajuda porfavor.<br />ou por favor me diga como eu posso falar com vocs.<br />meu e-mail atual mi_angel_espejo@hotmail.com"""

        contentDict = self.messageService.parseMessage(base64.b64decode(content))

        actual = self.messageService.parseContent(contentDict)
        self.assertEqual(actual, expected)

    def test_should_parse_subject(self):
        content = """PGh0bWwgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHhtbDpsYW5nPSJwdC1i
ciIKICAgICAgbGFuZz0icHQtYnIiPgoKICAKICA8aGVhZD4KICAgIDxtZXRhIGNvbnRlbnQ9InRl
eHQvaHRtbDtjaGFyc2V0PXV0Zi04IiBodHRwLWVxdWl2PSJDb250ZW50LVR5cGUiPgogIDwvaGVh
ZD4KCiAgPGJvZHk+CiAgICA8ZGl2IHN0eWxlPSJtYXJnaW46IDEwcHg7Ij4gICAgICAgICAgICAK
ICAgICAgPGxhYmVsIHN0eWxlPSJmb250LXdlaWdodDogYm9sZDsiPk5vbWUgZG8gcmVtZXRlbnRl
OjwvbGFiZWw+CiAgICAgIDxzcGFuPlZJUkdJTklBIENPTkRPUkkgQ0hPUVVFPC9zcGFuPiAgICAK
ICAgIDwvZGl2PgogICAgPGRpdiBzdHlsZT0ibWFyZ2luOiAxMHB4OyI+ICAgICAgICAgICAgCiAg
ICAgIDxsYWJlbCBzdHlsZT0iZm9udC13ZWlnaHQ6IGJvbGQ7Ij5FLW1haWwgZG8gcmVtZXRlbnRl
OjwvbGFiZWw+CiAgICAgIDxzcGFuPm1pX2FuZ2VsX2VzcGVqb0Bob3RtYWlsLmNvbTwvc3Bhbj4g
ICAgCiAgICA8L2Rpdj4KICAgIDxkaXYgc3R5bGU9Im1hcmdpbjogMTBweDsiPiAgICAgICAgICAg
IAogICAgICA8bGFiZWwgc3R5bGU9ImZvbnQtd2VpZ2h0OiBib2xkOyI+QXNzdW50bzo8L2xhYmVs
PgogICAgICA8c3Bhbj5FdSBxdWVybyBwYXJ0aWNpcGFyIGRlIE8gRXhhbWUgTmFjaW9uYWwgZGUg
UmV2YWxpZGHDp8OjbyBkZSBEaXBsb21hcyBNw6lkaWNvcyAyMDE0PC9zcGFuPiAgICAKICAgIDwv
ZGl2PgogICAgPGRpdiBzdHlsZT0ibWFyZ2luOiAxMHB4OyI+ICAgICAgICAgICAgCiAgICAgIDxs
YWJlbCBzdHlsZT0iZm9udC13ZWlnaHQ6IGJvbGQ7Ij5UaXBvOjwvbGFiZWw+CiAgICAgIDxzcGFu
Pk91dHJvPC9zcGFuPgogICAgPC9kaXY+ICAgICAKICAgIDxkaXYgc3R5bGU9Im1hcmdpbjogMTBw
eDsiPiAgICAgICAgICAgIAogICAgICA8bGFiZWwgc3R5bGU9ImZvbnQtd2VpZ2h0OiBib2xkOyI+
ZGF0YSBkZSBlbnZpbzo8L2xhYmVsPgogICAgICA8c3Bhbj4yNC8wNi8yMDE0IDAxOjE5OjMzPC9z
cGFuPiAgICAKICAgIDwvZGl2PgogICAgPGRpdiBzdHlsZT0ibWFyZ2luOiAxMHB4OyI+ICAgICAg
ICAgICAgCiAgICAgIDxsYWJlbCBzdHlsZT0iZm9udC13ZWlnaHQ6IGJvbGQ7Ij5SZXNwb25kaWRh
OjwvbGFiZWw+CiAgICAgIDxzcGFuPlNpbTwvc3Bhbj4KICAgIDwvZGl2PgogICAgPGRpdiBzdHls
ZT0ibWFyZ2luOiAxMHB4OyI+ICAgICAgICAgICAgCiAgICAgIDxsYWJlbCBzdHlsZT0iZm9udC13
ZWlnaHQ6IGJvbGQ7Ij5NZW5zYWdlbSBFeHRlcm5hOjwvbGFiZWw+CiAgICAgIDxzcGFuPlNpbTwv
c3Bhbj4KICAgIDwvZGl2PgogICAgPGRpdiBzdHlsZT0ibWFyZ2luOiAxMHB4OyI+ICAgICAgICAg
ICAgCiAgICAgIDxsYWJlbCBzdHlsZT0iZm9udC13ZWlnaHQ6IGJvbGQ7Ij5NZW5zYWdlbTo8L2xh
YmVsPjxiciAvPjxiciAvPgogICAgICA8ZGl2PkJvYSBub2l0ZSwgcG9yIGZhdm9yIGV1IHF1ZXJv
IHBhcnRpY2lwYXIgZGUgTyBFeGFtZSBOYWNpb25hbCBkZSBSZXZhbGlkYcOnw6NvIGRlIERpcGxv
bWFzIE3DqWRpY29zIEV4cGVkaWRvcyBwb3IgSW5zdGl0dWnDp8O1ZXMgZGUgRWR1Y2HDp8OjbyBT
dXBlcmlvciBFc3RyYW5nZWlyYXMg4oCTIFJFVkFMSURBIDIwMTQsIG1haXMgbsOjbyBwb3NzbyBm
YXplciBtaW5oYSBpbnNjcmnDp8OjbyBwb3IgcXVlIG5vIGFubyBwYXNzYWRvIHF1aXMgZmF6ZXIg
bWluaGEgaW5zY3Jpw6fDo28gcGVybyBmb2kgdGFyZGUgZGVtYWlzIGUgbyBjYWRhc3RybyBxdWUg
Zml6IGZvaSBjb20gdW0gZS1tYWlsIHF1ZSBwZXJkaSAocGVyZGkgYSBjb250YSllIG7Do28gbGVt
YnJvIGEgc2VuaGEsIFBPUkZBVk9SIENPTU8gUE9TU08gRkFaRVIgUEFSQS1NRSBDQURBU1RSQVIg
Tk9WQU1FTlRFIENPTSBPVVRSTyBFLU1BSUwsIFBPUiBGQVZPUiBNRSBBSlVERSwgRVUgUVVFUk8g
TVVJVE8gTUVTTU8gUEFSVElDSVBBUiBEQSBQUk9WQS4gZXUgcGXDp28gc3VhIGFqdWRhIGUgZ3Jh
dGEgYW50ZWNpcGFkYW1lbnRlIHBlbGEgc3VhIGFqdWRhIFBPUkZBVk9SLjxici8+T3UgcG9yIGZh
dm9yIG1lIGRpZ2EgY29tbyBldSBwb3NzbyBmYWxhciBjb20gdm9jw6pzLjxici8+TWV1IGUtbWFp
bCBhdHVhbCBtaV9hbmdlbF9lc3Blam9AaG90bWFpbC5jb208L2Rpdj4gICAgCiAgICA8L2Rpdj4K
ICA8L2JvZHk+CjwvaHRtbD4K"""
        expected = """boa noite por favor eu quero participar de o exame nacional de revalidao de diplomas mdicos expedidos por instituies de educao superior estrangeiras  revalida 2014 mais no posso fazer minha inscrio por que no ano passado quis fazer minha inscrio pero foi tarde demais e o cadastro que fiz foi com um e-mail que perdi (perdi a conta)e no lembro a senha porfavor como posso fazer para-me cadastrar novamente com outro e-mail por favor me ajude eu quero muito mesmo participar da prova. eu peo sua ajuda e grata antecipadamente pela sua ajuda porfavor.<br />ou por favor me diga como eu posso falar com vocs.<br />meu e-mail atual mi_angel_espejo@hotmail.com"""

        contentDict = self.messageService.parseMessage(base64.b64decode(content))

        actual = self.messageService.parseContent(contentDict)
        self.assertEqual(actual, expected)        

    def test_should_parse_file_chunks(self):
        firstChunkData = """From nobody Fri 02 13 21:48:52 2015
Return-Path: <dcwravazzi@gmail.com>
Received: from lmtpproxyd ([161.148.28.133])
     by corp-bsa-exp-backimap28 (Cyrus v2.4.9-Debian-2.4.9-1) with LMTPA;
     Thu, 04 Sep 2014 15:01:15 -0300
X-Sieve: CMU Sieve 2.4
Received: from corp-bsa-exp-feimapv2-04.localdomain (localhost [127.0.0.1])
     by corp-bsa-exp-feimapv2-04 with LMTPA;
     Thu, 04 Sep 2014 15:01:15 -0300
Received: from mail-apl.serpro.gov.br (corp-bsa-exp-balancer-28-81 [161.148.28.81])
    by corp-bsa-exp-feimapv2-04.localdomain (Postfix) with ESMTP id 28009811B0
    for <servicos@mail.planejamento.gov.br>; Thu,  4 Sep 2014 15:01:15 -0300 (BRT)
Received: from pps.filterd (mail-apl2.serpro.gov.br [127.0.0.1])
    by mail-apl2.serpro.gov.br (8.14.5/8.14.5) with SMTP id s84I0cqY002856
    for <servicos@planejamento.gov.br>; Thu, 4 Sep 2014 15:01:15 -0300
Received: from dfcdsrvv1270.localhost ([161.148.175.63])
    by mail-apl2.serpro.gov.br with ESMTP id 1p2qwqrf20-1
    for <servicos@planejamento.gov.br>; Thu, 04 Sep 2014 15:01:14 -0300"""
        
        secondChunkData = """Content-Type: text/html; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64
To: servicos@planejamento.gov.br
From: dcwravazzi@gmail.com
Subject: =?utf-8?b?W2V4cG9ydGHDp8OjbyBkbyBHdWlhIGRlIFNlcnZpw6dvc10gODk0NjogImNh?=
    =?utf-8?q?ncelamento_de_conta=22_recebida_em_2014/07/18_11=3A39=3A05=2E00?=
    =?utf-8?q?8_GMT-3?=
Date: Thu, 04 Sep 2014 15:01:12 -0300
X-Mailer: Zope/SecureMailHost
Message-Id: <20140904180112.3482.60060.dfcdsrvv1270.localhost@dfcdsrvv1270.localhost>
X-Proofpoint-Spam-Details: rule=notspam policy=default score=0 spamscore=0 suspectscore=3 phishscore=0
 adultscore=0 bulkscore=0 classifier=spam adjust=0 reason=mlx scancount=1
 engine=7.0.1-1402240000 definitions=main-1409040162
X-Proofpoint-Virus-Version: vendor=fsecure engine=2.50.10432:5.12.52,1.0.27,0.0.0000
 definitions=2014-09-04_03:2014-09-04,2014-09-04,1970-01-01 signatures=0

PGh0bWwgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHhtbDpsYW5nPSJwdC1i
ciIKICAgICAgbGFuZz0icHQtYnIiPgoKICAKICA8aGVhZD4KICAgIDxtZXRhIGNvbnRlbnQ9InRl
eHQvaHRtbDtjaGFyc2V0PXV0Zi04IiBodHRwLWVxdWl2PSJDb250ZW50LVR5cGUiPgogIDwvaGVh
ZD4KCiAgPGJvZHk+CiAgICA8ZGl2IHN0eWxlPSJtYXJnaW46IDEwcHg7Ij4gICAgICAgICAgICAK
ICAgICAgPGxhYmVsIHN0eWxlPSJmb250LXdlaWdodDogYm9sZDsiPk5vbWUgZG8gcmVtZXRlbnRl
OjwvbGFiZWw+CiAgICAgIDxzcGFuPkTDqWxjZXJvIENlc2FyIFdvbGYgUmF2YXp6aTwvc3Bhbj4g
ICAgCiAgICA8L2Rpdj4KICAgIDxkaXYgc3R5bGU9Im1hcmdpbjogMTBweDsiPiAgICAgICAgICAg
IAogICAgICA8bGFiZWwgc3R5bGU9ImZvbnQtd2VpZ2h0OiBib2xkOyI+RS1tYWlsIGRvIHJlbWV0
ZW50ZTo8L2xhYmVsPgogICAgICA8c3Bhbj5kY3dyYXZhenppQGdtYWlsLmNvbTwvc3Bhbj4gICAg
CiAgICA8L2Rpdj4KICAgIDxkaXYgc3R5bGU9Im1hcmdpbjogMTBweDsiPiAgICAgICAgICAgIAog"""
        
        thirdChunkData = """ICAgICA8bGFiZWwgc3R5bGU9ImZvbnQtd2VpZ2h0OiBib2xkOyI+QXNzdW50bzo8L2xhYmVsPgog
ICAgICA8c3Bhbj5jYW5jZWxhbWVudG8gZGUgY29udGE8L3NwYW4+ICAgIAogICAgPC9kaXY+CiAg
ICA8ZGl2IHN0eWxlPSJtYXJnaW46IDEwcHg7Ij4gICAgICAgICAgICAKICAgICAgPGxhYmVsIHN0
eWxlPSJmb250LXdlaWdodDogYm9sZDsiPlRpcG86PC9sYWJlbD4KICAgICAgPHNwYW4+T3V0cm88
L3NwYW4+CiAgICA8L2Rpdj4gICAgIAogICAgPGRpdiBzdHlsZT0ibWFyZ2luOiAxMHB4OyI+ICAg
ICAgICAgICAgCiAgICAgIDxsYWJlbCBzdHlsZT0iZm9udC13ZWlnaHQ6IGJvbGQ7Ij5kYXRhIGRl
IGVudmlvOjwvbGFiZWw+CiAgICAgIDxzcGFuPjE4LzA3LzIwMTQgMTE6Mzk6MDM8L3NwYW4+ICAg
IAogICAgPC9kaXY+CiAgICA8ZGl2IHN0eWxlPSJtYXJnaW46IDEwcHg7Ij4gICAgICAgICAgICAK
ICAgICAgPGxhYmVsIHN0eWxlPSJmb250LXdlaWdodDogYm9sZDsiPlJlc3BvbmRpZGE6PC9sYWJl
bD4KICAgICAgPHNwYW4+U2ltPC9zcGFuPgogICAgPC9kaXY+CiAgICA8ZGl2IHN0eWxlPSJtYXJn
aW46IDEwcHg7Ij4gICAgICAgICAgICAKICAgICAgPGxhYmVsIHN0eWxlPSJmb250LXdlaWdodDog
Ym9sZDsiPk1lbnNhZ2VtIEV4dGVybmE6PC9sYWJlbD4KICAgICAgPHNwYW4+U2ltPC9zcGFuPgog
ICAgPC9kaXY+CiAgICA8ZGl2IHN0eWxlPSJtYXJnaW46IDEwcHg7Ij4gICAgICAgICAgICAKICAg
ICAgPGxhYmVsIHN0eWxlPSJmb250LXdlaWdodDogYm9sZDsiPk1lbnNhZ2VtOjwvbGFiZWw+PGJy
IC8+PGJyIC8+CiAgICAgIDxkaXY+Qm9tIGRpYSwgdHJhYmFsaG8gbmEgRGVmZXNhIENpdmlsIGRl
IFPDo28gSm9zw6kgZG8gUmlvIFByZXRvIC8gU1AgZSwgcGVzcXVpc2FuZG8gc29icmUgbyBTSUdB
UCwgYWNlc3NlaSBvIGxpbmsgaHR0cDovL3NpZ2FwLmluZXAuZ292LmJyL3NpZ2FwLzxici8+cGFy
YSBtZSBjYWRhc3RyYXIuIEVmZXR1YWRvIG8gY2FkYXN0cmFtZW50byBlIHRlbnRhbmRvIGFjZXNz
YXIgbyBtZXNtbyBsaW5rLCByZWNlYmkgYSBtZW5zYWdlbSBkZSBxdWUgbsOjbyBoYXZpYSBkYWRv
cyBwYXJhIGFjZXNzYXIgbyBTSUdBUCBlIHRlbnRlaSBmYXplciBvIGNhbmNlbGFtZW50byBkbyBt
ZXUgY2FkYXN0cm8gc2VtIHN1Y2Vzc28uIENvbW8gZmHDp28gcGFyYSBjYW5jZWxhciBtZXVzIGRh
ZG9zPzxici8+PGJyLz5BdHQsPC9kaXY+ICAgIAogICAgPC9kaXY+CiAgPC9ib2R5Pgo8L2h0bWw+
Cg==
"""
        chunks = [FileChunk("02a3aa53-3220-48a1-81c0-c3f5f807b681", 1, "jp", thirdChunkData, 3),FileChunk("3ba192de-8139-4d66-9c89-e47be1274fc5", 1, "jp", firstChunkData, 1),FileChunk("22e625e2-9b0d-42b2-a91e-ab41c9bc1706", 1, "jp", secondChunkData, 2)]

        messageOriginalContent = """bom dia trabalho na defesa civil de so jos do rio preto / sp e pesquisando sobre o sigap acessei o link http://sigap.inep.gov.br/sigap/<br />para me cadastrar. efetuado o cadastramento e tentando acessar o mesmo link recebi a mensagem de que no havia dados para acessar o sigap e tentei fazer o cancelamento do meu cadastro sem sucesso. como fao para cancelar meus dados?<br /><br />att"""

        messageContent = """bom dia trabalho na defesa civil de so jos do rio preto / sp e pesquisando sobre o sigap acessei o link http://sigap.inep.gov.br/sigap/<br />para me cadastrar. efetuado o cadastramento e tentando acessar o mesmo link recebi a mensagem de que no havia dados para acessar o sigap e tentei fazer o cancelamento do meu cadastro sem sucesso. como fao para cancelar meus dados?<br /><br />att"""

        expected = [Message("b5d9422a-faf6-4534-b3ed-0d5265e8e9f8", 1, messageOriginalContent, messageContent, "subject", "sender", "to", "user")]

        actual = self.messageService.parseFileChunks(chunks)

        self.assertEqual(actual[0].content, expected[0].content)





if __name__ == '__main__':
    unittest.main()