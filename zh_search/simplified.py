#coding: utf8

"""
Simplified search Chinese language database.

A tool to allow rapid look up of 'heard' Mandarin phrases bases on pinyin.

Allow fuzzy searches based on pinyin, return hits based on frequency.

"""

__author__ = 'Chris Hall<chris.mandarinstudent@googlemail.com>'

import codecs
import re
import sqlite3

import android

import config as c


def return_menu_items():
  menu_items = []
  menu_items.append({'label' : 'Simplified search', 'callback' : simplified_run})
  return menu_items
  
  
def simplified_run(database = None):
  
  conn = sqlite3.connect(c.DATABASE_PATH)
  cursor = conn.cursor()

  droid = android.Android()
  
  log = codecs.open(c.LOGFILE_PATH,'a','utf-8')
  
  while 1:
     
    query = droid.dialogGetInput('search', 'Enter Simplified text to search for').result
    
    if not query:
      return
    
    cursor.execute("select pinyin,simplified,definition,traditional,freq from Chinese where simplified like ? order by freq desc limit 100",[process_query(query)]) 
  
    for row in cursor:
      pinyin = row[0]
      simplified = row[1]
      definition = row[2]
      traditional = row[3]
      frequency = row[4]
      
      message = "%s / %s\n%s\n%s\nFreq:%s" % (simplified, traditional, pinyin, definition, frequency)
      
      droid.dialogCreateAlert("Result", message)
      droid.dialogSetPositiveButtonText('Continue')
      droid.dialogSetNegativeButtonText('Finish')
      droid.dialogSetNeutralButtonText('Log')
      droid.dialogShow()
      
      response = droid.dialogGetResponse().result
      
      if response and response['which'] == 'negative':
        break   
      
      if response and response['which'] == 'neutral':
        print >> log, "%s : %s : %s : %s : %s" % (pinyin, simplified, traditional, definition, frequency)
        
      print pinyin

      
    droid.dialogCreateAlert("Continue?", 'Search again?')
    droid.dialogSetPositiveButtonText('Yes')
    droid.dialogSetNegativeButtonText('No')
    droid.dialogShow()
    
    response = droid.dialogGetResponse().result
    
    if response['which'] == 'negative':
      conn.close()
      log.close()
      break

def process_query(query):

  """
  Take a simplified Chinese input and process for sql 'like' query.
  See doc tests below for expected behavour.
  """
  
  #To support more conventional wildcards.
  r = re.compile('\?')
  if r.search(query):
    query = r.sub(r'_',query)
    
  #The Chinese version of ?
  r = re.compile('\？')
  if r.search(query):
    query = r.sub(r'_',query)
    
  r = re.compile(' ')
  if r.search(query):
    query = r.sub(r'_',query)
    
  return query
  
          
if __name__ == '__main__':
  simplified_run()
  