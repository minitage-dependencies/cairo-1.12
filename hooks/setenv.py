import os
import zc.buildout

os_ldflags=''
uname=os.uname()[0]
if uname == 'Darwin':
    os_ldflags=' -mmacosx-version-min=10.5.0'

def getcairoenv(options=None,buildout=None):
    cwd =os.getcwd()
    if buildout:
        for var in ['zlib','libxslt','libxml2','cairo','libpng','freetype','fontconfig']:
            append_env_var('PKG_CONFIG_PATH', ["%(lib)s/lib/pkgconfig/'"%{'lib':buildout[var]['location']}],sep=':',before=False)
            append_env_var('LDFLAGS', ["-L%(lib)s/lib -Wl,-rpath -Wl,%(lib)s/lib %(os)s"%{'lib':buildout[var]['location'],'os':os_ldflags}],sep=' ',before=False)
            append_env_var('CFLAGS', ["-I%s/include "%(buildout[var]['location'])],sep=' ',before=False)
            append_env_var('CPPFLAGS', ["-I%s/include "%(buildout[var]['location'])],sep=' ',before=False)
            append_env_var('LD_RUN_PATH', [buildout[var]['lib']],sep=':',before=False)
    else:
        for path in [ 'libxslt-1.1', 'libpng-1.2', 'libxml2-2.6', 'freetype-2.1', 'cairo-1.4' ,   'fontconfig-2.5',]:
        # when we call it from classical egg repices, we do not have the
        # buildout and options variables !
            os.environ['PKG_CONFIG_PATH'] = '%s/../../dependencies/%s/part/lib/pkgconfig:%s' % (cwd,path, os.environ.get('PKG_CONFIG_PATH',''))


        import sys
        for i in ['pycairo']:
            # are we in good context
            eggspath='%s/../../eggs/cache/' % cwd
            if os.path.isdir(eggspath):
            # search now eggs dir
                for dir in os.listdir(eggspath):
                    path="%s/%s" % (cwd,dir)
                    if dir.startswith(i):
                        os.environ['PKG_CONFIG_PATH'] = '%s/lib/pkgconfig/:%s' % ( path,os.environ.get('PKG_CONFIG_PATH'))


def append_env_var(env,var,sep=":",before=True):
    """ append text to a environnement variable
    @param env String variable to set
    @param before append before or after the variable"""
    for path in var:
    	if before:os.environ[env] = "%s%s%s" % (path,sep,os.environ.get(env,''))
	else:os.environ[env] = "%s%s%s" % (os.environ.get(env,''),sep,path)


# vim:set ts=4 sts=4 et  :
