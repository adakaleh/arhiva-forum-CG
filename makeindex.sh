#!/bin/sh

# Script pentru generarea fișierelor index.html din folderele „admin__incomplet” și „restul__incomplet”

# 1. găsește toate fișierele html, sortează-le și elimină prefixul "./" din fiecare rând
#find . -name '*.html' | sort -n | cut -c 3- > links.txt

# 2. [sortare manuală]

# 3. generează link-uri
while read line; do
	echo '<a href="'$line'">'${line#"files/forum.computergames.ro/"}'</a><br>' >> index.html
done < links.txt
