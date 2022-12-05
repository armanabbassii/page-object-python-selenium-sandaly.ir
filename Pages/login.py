class Login:

    def __init__(self,driver):
        self.driver = driver
        self.name_textbox_id = "form-field-name"
        self.phonenumber_textbox_id = "form-field-email"
        self.message_textbox_id = "form-field-message"
        #self.send_button_class = driver.find_element(By.xpath, "//*[@class = 'elementor-button-text '][1]")
       # self.send_button_class = "//span[@className= 'elementor-button-text'][1]"
        #self.send_button_class = "(//span[@class= 'elementor-button-text'])[1]"
        #self.send_button_class = "//span[text()= 'ارسال'][1]"
        self.send_button_class = "elementor-button-text"
    def enter_name (self, name):
        self.driver.find_element ('id', self.name_textbox_id).send_keys(name)

    def enter_phonenumber (self,phonenumber):
        self.driver.find_element ('id', self.phonenumber_textbox_id).send_keys(phonenumber)

    def enter_message(self, message):
        self.driver.find_element ('id', self.message_textbox_id).send_keys(message)

    def click_on_send_button (self):
        self.driver.find_element('xpath',"//*[@class ='elementor-button-text'][1]").click()


    # we set attribute in this class and we can use all functional and other thing that using from this class, we can use from this attribute
