from django.test import TestCase
from sim.spec_factory import Parser


class ParserTest(TestCase):

    def test_parser_can_parse_template(self):
        parser = Parser()
        template = '-c #{first} -#{second} #{123third}'
        parser.parse_template(template)
        names = parser.getnames()
        buff = parser.getbuff()
        self.assertEqual(len(names), 3, msg="Incorrect number of names")
        self.assertEqual(names, ['first', 'second', '123third'], msg="Incorrect names, they are: " + ' '.join(names))
