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
import time

import android

import config as c


droid = android.Android()


def return_menu_items():
  """ Return the zh_search menu items provided by this module. """
  
  menu_items = []
  menu_items.append({'label' : 'Pinyin search', 'callback' : pinyin_run})
  menu_items.append({'label' : 'Pinyin fuzzy search', 'callback' : pinyin_run_fuzzy})
  
  return menu_items


def pinyin_run(fuzzy = 0, query = None):

  conn = sqlite3.connect(c.DATABASE_PATH)
  cursor = conn.cursor()
  
  log = codecs.open(c.LOGFILE_PATH,'a','utf-8')
  
  while 1:
     
    if not query:
      query = get_query()
    
    if not query:
      return
    
    cursor.execute("""select pinyin,simplified,definition,traditional,freq 
      from Chinese 
      where pinyin like ? 
      order by freq desc 
      limit 35""",[process_query(query)]) 
  
    for row in cursor:
    
      pinyin, simplified, definition, traditional, frequency = row
      
      message = "%s / %s\n%s\n%s\nFreq:%s" % (
        simplified,
        traditional,
        pinyin,
        definition,
        frequency)
      
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
  
  queries.sort()
  
  while 1:
    
    droid.dialogCreateAlert('Pick a query')
    droid.dialogSetItems(queries)
    droid.dialogSetNegativeButtonText('Back')
    droid.dialogShow()
    
    response = droid.dialogGetResponse().result
      
    # 'which' means exit has been selected, items are the menu choices.
    if 'which' in response or not 'item' in response:
      break
      
    pinyin_run(1, queries[response["item"]])


def return_fuzzy_matches(query):
  
  title = 'Processing'
  message = 'Checking alternatives!'
  droid.dialogCreateSpinnerProgress(title, message)
  
  droid.dialogShow()
  
  # Prepare for a list of queries.
  queries = [query]

  # Isolate the syllables in the query.
  r = re.compile('[a-z]{1,%d}' % c.MAX_SYLLABLE_LENGTH)
  syllables = r.findall(query)
  syllable_list = []
  
  # Add more syllables from the soundalikes
  additional_syllables = []
  for syllable in syllables:
    if syllable in c.SOUND_ALIKES:
      additional_syllables = additional_syllables + c.SOUND_ALIKES[syllable]
  
  syllables = syllables + additional_syllables
  
  # Create a list of syllables mapped to sound_alikes they may have.
  for syllable in syllables:
    if syllable in c.SOUND_ALIKES:
      syllable_list.append({'syllable' : syllable,
        'soundalikes' : c.SOUND_ALIKES[syllable],
      })
  
  # Loop over the syllable_map and generate new queries for combinations.
  for match in syllable_list:
    for soundalike in match['soundalikes']:
      additional_queries = []
      
      for q in queries:
        r = re.compile(match['syllable'] + '($|[^a-z]{1})')
        if r.search(q):
          additional_query = r.sub(soundalike + r'\1',q,1)
        
        if additional_query not in queries:
          additional_queries.append(additional_query)
          
      queries = queries + additional_queries

  # Return a deduped list of queries.
  droid.DialogDismiss()
  
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
  >>> process_query('nan ')
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
  query = re.sub(u'ü{1}', r'u:', query)
    
  # To support more conventional wildcards.
  query = re.sub('\?{1}', r' %', query)
  
  # Clean up % that need extra space.
  query = re.sub('%([a-z])', r'% \1', query)
   
  # Convert double space to % wildcard.
  query = re.sub(' {2}', r'% ', query)
  
  # Trim final space from queries that end in %.
  query = re.sub('(% )$', r'%', query)
  
  # Append _ to naked syllables at the end of the query.
  query = re.sub('([a-z:]+)$', r'\1_', query)
  
  # Append _ to queries that end with syllables and space. 
  query = re.sub('([a-z:]+) $', r'\1_', query)
  
  # Append _ to syllables which are follwed by a space.
  query = re.sub('([a-z:]+) ', r'\1_ ', query)
    
  return query
  
          
if __name__ == '__main__':
  pinyin_run()
  #import doctest
  #doctest.testmod()
  
