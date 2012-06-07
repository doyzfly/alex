#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import __init__

import SDS.utils.audio as audio

from SDS.components.tts.google import GoogleTTS

print "Synthesize all sentences"
print "="*120
print

text = 'Dobrý den. Děkujeme za zavolání.'
language = 'cs'
sample_rate = 8000

print "Language:       ", language
print "Sample rate:    ", sample_rate
print

cfg = {
  'Audio': {
      'sample_rate': sample_rate
    },
  'TTS': {
    'Google': {
      'debug': False,
      'language' : language
    }
  }
}

tts = GoogleTTS(cfg)

f = open('mkp_rur_matka.txt', 'r')
r = []
for s in f:
  s = s.strip()
  r.append(s)
f.close()

for s in r:
  print 'calling TTS: ', s
  wav = tts.synthesize(s)

  n = s.replace(' ', '_')

  print 'saving the TTS audio in ./tmp/gtts_%s.wav' % n
  audio.save_wav(cfg, './tmp/gtts_%s.wav' %n, wav)

  #time.sleep(random.randint(1, 10))