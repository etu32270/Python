from textwrap import wrap
s1 = "qsfuihDFKJBSKJDVBQDKVBcscsdc<cscoXHJHCWKJXCQC"
s2 = ""
print(wrap(s1,5))
for s in wrap(s1, 5):
    s2 = s + s2
print(s2)
