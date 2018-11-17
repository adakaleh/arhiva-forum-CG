Forumul Computer Games a fost arhivat în paralel de mai mulți utilizatori. Arhivele sunt disponibile aici: https://revistevechi.awiki.org/computer_games

Am creat acest repo ca să prezint cum am făcut arhiva mea.

Forumul CG a fost imens, nu am avut timp să descarc tot, așa că am prioritizat anumite secțiuni care mă interesau mai mult sau care nu au fost incluse în alte arhive. Pentru asta am scris un mic crawler care a adunat o listă de link-uri către toate paginile din toate thread-urile forumului, le-am împărțit conform priorităților și am descărcat o parte din ele cu wget.

Forumul avea secțiuni vizibile doar membrilor, pentru care a fost nevoie ca script-urile să se autentifice. Am creat două conturi special pentru asta și le-am folosit în paralel.

Întâi am obținut link-urile către toate secțiunile forumului copiind codul HTML din "Quick Navigation" într-un fișier (all_forums.html), apoi rulând comanda:

  lynx -dump -hiddenlinks=listonly all_forums.html > all_forums.txt

Am editat all_forums.txt și am lăsat doar link-urile, câte unul pe rând. Le-am împărțit în mai multe fișiere, în funcție de prioritățile mele. De exemplu am vrut să încep cu secțiunile members-only, așa că le-am pus într-un fișier separat.

Apoi am scris un script python (crawl.py) cu care am extras link-urile către fiecare pagină din fiecare thread în mai multe fișiere text.

După care a venit rândul lui wget:
1. wget_login.sh a făcut login-ul și a salvat sesiunea în cookies.txt
2. wget_download.sh a descărcat efectiv paginile forumului, primind ca input link-urile adunate de crawl.py

Am inclus în arhive și fișierele forum.warc și wget.log, care arată în detaliu cum a decurs descărcarea.

Din păcate, arhiva nu include atașamentele, paginile membrilor și announcements. N-am avut timp să găsesc o soluție pentru descărcarea lor.

Arhiva conține următoarele secțiuni:

complete (cu excepția atașamentelor):
- Mass-media
- The Workshop
- History

incomplete (fără css, link-uri nefuncționale):
- Admin
- folder-ul „restul__incomplet”, care conține părți semnificative din secțiunile:
  - RPG
  - World of Warcraft
  - Console
  - Religie, credinta, agnosticism, ateism
  - Publicitate

Secțiunile complete arată cum trebuie și au link-uri funcționale către paginile descărcate, așa că puteți naviga normal prin ele.

Cele incomplete nu includ decât HTML-ul paginilor forumului. Lipsesc CSS-ul, JS-ul și imaginile, iar link-urile nu au fost modificate, deci navigarea din paginile descărcate nu va funcționa. Așa că am făcut în folderele „admin__incomplet” și „restul__incomplet” câte un index al tuturor paginilor din arhivă (index.html), ca să nu fie nevoie să săpați prin fișiere ca să vedeți conținului arhivei. Aceste index-uri au fost create cu script-ul makeindex.sh.

Cam atât.

Forumul CG a fost unul din cele mai importante forumuri românești. Mulțumiri tuturor celor implicați!

