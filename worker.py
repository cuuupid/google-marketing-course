import os

mds = []

for f in os.listdir('.'):
    if f.split('.')[-1] == 'md' and f != 'README.md':
        mds.append(f.split('.')[0])

template='''# Google Marketing Course: Digital Garage

Notes from Google's Digital Garage certification course online.

%s''' % '\n'.join(['[{x}](./{x})'.format(x=md) for md in mds])

open('README.md','w').write(template)
