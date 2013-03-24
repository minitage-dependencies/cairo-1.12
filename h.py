import os
import sys
def h(options, buildout):
    if sys.platform.startswith('cygwin'):
        c = os.getcwd()
        os.chdir(options['compile-directory'])
        os.system("autoreconf -ifv")
        #r = open('config.h.in').readlines()
        #r.append('\n\n#define _POSIX_C_SOURCE 200112L\n\n')
        #open('config.h.in', 'w').writelines(r)
def p(options, buildout):
    if sys.platform.startswith('cygwin'):
        c = os.getcwd()
        os.chdir(options['compile-directory'])
        r = open('config.h').readlines()
        r.append('\n\n#define _POSIX_C_SOURCE 200112L\n\n')
        open('config.h', 'w').writelines(r)
        
def q(options, buildout):
    import pdb;pdb.set_trace()

