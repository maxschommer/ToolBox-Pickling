import os
import anydbm
import pickle


t = [1,2,3]
s = pickle.dumps(t)
t2 = pickle.loads(s)
from pattern.web import *

f = Facebook(licence='CAAEuAis8fUgBAJQKS4ZBRUsxIRlsrW76PcYITJRC5hAoFmhYCyZBWDQc7NLFHtRABcRemTZA6YWByo12xL6ZB8gttBA4lDABIQI8fIcq9Eroaq2VRPoW8ZAPzarU1y7ZBL34eeYYO9TRNcpnMJsVrCN2gZAJICRcnCM5YsDZCXTANkNJSxD0sJw3kuoTGmYourEZD')
me = f.profile()
print me
print t2
print t2 == t
print t2 is t
# cmd = 'python Test.py'
# fp = os.popen(cmd)
# res = fp.read()
print res
# db = anydbm.open('lolcatz.db', 'c')

# db['LOLWUT'] = 'CATZZ!!!'
# print db['LOLWUT']
# db.close
# def test():
# 	# mystring = raw_input("Hi")
# 	# ("Input the letters you want to avoid:  ")
# 	fin = open('words.txt' , 'w')
# 	line1 = "This here's the wattle, \n"
# 	fin.write(line1)
# 	line2 = "the emblem of our land.\n"
# 	camels = 42
# 	print 'I have spotted %d camels.' % camels
# 	fin.write(line2)
# 	fin.close()
# test()


# def walk(dirname):
#     for name in os.listdir(dirname):
#         path = os.path.join(dirname, name)

#         if os.path.isfile(path):
#             print path
#         else:
#             walk(path)


# walk('/home')
