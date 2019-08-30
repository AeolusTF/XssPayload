# -*- coding: utf-8 -*-
__author__ = 'Ae0lus'

import re
n = 0
for xss in open("easyXssPayload.txt"):
    n += 1
    try:
        alert = re.findall(r"alert\((.+?)\)", xss)
        print(alert[0])
        xss = xss.replace(alert[0],str(n))
        print(xss)
        f = open("XssPayload.txt","a")
        f.write(xss)
        f.close()
    except:
        pass
