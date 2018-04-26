#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def find_bic(iban):
  res = requests.get('https://openiban.com/validate/' + iban + '?getBIC=true')
  for line in res.text.split("\n"):
    if "bic" in line:
     BIC = line.split()[-1].strip()
     BIC = BIC.replace('\"', '')
  return BIC
