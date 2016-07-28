# -*- coding: utf-8 -*-


class Command(object):
    def __init__(self, language, command_str, response):
        """
        Command object.
        :param language: language set. eg. zh_TW
        :param command_str: string to trigger command. eg. help
        :param response: list of response content. eg. ['hi', 'hello']
        """
        self.command_str = command_str
        self.language = language
        self.response = response


class NlpAction(object):
    def __init__(self, language, action_str, responses):
        """
        Command object.
        :param language: language set. eg. zh_TW
        :param command_str: string to trigger command. eg. help
        :param response: list of response content. eg. ['hi', 'hello']
        """
        self.action_str = action_str
        self.language = language
        self.response = responses


class NLPActions(object):
    Welcome = 'WELCOME'
    Location = 'LOCATION'
    EventTime = 'EVENTTIME'
    Error = 'ERROR'
