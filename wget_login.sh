#!/bin/sh

# login și salvează cookie-urile în cookies.txt

wget \
	--save-cookies cookies.txt \
	--keep-session-cookies \
	--post-data 'vb_login_username=arhivist&vb_login_password=f4n3gonws&vb_login_password_hint=Password&cookieuser=1&s=&securitytoken=guest&do=login&vb_login_md5password=&vb_login_md5password_utf=' \
	--delete-after \
	'http://forum.computergames.ro/login.php?do=login'

# login alternativ (cu hash-uri md5)
	#--post-data 'vb_login_username=arhivar&vb_login_password=&vb_login_password_hint=Password&cookieuser=1&s=&securitytoken=guest&do=login&vb_login_md5password=cdcf585629c9241a7586deac51183629&vb_login_md5password_utf=cdcf585629c9241a7586deac51183629' \

