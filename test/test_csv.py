import unittest
from in_n_out import in_n_out_app


class TestCsvFile(unittest.TestCase):
    def setUp(self):
        self.input_data = [['Name', ' Surname', ' Age'], ['Joe', ' Soap', ' 25'], ['Jane', ' Doe', ' 45'],
                           ['John', ' Smith', ' 80']]
        self.class_holder = in_n_out_app.CsvCreator()

# test if the list created holds the correct information
    def test_parsed_correct_info(self):
        csv_list_create = self.class_holder.parse_in_content(self.input_data)
        self.assertEqual(csv_list_create[0], ['Name', ' Surname', ' Age', ' Parsed'])


if __name__ == '__main__':
    unittest.main()

