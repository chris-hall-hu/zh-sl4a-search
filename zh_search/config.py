"""
Configuration for the Chinese search package.
"""

import os

# Dictionary database used for searches.
DATABASE_PATH = os.path.dirname(__file__) + '/data/' + 'chinese.sqlite'

# Log file used for saving entries of interest.
LOGFILE_PATH = os.path.dirname(__file__) + '/data/' + 'log.txt'

# Dictionary of soundalikes
SOUND_ALIKES = {
  'cai' : ['tai','zai'],
  'che' : ['chi'],
  'chen' : ['cheng'],
  'cheng' : ['chen'],
  'chi' : ['che'],
  'chu' : ['qu'],
  'ci' : ['zi'],
  'cong' : ['tong'],
  'fan' : ['fang'],
  'fang' : ['fan'],
  'fen' : ['feng'],
  'feng' : ['fen'],
  'gan' : ['gang', 'guang'],
  'gang' : ['gan', 'guang'],
  'gen' : ['geng'],
  'geng' : ['gen'],
  'guang' : ['gan', 'gang'],
  'hen' : ['heng'],
  'heng' : ['hen'],
  'shan' : ['shang', 'xiang'],
  'shang' : ['shan', 'xiang'],  
  'she' : ['shi', 'si'],
  'shen' : ['sheng'],
  'shi' : ['si','she'],
  'sheng' : ['shen'],
  'shu' : ['xu'],
  'si' : ['shi', 'she'],
  'tai' : ['cai','zai'],
  'tong' : ['cong'],
  'qu' : ['chu'],
  'xiang' : ['shan', 'shang'],
  'xin' : ['xing'],
  'xing' : ['xin'],
  'xu' : ['shu'],
  'yin' : ['ying'],
  'ying' : ['ying'],
  'zai' : ['tai','cai'],
  'zhan' : ['zhang', 'zhuang'],
  'zhang' : ['zhan','zhuang'],
  'zhuang' : ['zhan', 'zhang'],
  'zhe' : ['ze'],
  'ze' : ['zhe'],
  'zhou' : ['zhao'],
  'zhao' : ['zhou'],
  'zi' : ['ci'],
}

# The maximum length of a syllable for tokenising.
MAX_SYLLABLE_LENGTH = 6;

