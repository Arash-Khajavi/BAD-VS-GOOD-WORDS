import string
def words_check(text):
    l=[]
    for y in string.ascii_letters:
        l.append(y)
    pri=text.split(" ")
    lk=[]
    for i in pri:
        # print(i)
        for tyu in i:
            lk.append(tyu)
    # print(lk)
    # print(l)
    print(lk)
    for ui in lk:
        # print(ui)
        if ui not in l:
            # print(ui)
            for i in pri:
                pri1=len(i)
                if ui in i:
                    pr=i.count(ui)
                    if pri1 / 2 <= pr:
                        pri.remove(i)

    print(pri)
    j=[]
    for nh in pri:
        for iu in nh:
            j.append(iu)
            if iu not in l:
                prin=nh.replace(iu,"")
                # print(prin)
                p=pri.index(nh)
                pri[p] = prin
                print(p)
                break

    print(pri)
    jhg=[]
    for hu in pri:
        capital=hu.capitalize()
        jhg.append(capital)
    print(" ".join(jhg))
    # print(' '.join(j))




        # break
            # lk.remove(ui)
    # print(lk)
words_check('"hEllO My FriEnDs!!! thIS i$s A tE%sT For your #p#r#o#b#l#e#m a')
