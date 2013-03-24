#coding: utf8
"""
Pinyin search Chinese language database.

A tool to allow rapid look up of 'heard' Mandarin phrases bases on pinyin.

Allow fuzzy searches based on pinyin, return hits based on frequency.

"""

__author__ = 'Chris Hall<chris@clockwork-language.co.uk>'

import codecs
import re
import sqlite3

import android

import config


droid = android.Android()


def return_menu_items():
  """ Return the zh_search menu items provided by this module. """
  
  menu_items = []
  menu_items.append({'label' : 'Pinyin search', 'callback' : pinyin_run})
  menu_items.append({'label' : 'Pinyin fuzzy search', 'callback' : pinyin_run_fuzzy})
  
  return menu_items


def pinyin_run(fuzzy = 0, query = None):

  conn = sqlite3.connect(config.database)
  cursor = conn.cursor()
  
  log = codecs.open(config.logfile,'a','utf-8')
  
  while 1:
     
    if not query:
      query = get_query()
    
    if not query:
      return
    
    cursor.execute("select pinyin,simplified,definition,traditional,freq from Chinese where pinyin like ? order by freq desc limit 35",[process_query(query)]) 
  
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

    if not fuzzy:
      droid.dialogCreateAlert("Continue?", 'Search again?')
      droid.dialogSetPositiveButtonText('Yes')
      droid.dialogSetNegativeButtonText('No')
      droid.dialogShow()
    
      response = droid.dialogGetResponse().result
    
      if response['which'] == 'negative':
        conn.close()
        log.close()
        break
      else:
        query = None
        continue
       
    else:
      conn.close()
      log.close()
      break


def pinyin_run_fuzzy():
  
  query = get_query()
  
  queries = return_fuzzy_matches(query)
  
  while 1:
    
    droid.dialogCreateAlert('Pick a query')
    droid.dialogSetItems(queries)
    droid.dialogSetNegativeButtonText('Back')
    droid.dialogShow()
    
    response = droid.dialogGetResponse().result
      
    # 'Which' means exit has been selected, items are the menu choices.
    if 'which' in response or not 'item' in response:
      break
      
    pinyin_run(1, queries[response["item"]])


def return_fuzzy_matches(query):

  queries = [query]

  # Isolate the syllables in the query.
  r = re.compile('[a-z]{1,5}')
  syllables = r.findall(query)
  syllable_list = []
  
  # Add more syllables from the soundalikes
  additional_syllables = []
  for syllable in syllables:
    if syllable in config.soundalikes:
      additional_syllables = additional_syllables + config.soundalikes[syllable]
  
  syllables = syllables + additional_syllables
  
  # Create a list of syllables mapped to sound_alikes they may have.
  for syllable in syllables:
    if syllable in config.soundalikes:
      syllable_list.append({'syllable' : syllable,
        'soundalikes' : config.soundalikes[syllable],
      })
  
  # Loop over the syllable_map and generate new queries for combinations.
  for match in syllable_list:
    for soundalike in match['soundalikes']:
      additional_queries = []
      
      for q in queries:
        additional_query = q.replace(match['syllable'], soundalike, 1)
        
        if additional_query not in queries:
          additional_queries.append(additional_query)
          
      queries = queries + additional_queries

  # Return a deduped list of queries.
  return list(set(queries))


def get_query():
  """ Present a dialog to fetch a query string. """
  
  query = droid.dialogGetInput('search', 'Enter Pinyin text to search for').result
  return query


def process_query(query):
  """ Take a pinyin input and process for sql 'like' query.
  
  The doc tests below demonstrate how the regular expressions are supposed to work.
  
  >>> process_query('nan du')
  'nan_ du_'
  >>> process_query('nan??du')
  'nan_ % % du_'
  >>> process_query('nan3 du3')
  'nan3 du3'
  >>> process_query('nan')
  'nan_'
  >>> process_query('nan  ')
  'nan%'
  >>> process_query('nan du3')
  'nan_ du3'
  >>> process_query('nan  du3')
  'nan% du3'
  >>> process_query('nu:')
  'nu:_'
  >>> process_query('nu:3')
  'nu:3'
  >>> process_query('nu:3 du4')
  'nu:3 du4'
  >>> process_query('nu: du4')
  'nu:_ du4'
  >>> process_query('nü3')
  'nu:3'
  """
  
  # To support the umlaut version of u.
  r = re.compile('ü{1}')
  if r.search(query):
    query = r.sub(r'u:',query)
  
  # To support more conventional wildcards.
  r = re.compile('\?{1}')
  if r.search(query):
    query = r.sub(r' %',query)
    
  # Clean up % that need extra space.
  r = re.compile('%([a-z])')
  if r.search(query):
    query = r.sub(r'% \1',query)
    
  r = re.compile(' {2}')
  if r.search(query):
    query = r.sub(r'% ',query)
  
  r = re.compile('(% )$')
  if r.search(query):
    query = r.sub(r'%',query)
  
  r = re.compile('([a-z:]+)$')
  if r.search(query):
    query = r.sub(r'\1_',query)
  
  r = re.compile('([a-z:]+) ')
  if r.search(query):
    query = r.sub(r'\1_ ',query)
    
  return query
  
          
if __name__ == '__main__':
  pinyin_run()
  # import doctest
  # doctest.testmod()
  