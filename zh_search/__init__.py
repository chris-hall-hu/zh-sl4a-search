import pinyin
import simplified
import english

import search_menu

menu = search_menu.Menu()
  
menu.add_items(pinyin.return_menu_items())
menu.add_items(simplified.return_menu_items())
menu.add_items(english.return_menu_items())

