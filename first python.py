Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> python --version
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    python --version
NameError: name 'python' is not defined
>>> len("galatasaray")
11
>>> prim
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    prim
NameError: name 'prim' is not defined
>>> print("""galatasaray is the
best team
in TURKEY""")
galatasaray is the
best team
in TURKEY
>>> print(""galatasaray
      
SyntaxError: invalid syntax
>>> print("""dışarda deli dalgalar
gelip duvarları yalar
seni bu sesler oyalar
aldırma gönül aldırma""")
dışarda deli dalgalar
gelip duvarları yalar
seni bu sesler oyalar
aldırma gönül aldırma
>>> print("""-------------
|            |
|            |
|            |
|            |
|            |
-------------""")
-------------
|            |
|            |
|            |
|            |
|            |
-------------
>>> 
>>> print("""--------------
|            |
|            |
|            |
|            |
|            |
--------------""")
--------------
|            |
|            |
|            |
|            |
|            |
--------------
>>> (""" ... [H]=========HARMAN========[-][o][x] ... | | ... | Programa Hoşgeldiniz! | ... | Sürüm 0.8 | ... | Devam etmek için herhangi | ... | bir düğmeye basın. | ... | | ... |=================================| ... """)
' ... [H]=========HARMAN========[-][o][x] ... | | ... | Programa Hoşgeldiniz! | ... | Sürüm 0.8 | ... | Devam etmek için herhangi | ... | bir düğmeye basın. | ... | | ... |=================================| ... '
>>> (""" [H]=========HARMAN========[-][o][x]| | ... | Programa Hoşgeldiniz! | ... | Sürüm 0.8 | ... | Devam etmek için herhangi | ... | bir düğmeye basın. | ... | | ... |=================================| ... """)
' [H]=========HARMAN========[-][o][x]| | ... | Programa Hoşgeldiniz! | ... | Sürüm 0.8 | ... | Devam etmek için herhangi | ... | bir düğmeye basın. | ... | | ... |=================================| ... '
>>> ("""[H]=========HARMAN========[-][o][x] ... | | ... | Programa Hoşgeldiniz! | ... | Sürüm 0.8 | ... | Devam etmek için herhangi | ... | bir düğmeye basın. | ... | | ... |=================================| ...
""")
'[H]=========HARMAN========[-][o][x] ... | | ... | Programa Hoşgeldiniz! | ... | Sürüm 0.8 | ... | Devam etmek için herhangi | ... | bir düğmeye basın. | ... | | ... |=================================| ...\n'
>>> print("""
[H]=========HARMAN========[-][o][x]
|                                 |
|       Programa Hoşgeldiniz!     |
|            Sürüm 0.8            |
|   Devam etmek için herhangi     |
|        bir düğmeye basın.       |
|                                 |
|=================================|""")

[H]=========HARMAN========[-][o][x]
|                                 |
|       Programa Hoşgeldiniz!     |
|            Sürüm 0.8            |
|   Devam etmek için herhangi     |
|        bir düğmeye basın.       |
|                                 |
|=================================|
>>> 
>>> """game over
insert coin"""
'game over\ninsert coin'
>>> print("""game over
insert coin""")
game over
insert coin
>>> print("""son yıllarda başımıza gelen felaketler;
depremler,
seller,
tsunamiler,
corona.
umarım daha fazlası olmaz""")
son yıllarda başımıza gelen felaketler;
depremler,
seller,
tsunamiler,
corona.
umarım daha fazlası olmaz
>>> 