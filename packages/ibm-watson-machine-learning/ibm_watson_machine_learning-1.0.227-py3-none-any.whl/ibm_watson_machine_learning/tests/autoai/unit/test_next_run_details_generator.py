#  (C) Copyright IBM Corp. 2021.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import unittest

from ibm_watson_machine_learning import APIClient
from ibm_watson_machine_learning.utils.autoai.utils import NextRunDetailsGenerator
from ibm_watson_machine_learning.tests.utils import get_wml_credentials


class TestNextRunDetailsGenerator(unittest.TestCase):
    wml_credentials_cp4d = None
    client = None
    project_id = 'dd829201-9d59-4f5a-b0e0-6ea3a88ae66b'
    generator = None
    data = []

    @classmethod
    def setUp(cls) -> None:
        cls.wml_credentials_cp4d = get_wml_credentials('CLOUD_DEV_AM')
        cls.client = APIClient(cls.wml_credentials_cp4d, cls.project_id)
        cls.client.set.default_project(cls.project_id)

    def test_01__initialize_generator_class(self):
        details = self.client.training.get_details(limit=1)
        self.data.extend(details['resources'])
        TestNextRunDetailsGenerator.generator = NextRunDetailsGenerator(wml_client=self.client,
                                                                        href=details['next']['href'])

        self.assertIsInstance(self.generator.wml_client, APIClient, msg="wml client not set")
        self.assertEqual(self.generator.href, details['next']['href'], msg="href is incorrect")

    def test_02__generate_next_run_details(self):
        for entry in self.generator:
            self.data.extend(entry)
        self.assertGreater(1, len(self.data), msg="There is only one or 0 runs, or generator works in incorrect way.")


if __name__ == '__main__':
    unittest.main()
