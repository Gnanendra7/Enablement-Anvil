from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server

class Login(LoginTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        email_user = self.email_textbox.text
        user_password = self.password_textbox.text
        
        user = anvil.server.call('get_user', email_user, user_password)
        
        if user:
            user_type = user['user_type']
            if user_type=='admin':
              open_form('Admin')
            else:
              open_form('Employee')
          
            # Define a mapping from user_type to form names
        #     user_type_to_form = {
        #         "admin": "Admin",
        #         "employee": "Employee"
        #     }
        #     form_name = user_type_to_form.get(user_type)
            
        #     if form_name:
        #         open_form(form_name,user)
        #     else:
        #         alert("Invalid user type detected.")
        # else:
        #     alert("Incorrect email or password.")


        
        
    

   
