# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from server.models.status_info import StatusInfo  # noqa: E501
from server.test import BaseTestCase


class TestStatusController(BaseTestCase):
    """StatusController integration test stubs"""

    def test_get_statusnj(self):
        """Test case for get_statusnj

        Get all status at Paterson
        """
        response = self.client.open(
            '/status/nj',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_statusva(self):
        """Test case for get_statusva

        Get all status at Richmond
        """
        response = self.client.open(
            '/status/va',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
