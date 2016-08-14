#import entropy
#import zlib
#import bz2
#import timeit
import os


for root, directories, filenames in os.walk('~/Documents/'):
    for directory in directories:
        print(os.path.join(root, directory))
    for filename in filenames:
        print(os.path.join(root, filename))
"""
moby_dick = entropy.shannon_entropy('User/admin/Desktop/moby-dick.txt')
resume = entropy.shannon_entropy('User/admin/Desktop/resume.docx')

print("Entropy Results:")
print(moby_dick)
print(resume)
"""