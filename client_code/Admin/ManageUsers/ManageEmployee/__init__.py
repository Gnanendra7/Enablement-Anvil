from ._anvil_designer import ManageEmployeeTemplate
from anvil import *
import anvil.server


class ManageEmployee(ManageEmployeeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_employee_button_click(self, **event_args):
    open_form('Admin.ManageUsers.ManageEmployee.addemployee')

  def link_1_click(self, **event_args):
   open_form('Admin.ManageUsers')
