#!/bin/sh

wget \
	-U "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0" \
	-nv \
	-o wget.log \
	--directory-prefix files/ \
	--force-directories \
	--load-cookies cookies.txt \
	--adjust-extension \
	-e "robots=off" \
	--timeout 10 \
	--tries 3 \
	--waitretry 5 \
	--convert-links \
	--warc-file forum \
	--warc-header "operator: arhivist" \
	--input-file forum_links.txt


# încetinește descărcarea
#	--wait 0.3 \
#	--random-wait \

# include imagini, CSS, etc.
#	--page-requisites --span-hosts \

# ignoră fișierele inexistente, ca să eviți răspunsurile "404 not found" repetate
#	--reject yellow-card_sm-hover.png,android_icon.png,android_icon-hover.png,iphone_icon.png,iphone_icon-hover.png,facebook_icon.png,facebook_icon-hover.png,controls.png,blackdot.gif,rec_live_cg.png,avatar26421_1.gif,unsubscribed_40b.png \

