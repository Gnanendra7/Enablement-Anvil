from ._anvil_designer import addemployeeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class addemployee(addemployeeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    open_form('Admin.ManageUsers.ManageEmployee')

  def button_1_click(self, **event_args):
    name=self.text_box_name.text
    email=self.text_box_email.text
    phone=int(self.text_box_phonenumber.text)
    password = self.text_box_password.text
    repassword = self.text_box_reenterpassword.text
    anvil.server.call('submit',name=name,email=email,phone=phone,password=password,repassword=repassword)
    Notification("Your employee details has been saved!!!").show()