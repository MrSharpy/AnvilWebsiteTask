from ._anvil_designer import StudentPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StudentPage(StudentPageTemplate):
  def __init__(self, fullname, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.banana.text = f"Welcome {fullname}"
    

    # Any code you write here will run before the form opens.
