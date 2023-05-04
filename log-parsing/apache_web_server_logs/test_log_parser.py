import unittest
from log_parser import parse_log

class TestLogParser(unittest.TestCase):
    def test_parse_log(self):
        # create a sample log file
        log_file = 'sample_log.txt'
        with open(log_file, 'w') as f:
            f.write('192.168.0.1 - - [01/Jan/2023:12:00:00 -0800] "GET /index.html HTTP/1.1" 200 2326\n')

        # define the expected output
        expected_output = [{'ip': '192.168.0.1', 'timestamp': '01/Jan/2023:12:00:00 -0800'}]

        # parse the log file
        result = parse_log(log_file)

        # assert that the result is equal to the expected output
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
