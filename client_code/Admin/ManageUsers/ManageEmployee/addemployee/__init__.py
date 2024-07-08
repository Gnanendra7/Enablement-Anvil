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
    phone=self.text_box_phonenumber.text
    password = self.text_box_password.text
    repassword = self.text_box_reenterpassword.text
    
    
# Input validation
    if not (name and email and phone and password and repassword):
      Notification("Please fill all the fields").show()
      return

    # elif phone.isdigit():
    #   Notification("Phone number must be numeric").show()
    #   return

    elif password != repassword:
      Notification("Passwords do not match").show()
      return
      
    elif len(str(phone)) != 10:  # Check for phone number length
      Notification("Phone number must be exactly 10 digits").show()
      return

    try:
      phone_int = int(phone)  # Convert phone to int after validation
    except ValueError:
      Notification("Invalid phone number format").show()
      return

    # Server call from servermodule1_addemployee
    try:
      anvil.server.call('submit', name=name, email=email, phone=phone_int, password=password, repassword=repassword)
      Notification("Your employee details have been saved!!!").show()
    except Exception as e:
      Notification("An error occurred:",e).show()

