import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def checkLoginDetails(username, password):
  foundRow = app_tables.accounts.get(email = username)
  if foundRow['password'] == password:
    fullname = getName(username)
    return True, foundRow['isTeacher'], fullname
  else:
    return False, foundRow['isTeacher'], "No Name"

def getName(name):
  name = name.replace("@dbbstu.catholic.edu.au","")
  name = name.replace("@dbb.catholic.edu.au","")
  name = name.split(".")
  firstName = name[0].capitalize()
  lastName = name[1].capitalize()
  fullname = firstName + " " + lastName
  return fullname
  