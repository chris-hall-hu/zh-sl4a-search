

class Menu():
  """ Hold a list of menu labels and callbacks. """
  
  def __init__(self):
    self.menu_items = []
  
  def add_items(self, items = None):
    """ Add new menu items to items. """
    if not items: return
    
    for item in items:
      if 'label' in item and 'callback' in item:
        self.menu_items.append(item)
    
    return True 

  def get_labels(self):
    """ Return a list of labels for the current menu_items. """
    return [x['label'] for x in self.menu_items]

  def get_callbacks(self):
    """ Return a list of callback functions for the current menu_list. """
    return [x['callback'] for x in self.menu_items]


