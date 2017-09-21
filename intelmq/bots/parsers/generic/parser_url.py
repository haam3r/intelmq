# -*- coding: utf-8 -*-
"""
Generic URL parser

Parameters:
type: string
"""

import io
import json
import re

from intelmq.lib import utils
from intelmq.lib.bot import ParserBot

class GenericUrlParserBot(ParserBot):

    def process(self):
        report = self.receive_message()

        print("{0}" % report)

        """
        raw_report = utils.base64_decode(report.get("raw"))

        for row in raw_report.splitlines():

            if row.startswith("#") or len(row) == 0 or row == "Site":
                if 'updated' in row:
                    time_str = row[row.find(': ') + 2:]
                    time = dateutil.parser.parse(time_str).isoformat()
                continue

            event = self.new_event(report)

            event.add('classification.type', 'malware')
            event.add('source.fqdn', row.strip())
            event.add('time.source', time)
            event.add("raw", row)

            self.send_message(event)
        self.acknowledge_message()
        """

BOT = GenericUrlParserBot