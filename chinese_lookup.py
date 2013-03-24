""" Ui entry point for Chinese search.

Get the menu items from the package and present user with
choice via android dialog.

Run appropriate callback function dependant on user choice.

"""

import android

import zh_search as zh

droid = android.Android()

def run():
  """ Loop for the search menu chooser dialog. """

  while 1:
  
    droid.dialogCreateAlert('What do you want to do?')
    droid.dialogSetItems(zh.menu.get_labels())
    droid.dialogSetNegativeButtonText('Exit')
    droid.dialogShow()
    
    response = droid.dialogGetResponse().result
    
    # 'Which' means exit has been selected, item is the index of the menu choice.
    if 'which' in response or not 'item' in response:
      break
 
    #Retrive and call the appropriate zh_search callback.
    zh.menu.get_callbacks()[response["item"]]()


if __name__ == '__main__':
  run()
