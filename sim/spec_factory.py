import htcondor
import re


class Parser:

    __template_buff = []
    __names = []

    def parse_template(self, template):
        regex_name = r'#{\w*}'
        self.__template_buff = re.split(regex_name, template)
        self.__names = re.findall(regex_name, template)
        for i in range(len(self.__names)):
            self.__names[i] = self.__names[i].replace('#{', '')
            self.__names[i] = self.__names[i].replace('}', '')

    def getnames(self):
        return self.__names

    def getbuff(self):
        return self.__template_buff



