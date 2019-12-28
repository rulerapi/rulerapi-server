# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestGetRuleListController(BaseTestCase):
    """GetRuleListController integration test stubs"""

    def test_get_rules(self):
        """Test case for get_rules

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/rules',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
