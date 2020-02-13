# Copyright 2020 The Texar Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Unit tests for utility functions.
"""

import unittest

from texar.tf.utils import utils


class UtilsTest(unittest.TestCase):
    """Tests utility functions.
    """
    def test_uniquify_str(self):
        """Tests :func:`texar.tf.utils.uniquify_str`.
        """

        str_set = ['str']
        unique_str = utils.uniquify_str('str', str_set)
        self.assertEqual(unique_str, 'str_1')

        str_set.append('str_1')
        str_set.append('str_2')
        unique_str = utils.uniquify_str('str', str_set)
        self.assertEqual(unique_str, 'str_3')

    def test_truncate_seq_pair(self):

        tokens_a = [1, 2, 3]
        tokens_b = [4, 5, 6]
        utils.truncate_seq_pair(tokens_a, tokens_b, 4)
        self.assertListEqual(tokens_a, [1, 2])
        self.assertListEqual(tokens_b, [4, 5])

        tokens_a = [1]
        tokens_b = [2, 3, 4, 5]
        utils.truncate_seq_pair(tokens_a, tokens_b, 3)
        self.assertListEqual(tokens_a, [1])
        self.assertListEqual(tokens_b, [2, 3])


if __name__ == "__main__":
    unittest.main()
