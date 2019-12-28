# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestGetRuleController(BaseTestCase):
    """GetRuleController integration test stubs"""

    def test_get_rule(self):
        """Test case for get_rule

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/rule/{rule_id}'.format(rule_id='rule_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
