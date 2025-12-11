from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def btnLogin_click(self, **event_args):
    loginPass, isTeacher, fullname = anvil.server.call('checkLoginDetails', self.txtbUsername.text, self.txtbPassword.text)
    if not loginPass:
      self.lblError.visible = True
    else:
      if isTeacher:
        open_form('TeacherPage', fullname)
      else:
        open_form('StudentPage', fullname)
