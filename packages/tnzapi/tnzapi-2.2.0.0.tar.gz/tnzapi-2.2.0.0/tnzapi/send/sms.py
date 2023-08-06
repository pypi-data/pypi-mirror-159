import requests
import json
import asyncio

from tnzapi.send._common import Common
from tnzapi.base import MessageResult

class SMS(Common):
    
    FromNumber          = ""
    SMSEmailReply       = ""
    CharacterConversion	= False
    MessageText         = ""

    """ Constructor """
    def __init__(self, kwargs):
        
        super().__init__(kwargs)

        self.SetArgsChild(kwargs)

    """ Destructor """
    def __del__(self):
        self.FromNumber             = ""
        self.SMSEmailReply          = ""
        self.CharacterConversion    = False
        self.MessageText            = ""

    """ Update Data """
    def SetArgsChild(self, kwargs):

        #print("sms().SetArgs()")

        for key, value in kwargs.items():

            if key == "FromNumber":
                self.FromNumber = value

            if key == "SMSEmailReply":
                self.SMSEmailReply = value

            if key == "CharacterConversion":
                self.CharacterConversion = value
            
            if key == "MessageText":
                self.MessageText = value

    """ API Data """
    @property
    def APIMessageData(self):
        return {
            "Mode": self.SendMode,
            "MessageID" : self.MessageID,

            "ErrorEmailNotify": self.ErrorEmailNotify,
            "WebhookCallbackURL": self.WebhookCallbackURL,
            "WebhookCallbackFormat": self.WebhookCallbackFormat,

            "Reference": self.Reference,
            "SendTime": self.SendTime,
            "TimeZone": self.Timezone,
            "SubAccount": self.SubAccount,
            "Department": self.Department,
            "ChargeCode": self.ChargeCode,
            "FromNumber": self.FromNumber,
            "SMSEmailReply": self.SMSEmailReply,
            "CharacterConversion": self.CharacterConversion,
            "Message": self.MessageText,
            "Destinations" : self.Recipients,
            "Files": self.Attachments
        }

    @property
    def APIDataWithSender(self):
        return {
            "Sender": self.Sender,
            "APIKey": self.APIKey,
            "MessageData" : self.APIMessageData
        }

    @property
    def APIDataWithAuthToken(self):
        return {
            "MessageData" : self.APIMessageData
        }

    @property
    def APIData(self):
        if self.AuthToken :
            return self.APIDataWithAuthToken
        return self.APIDataWithSender

    """ Private function to POST message to TNZ REST API """
    def __PostMessage(self):
        
        try:
            r = requests.post(self.APIURL+"/send/sms", data=json.dumps(self.APIData), headers=self.APIHeaders)
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return MessageResult(response=r)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            return MessageResult(error=str(e))
            
        return MessageResult(response=r)

    """ Private async function to POST message to TNZ REST API """
    async def __PostMessageAsync(self):

        return self.__PostMessage()

    """ Function to send message """

    """
    def SendMessage(self, **kwargs):
        super().SetArgsCommon(kwargs)
        self.SetArgsSMS(kwargs)
        ...
    """
    
    def SendMessage(self, **kwargs):

        if kwargs != None and len(kwargs) > 0:
            self.__init__(kwargs)

        if not self.AuthToken :

            if not self.Sender :
                return MessageResult(error="Missing AuthToken")
            
            if not self.APIKey :
                return MessageResult(error="Missing AuthToken")

        if self.WebhookCallbackURL :

            if not self.WebhookCallbackFormat :
                return MessageResult(error="Missing WebhookCallbackFormat - JSON or XML")

            if self.WebhookCallbackFormat.upper() != "JSON" and self.WebhookCallbackFormat.upper() != "XML" :
                return MessageResult(error="Invalid WebhookCallbackFormat - JSON or XML")
        
        if not self.MessageText:
            return MessageResult(error="Emtpy Message Text")

        if not self.Recipients:
            return MessageResult(error="Empty recipient(s)")

        return self.__PostMessage()

    """ Async Function to send message """
    async def SendMessageAsync(self, **kwargs):

        if kwargs != None and len(kwargs) > 0:
            self.__init__(kwargs)

        if not self.AuthToken:

            if not self.Sender :
                return MessageResult(error="Missing AuthToken")
            
            if not self.APIKey :
                return MessageResult(error="Missing AuthToken")

        if self.WebhookCallbackURL :

            if not self.WebhookCallbackFormat :
                return MessageResult(error="Missing WebhookCallbackFormat - JSON or XML")

            if self.WebhookCallbackFormat.upper() != "JSON" and self.WebhookCallbackFormat.upper() != "XML" :
                return MessageResult(error="Invalid WebhookCallbackFormat - JSON or XML")
        
        if not self.MessageText:
            return MessageResult(error="Emtpy Message Text")

        if not self.Recipients:
            return MessageResult(error="Empty recipient(s)")

        return await asyncio.create_task(self.__PostMessageAsync())

    def __repr__(self):
        return self.__pretty__(self.APIData)

    def __str__(self):
        if self.AuthToken:
            return 'SMS(AuthToken='+self.AuthToken+')'
        
        return 'SMS(Sender='+self.Sender+', APIKey='+str(self.APIKey)+ ')'