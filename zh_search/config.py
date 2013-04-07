"""
Configuration for the Chinese search package.
"""

import os

# Dictionary database used for searches.
DATABASE_PATH = os.path.dirname(__file__) + '/data/' + 'chinese.sqlite'

# Log file used for saving entries of interest.
LOGFILE_PATH = os.path.dirname(__file__) + '/data/' + 'log.txt'

# Dictionary of soundalikes
SOUNDALIKES = {'shi' : ['si','she'],
  'si' : ['shi', 'she'],
  'gan' : ['gang', 'guang'],
  'gang' : ['gan', 'guang'],
  'guang' : ['gan', 'gang'],
  'shan' : ['shang'],
  'shang' : ['shan'],
  'cai' : ['tai','zai'],
  'zai' : ['tai','cai'],
  'tai' : ['cai','zai'],
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
  'zhan' : ['zhang', 'zhuang'],
  'zhang' : ['zhan','zhuang'],
  'zhuang' : ['zhan', 'zhang'],
}

# The maximum length of a syllable for tokenising.
MAX_SYLLABLE_LENGTH = 6;

