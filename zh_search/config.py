"""
Configuration for the Chinese search package.
"""

import os

# Dictionary database used for searches.
database= os.path.dirname(__file__) + '/data/' + 'chinese.sqlite'

# Log file used for saving entries of interest.
logfile = os.path.dirname(__file__) + '/data/' + 'log.txt'

# Dictionary of soundalikes
soundalikes = {'shi' : ['si','she'],
  'si' : ['shi', 'she'],
  'gan' : ['gang', 'guang'],
  'gang' : ['gan', 'guang'],
  'guang' : ['gan', 'gang'],
  'shan' : ['shang'],
  'shang' : ['shan'],
  'cai' : ['tai'],
  'tai' : ['cai'],
  'she' : ['shi', 'si'],
  'shen' : ['sheng'],
  'sheng' : ['shen'],
  'shu' : ['xu'],
  'xu' : ['shu'],
  'che' : ['chi'],
  'chi' : ['che'],
  'fan' : ['fang'],
  'fang' : ['fan'],
  'guang' : ['gang'],
  'cong' : ['tong'],
  'tong' : ['cong'],
  'chu' : ['qu'],
  'qu' : ['chu'],
  'fan' : ['fang'],
  'fang' : ['fan'],
  'hen' : ['heng'],
  'heng' : ['hen'],
  'gen' : ['geng'],
  'geng' : ['gen'],
}