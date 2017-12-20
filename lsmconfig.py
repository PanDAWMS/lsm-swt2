#
# Configuration options for the Xrootd Local Site Mover
#
#
# PATH to the xrd executable
XRD='/cluster/xrootd/bin/xrd'
# PATH to the xrdcp exectutable
XRDCP='/cluster/xrootd/bin/xrdcp'
# PATH to the xrdadler32 executable
XRDADLER32='/cluster/xrootd/bin/xrdadler32'
# PATH to the xrootd library directory
LDPATH='/cluster/xrootd/lib'
# Your redirector
RDR='xrdb.local:1094'
# Don't know if I need this yet, but the SRM prefix for files
SRMPREFIX='srm://gk03.atlas-swt2.org:8443/srm/v2/server?SFN='
# Base path for Xrootd storage from WN perspective
# May not need if we don't support DF
DFPATH='/xrd'
# The xrootd virtual mapping path for the cluster
# Used for remote adler32 checksums
XRD_VMP='xrdb:/xrd=/xrd'
# logging directory
# SHould exist and a method for rotating files should
# be in place
LOGDIR='/var/log/lsm'

