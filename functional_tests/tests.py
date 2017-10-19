from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from os import getcwd


class SubmitSimulationTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_simulation(self):
        # User enters site and selects "Start Simulation"
        self.browser.get(self.live_server_url + '/sim/')

        # User uploads executable file

        exec_upload = self.browser.find_element_by_id("id_exec")
        exec_upload.send_keys(getcwd() + "/test")

        # User enters argument template

        argtemplate = self.browser.find_element_by_id("id_argtemplate")
        argtemplate.send_keys("#{first} -c -#{second} #{files}")

        # User specifies first arg element
        # First, by selecting the type of arg and choosing Range

        arg_table = self.browser.find_element_by_id("id_value_forms")
        type_select = Select(self.browser.find_element_by_id("id_values-0-type"))
        type_select.select_by_visible_text("Range")

        # Then user specifies the name of a element
        name = self.browser.find_element_by_id("id_values-0-name")
        name.send_keys("first")

        # User enters arguments range function

        elem_arg = self.browser.find_element_by_id("id_values-0-args")
        elem_arg.send_keys("0, 99, 3")

        # Finished with first element, user add another and another form appears

        add_button = arg_table.find_element_by_class_name("add-row")
        add_button.click()
        elem_forms = arg_table.find_elements_by_tag_name("tbody")
        self.assertEqual(elem_forms.size(), 2)

        # User specifies the second element, now a list of string values

        type_select = Select(self.browser.find_element_by_id("id_values-1-type"))
        type_select.select_by_visible_text("List of values")
        name = self.browser.find_element_by_id("id_values-1-name")
        name.send_keys("first")
        elem_arg = self.browser.find_element_by_id("id_values-1-args")
        elem_arg.send_keys("code, decode")

        # Then user uploads some files
        # First file

        files_table = self.browser.find_element_by_id("id_files_forms")
        add_file = files_table.find_element_by_id("id_files-0-file")
        add_file.send_keys(getcwd() + "file1")
        filearg_name = files_table.find_element_by_id("id_files-0-name")
        filearg_name.send_keys("files")

        # Then he adds another form for a file

        add_fileform = files_table.find_element_by_class_name("add-row")
        add_fileform.click()
        file_forms = files_table.find_elements_by_tag_name("tbody")
        self.assertEqual(file_forms.size(), 2)

        # And then uploads another file

        add_file = files_table.find_element_by_id("id_files-1-file")
        add_file.send_keys(getcwd() + "file2")
        filearg_name = files_table.find_element_by_id("id_files-1-name")
        filearg_name.send_keys("files")

        # Then user want to add another file, but do not include it in the arguments

        add_fileform.click()
        add_file = files_table.find_element_by_id("id_files-2-file")
        add_file.send_keys(getcwd() + "file3")

        # User has finished specifying the simulation, he hits submit button

        submit_button = self.browser.find_element_by_id("id_submit")
        submit_button.click()

        # He then redirected to the success page

        self.fail("Finish the test!")

