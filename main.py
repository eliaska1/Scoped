from src.common import utils
from src.modules.interfaces import Module
from src.modules import *


# Compile assignments into a list
assignments = {}
modules = [
    Gradescope()
]
for module in modules:
    module.run(assignments)

# Save the list to a JavaScript file for Planit to import later
utils.save_data('assignments', assignments)
