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
Unit tests for data utils.
"""

import tempfile

import unittest

from texar.tf.data import data_utils


class CountFileLinesTest(unittest.TestCase):
    """Tests :func:`texar.tf.data.data_utils.count_file_lines`.
    """

    def test_load_glove(self):
        """Tests the load_glove function.
        """
        file_1 = tempfile.NamedTemporaryFile(mode="w+")
        num_lines = data_utils.count_file_lines(file_1.name)
        self.assertEqual(num_lines, 0)

        file_2 = tempfile.NamedTemporaryFile(mode="w+")
        file_2.write('\n'.join(['x'] * 5))
        file_2.flush()
        num_lines = data_utils.count_file_lines(
            [file_1.name, file_2.name, file_2.name])
        self.assertEqual(num_lines, 0 + 5 + 5)


if __name__ == "__main__":
    unittest.main()
