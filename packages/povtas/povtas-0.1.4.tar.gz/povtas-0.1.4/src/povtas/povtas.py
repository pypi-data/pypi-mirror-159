#!/usr/bin/env python
import re

def povtas_sub(string):
    string = re.sub("r", "v", string)
    return re.sub("R", "V", string)