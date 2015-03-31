import os,sys

def lottoroll():
    da = input("enter the first digit of the most recent number:")
    db = input("enter the second digit of the most recent number:")
    dc = input("enter the third digit of the most recent number:")
    am=0
    bm=0
    cm=0
    g=0 ##variable used to keep track of and determine chance of a double number
    h=0 ##variable used to keep track of and determine chance of triple number
    q=0 ## just number counters, q-z = 0-9 respectively
    r=0
    s=0
    t=0
    u=0
    v=0
    w=0
    e=0
    y=0
    z=0
    l=0
    m=0
    q1=0 ## will be used for keeping count on number of times a number appears in what order
    r1=0
    s1=0
    t1=0
    u1=0
    v1=0
    w1=0
    e1=0
    y1=0
    z1=0
    q2=0
    r2=0
    s2=0
    t2=0
    u2=0
    v2=0
    w2=0
    e2=0
    y2=0
    z2=0
    q3=0
    r3=0
    s3=0
    t3=0
    u3=0
    v3=0
    w3=0
    e3=0
    y3=0
    z3=0

    lista = [] ## list to keep track of each entry to find average for pi formula
    listb = []
    listc = []
    
    
    for x in range(5):
        a = 0
        b = 0
        c = 0
        a = input("enter the first number:")
        if a == 0:
            q=q+1
            q1=q1+1
        elif a == 1:
            r=r+1
            r1=r1+1
        elif a == 2:
            s=s+1
            s1= s1+1
        elif a == 3:
            t=t+1
            t1=t1+1
        elif a == 4:
            u=u+1
            u1=u1+1
        elif a == 5:
            v=v+1
            v1=v1+1
        elif a == 6:
            w=w+1
            w1=w1+1
        elif a == 7:
            e=e+1
            e1=e1+1
        elif a == 8:
            y=y+1
            y1=y1+1
        else:
            z=z+1
            z1=z1+1

        lista.append(a) ## adding each entry to the list of a
        
        b = input("enter the second number:")
        if b == 0:
            q = q+1
            q2 = q2+1
        elif b == 1:
            r=r+1
            r2=r2+1
        elif b == 2:
            s=s+1
            s2= s2+1
        elif b == 3:
            t=t+1
            t2=t2+1
        elif b == 4:
            u=u+1
            u2=u2+1
        elif b == 5:
            v=v+1
            v2=v2+1
        elif b == 6:
            w=w+1
            w2=w2+1
        elif b == 7:
            e=e+1
            e2=e2+1
        elif b == 8:
            y=y+1
            y2=y2+1
        else:
            z=z+1
            z2=z2+1
            
        listb.append(b)
        
        c = input("enter the third number:")
        if c == 0:
            q=q+1
            q3=q3+1
        elif c == 1:
            r=r+1
            r3=r3+1
        elif c == 2:
            s=s+1
            s3= s3+1
        elif c == 3:
            t=t+1
            t3=t3+1
        elif c == 4:
            u=u+1
            u3=u3+1
        elif c == 5:
            v=v+1
            v3=v3+1
        elif c == 6:
            w=w+1
            w3=w3+1
        elif c == 7:
            e=e+1
            e3=e3+1
        elif c == 8:
            y=y+1
            y3=y3+1
        else:
            z=z+1
            z3=z3+1
            
        if a==b or a==c or b==c:
            g=g+1
        if a==b and b==c and a==c:
            h=h+1
            
        listc.append(c)

        
    qp = (q*100)/15
    rp = (r*100)/15
    sp = (s*100)/15
    tp = (t*100)/15
    up = (u*100)/15
    vp = (v*100)/15
    wp = (w*100)/15
    ep = (e*100)/15
    yp = (y*100)/15
    zp = (z*100)/15
    gp = (g*100)/5
    hp = (h*100)/5
    qa = (q1*100)/5
    ra = (r1*100)/5
    sa = (s1*100)/5
    ta = (t1*100)/5
    ua = (u1*100)/5
    va = (v1*100)/5
    wa = (w1*100)/5
    ea = (e1*100)/5
    ya = (y1*100)/5
    za = (z1*100)/5
    qb = (q2*100)/5
    rb = (r2*100)/5
    sb = (s2*100)/5
    tb = (t2*100)/5
    ub = (u2*100)/5
    vb = (v2*100)/5
    wb = (w2*100)/5
    eb = (e2*100)/5
    yb = (y2*100)/5
    zb = (z2*100)/5
    qc = (q3*100)/5
    rc = (r3*100)/5
    sc = (s3*100)/5
    tc = (t3*100)/5
    uc = (u3*100)/5
    vc = (v3*100)/5
    wc = (w3*100)/5
    ec = (e3*100)/5
    yc = (y3*100)/5
    zc = (z3*100)/5
    
    print "0 appears %d percent of the time" % (qp)
    print "1 appears %d percent of the time" % (rp)
    print "2 appears %d percent of the time" % (sp)
    print "3 appears %d percent of the time" % (tp)
    print "4 appears %d percent of the time" % (up)
    print "5 appears %d percent of the time" % (vp)
    print "6 appears %d percent of the time" % (wp)
    print "7 appears %d percent of the time" % (ep)
    print "8 appears %d percent of the time" % (yp)
    print "9 appears %d percent of the time" % (zp)

    ## Determining the most likely to appear

    if qp>rp and qp>sp and qp>tp and qp>up and qp>vp and qp>wp and qp>ep and qp>yp and qp>zp:
        m=0
    elif rp>qp and rp>sp and rp>tp and rp>up and rp>vp and rp>wp and rp>ep and rp>yp and rp>zp:
        m=1
    elif sp>rp and sp>qp and sp>tp and sp>up and sp>vp and sp>wp and sp>ep and sp>yp and sp>zp:
        m=2
    elif tp>rp and tp>sp and tp>qp and tp>up and tp>vp and tp>wp and tp>ep and tp>yp and tp>zp:
        m=3
    elif up>rp and up>sp and up>tp and up>qp and up>vp and up>wp and up>ep and up>yp and up>zp:
        m=4
    elif vp>rp and vp>sp and vp>tp and vp>up and vp>qp and vp>wp and vp>ep and vp>yp and vp>zp:
        m=5        
    elif wp>rp and wp>sp and wp>tp and wp>up and wp>vp and wp>qp and wp>ep and wp>yp and wp>zp:
        m=6    
    elif ep>rp and ep>sp and ep>tp and ep>up and ep>vp and ep>wp and ep>qp and ep>yp and ep>zp:
        m=7 
    elif yp>rp and yp>sp and yp>tp and yp>up and yp>vp and yp>wp and yp>ep and yp>qp and yp>zp:
        m=8       
    else:
        m=9

    print "%d has the highest percentage of appearence" % (m)

    ##Determining the least likely to appear
    if qp<rp and qp<sp and qp<tp and qp<up and qp<vp and qp<wp and qp<ep and qp<yp and qp<zp:
        l=0
    elif rp<qp and rp<sp and rp<tp and rp<up and rp<vp and rp<wp and rp<ep and rp<yp and rp<zp:
        l=1
    elif sp<rp and sp<qp and sp<tp and sp<up and sp<vp and sp<wp and sp<ep and sp<yp and sp<zp:
        l=2
    elif tp<rp and tp<sp and tp<qp and tp<up and tp<vp and tp<wp and tp<ep and tp<yp and tp<zp:
        l=3
    elif up<rp and up<sp and up<tp and up<qp and up<vp and up<wp and up<ep and up<yp and up<zp:
        l=4
    elif vp<rp and vp<sp and vp<tp and vp<up and vp<qp and vp<wp and vp<ep and vp<yp and vp<zp:
        l=5        
    elif wp<rp and wp<sp and wp<tp and wp<up and wp<vp and wp<qp and wp<ep and wp<yp and wp<zp:
        l=6    
    elif ep<rp and ep<sp and ep<tp and ep<up and ep<vp and ep<wp and ep<qp and ep<yp and ep<zp:
        l=7 
    elif yp<rp and yp<sp and yp<tp and yp<up and yp<vp and yp<wp and yp<ep and yp<qp and yp<zp:
        l=8       
    else:
        l=9

    print "%d has the lowest percentage of appearence" % (l)


    ##determining the most likely first number
    if qa>ra and qa>sa and qa>ta and qa>ua and qa>va and qa>wa and qa>ea and qa>ya and qa>za:
        print "0 is the most likely number to appear first"
        am = 0
    elif ra>qa and ra>sa and ra>ta and ra>ua and ra>va and ra>wa and ra>ea and ra>ya and ra>za:
        print "1 is the most likely number to appear first"
        am = 1
    elif sa>ra and sa>qa and sa>ta and sa>ua and sa>va and sa>wa and sa>ea and sa>ya and sa>za:
        print "2 is the most likely number to appear first"
        am = 2
    elif ta>ra and ta>sa and ta>qa and ta>ua and ta>va and ta>wa and ta>ea and ta>ya and ta>za:
        print "3 is the most likely number to appear first"
        am = 3
    elif ua>ra and ua>sa and ua>ta and ua>qa and ua>va and ua>wa and ua>ea and ua>ya and ua>za:
        print "4 is the most likely number to appear first"
        am = 4
    elif va>ra and va>sa and va>ta and va>ua and va>qa and va>wa and va>ea and va>ya and va>za:
        print "5 is the most likely number to appear first"
        am = 5
    elif wa>ra and wa>sa and wa>ta and wa>ua and wa>va and wa>qa and wa>ea and wa>ya and wa>za:
        print "6 is the most likely number to appear first"
        am = 6
    elif ea>ra and ea>sa and ea>ta and ea>ua and ea>va and ea>wa and ea>qa and ea>ya and ea>za:
        print "7 is the most likely number to appear first"
        am = 7
    elif ya>ra and ya>sa and ya>ta and ya>ua and ya>va and ya>wa and ya>ea and ya>qa and ya>za:
        print "8 is the most likely number to appear first"
        am = 8
    elif za>ra and za>sa and za>ta and za>ua and za>va and za>wa and za>ea and za>qa and za>ya:
        print "9 is the most likely number to appear first"
        am = 9
    else:
        print "The first number is more likely to be a lower percentage number but well assume the average"
        am = (sum(lista)/5)

    ##determining the most likely second number
    if qb>rb and qb>sb and qb>tb and qb>ub and qb>vb and qb>wb and qb>eb and qb>yb and qb>zb:
        print "0 is the most likely number to appear second"
        bm = 0
    elif rb>qb and rb>sb and rb>tb and rb>ub and rb>vb and rb>wb and rb>eb and rb>yb and rb>zb:
        print "1 is the most likely number to appear second"
        bm = 1
    elif sb>rb and sb>qb and sb>tb and sb>ub and sb>vb and sb>wb and sb>eb and sb>yb and sb>zb:
        print "2 is the most likely number to appear second"
        bm = 2
    elif tb>rb and tb>sb and tb>qb and tb>ub and tb>vb and tb>wb and tb>eb and tb>yb and tb>zb:
        print "3 is the most likely number to appear second"
        bm = 3
    elif ub>rb and ub>sb and ub>tb and ub>qb and ub>vb and ub>wb and ub>eb and ub>yb and ub>zb:
        print "4 is the most likely number to appear second"
        bm =4
    elif vb>rb and vb>sb and vb>tb and vb>ub and vb>qb and vb>wb and vb>eb and vb>yb and vb>zb:
        print "5 is the most likely number to appear second"
        bm = 5
    elif wb>rb and wb>sb and wb>tb and wb>ub and wb>vb and wb>qb and wb>eb and wb>yb and wb>zb:
        print "6 is the most likely number to appear second"
        bm = 6
    elif eb>rb and eb>sb and eb>tb and eb>ub and eb>vb and eb>wb and eb>qb and eb>yb and eb>zb:
        print "7 is the most likely number to appear second"
        bm = 7
    elif yb>rb and yb>sb and yb>tb and yb>ub and yb>vb and yb>wb and yb>eb and yb>qb and yb>zb:
        print "8 is the most likely number to appear second"
        bm = 8
    elif zb>rb and zb>sb and zb>tb and zb>ub and zb>vb and zb>wb and zb>eb and zb>qb and zb>yb:
        print "9 is the most likely number to appear second"
        bm = 9
    else:
        print "The second number is more likely to be a lower percentage number but well assume the average"
        am = (sum(listb)/5)

    ##determinging the most likely third number
    if qc>rc and qc>sc and qc>tc and qc>uc and qc>vc and qc>wc and qc>ec and qc>yc and qc>zc:
        print "0 is the most likely number to appear third"
        cm = 0
    elif rc>qc and rc>sc and rc>tc and rc>uc and rc>vc and rc>wc and rc>ec and rc>yc and rc>zc:
        print "1 is the most likely number to appear third"
        cm = 1
    elif sc>rc and sc>qc and sc>tc and sc>uc and sc>vc and sc>wc and sc>ec and sc>yc and sc>zc:
        print "2 is the most likely number to appear third"
        cm = 2
    elif tc>rc and tc>sc and tc>qc and tc>uc and tc>vc and tc>wc and tc>ec and tc>yc and tc>zc:
        print "3 is the most likely number to appear third"
        cm = 3
    elif uc>rc and uc>sc and uc>tc and uc>qc and uc>vc and uc>wc and uc>ec and uc>yc and uc>zc:
        print "4 is the most likely number to appear third"
        cm = 4
    elif vc>rc and vc>sc and vc>tc and vc>uc and vc>qc and vc>wc and vc>ec and vc>yc and vc>zc:
        print "5 is the most likely number to appear third"
        cm = 5
    elif wc>rc and wc>sc and wc>tc and wc>uc and wc>vc and wc>qc and wc>ec and wc>yc and wc>zc:
        print "6 is the most likely number to appear third"
        cm = 6
    elif ec>rc and ec>sc and ec>tc and ec>uc and ec>vc and ec>wc and ec>qc and ec>yc and ec>zc:
        print "7 is the most likely number to appear third"
        cm = 7
    elif yc>rc and yc>sc and yc>tc and yc>uc and yc>vc and yc>wc and yc>ec and yc>qc and yc>zc:
        print "8 is the most likely number to appear third"
        cm = 8
    elif zc>rc and zc>sc and zc>tc and zc>uc and zc>vc and zc>wc and zc>ec and zc>qc and zc>yc:
        print "9 is the most likely number to appear third"
        cm = 9
    else:
        print "The third number is more likely to be a lower percentage number but well assume the average"
        cm = (sum(listc)/5)
        
    ##determining the least likely first number
    if qa<ra and qa<sa and qa<ta and qa<ua and qa<va and qa<wa and qa<ea and qa<ya and qa<za:
        print "0 is the least likely number to appear first"
        ad = 0
    elif ra<qa and ra<sa and ra<ta and ra<ua and ra<va and ra<wa and ra<ea and ra<ya and ra<za:
        print "1 is the least likely number to appear first"
        ad = 1
    elif sa<ra and sa<qa and sa<ta and sa<ua and sa<va and sa<wa and sa<ea and sa<ya and sa<za:
        print "2 is the least likely number to appear first"
        ad = 2
    elif ta<ra and ta<sa and ta<qa and ta<ua and ta<va and ta<wa and ta<ea and ta<ya and ta<za:
        print "3 is the least likely number to appear first"
        ad = 3
    elif ua<ra and ua<sa and ua<ta and ua<qa and ua<va and ua<wa and ua<ea and ua<ya and ua<za:
        print "4 is the least likely number to appear first"
        ad = 4
    elif va<ra and va<sa and va<ta and va<ua and va<qa and va<wa and va<ea and va<ya and va<za:
        print "5 is the least likely number to appear first"
        ad = 5
    elif wa<ra and wa<sa and wa<ta and wa<ua and wa<va and wa<qa and wa<ea and wa<ya and wa<za:
        print "6 is the least likely number to appear first"
        ad = 6
    elif ea<ra and ea<sa and ea<ta and ea<ua and ea<va and ea<wa and ea<qa and ea<ya and ea<za:
        print "7 is the least likely number to appear first"
        ad = 7
    elif ya<ra and ya<sa and ya<ta and ya<ua and ya<va and ya<wa and ya<ea and ya<qa and ya<za:
        print "8 is the least likely number to appear first"
        ad = 8
    elif za>ra and za>sa and za>ta and za>ua and za>va and za>wa and za>ea and za>qa and za>ya:
        print "9 is the least likely number to appear first"
        ad = 9
    else:
        print "The first number is less likely to be a lower percentage number but we'll use the average"
        ad = ((((sum(lista)/5)**2)+da)/5)%10

    ##determining the least likely second number
    if qb<rb and qb<sb and qb<tb and qb<ub and qb<vb and qb<wb and qb<eb and qb<yb and qb<zb:
        print "0 is the least likely number to appear second"
        bd = 0
    elif rb<qb and rb<sb and rb<tb and rb<ub and rb<vb and rb<wb and rb<eb and rb<yb and rb<zb:
        print "1 is the least likely number to appear second"
        bd = 1
    elif sb<rb and sb<qb and sb<tb and sb<ub and sb<vb and sb<wb and sb<eb and sb<yb and sb<zb:
        print "2 is the least likely number to appear second"
        bd = 2
    elif tb<rb and tb<sb and tb<qb and tb<ub and tb<vb and tb<wb and tb<eb and tb<yb and tb<zb:
        print "3 is the least likely number to appear second"
        bd = 3
    elif ub<rb and ub<sb and ub<tb and ub<qb and ub<vb and ub<wb and ub<eb and ub<yb and ub<zb:
        print "4 is the least likely number to appear second"
        bd =4
    elif vb<rb and vb<sb and vb<tb and vb<ub and vb<qb and vb<wb and vb<eb and vb<yb and vb<zb:
        print "5 is the least likely number to appear second"
        bd = 5
    elif wb<rb and wb<sb and wb<tb and wb<ub and wb<vb and wb<qb and wb<eb and wb<yb and wb<zb:
        print "6 is the least likely number to appear second"
        bd = 6
    elif eb<rb and eb<sb and eb<tb and eb<ub and eb<vb and eb<wb and eb<qb and eb<yb and eb<zb:
        print "7 is the least likely number to appear second"
        bd = 7
    elif yb<rb and yb<sb and yb<tb and yb<ub and yb<vb and yb<wb and yb<eb and yb<qb and yb<zb:
        print "8 is the least likely number to appear second"
        bd = 8
    elif zb>rb and zb>sb and zb>tb and zb>ub and zb>vb and zb>wb and zb>eb and zb>qb and zb>yb:
        print "9 is the least likely number to appear second"
        bd = 9
    else:
        print "The second number is more likely to be a lower percentage number but we'll use the average"
        bd = ((((sum(listb)/5)**2)+db)/5)%10

    ##determinging the least likely third number
    if qc<rc and qc<sc and qc<tc and qc<uc and qc<vc and qc<wc and qc<ec and qc<yc and qc<zc:
        print "0 is the least likely number to appear third"
        cd = 0
    elif rc<qc and rc<sc and rc<tc and rc<uc and rc<vc and rc<wc and rc<ec and rc<yc and rc<zc:
        print "1 is the least likely number to appear third"
        cd = 1
    elif sc<rc and sc<qc and sc<tc and sc<uc and sc<vc and sc<wc and sc<ec and sc<yc and sc<zc:
        print "2 is the least likely number to appear third"
        cd = 2
    elif tc<rc and tc<sc and tc<qc and tc<uc and tc<vc and tc<wc and tc<ec and tc<yc and tc<zc:
        print "3 is the least likely number to appear third"
        cd = 3
    elif uc<rc and uc<sc and uc<tc and uc<qc and uc<vc and uc<wc and uc<ec and uc<yc and uc<zc:
        print "4 is the least likely number to appear third"
        cd = 4
    elif vc<rc and vc<sc and vc<tc and vc<uc and vc<qc and vc<wc and vc<ec and vc<yc and vc<zc:
        print "5 is the least likely number to appear third"
        cd = 5
    elif wc<rc and wc<sc and wc<tc and wc<uc and wc<vc and wc<qc and wc<ec and wc<yc and wc<zc:
        print "6 is the least likely number to appear third"
        cd = 6
    elif ec<rc and ec<sc and ec<tc and ec<uc and ec<vc and ec<wc and ec<qc and ec<yc and ec<zc:
        print "7 is the least likely number to appear third"
        cd = 7
    elif yc<rc and yc<sc and yc<tc and yc<uc and yc<vc and yc<wc and yc<ec and yc<qc and yc<zc:
        print "8 is the least likely number to appear third"
        cd = 8
    elif zc<rc and zc<sc and zc<tc and zc<uc and zc<vc and zc<wc and zc<ec and zc<qc and zc<yc:
        print "9 is the least likely number to appear third"
        cd = 9
    else:
        print "The third number is less likely to be a lower percentage number but we'll use the average"
        cd = ((((sum(listc)/5)**2)+dc)/5)%10
        
    print "%d,%d,%d most likely" % (am,bm,cm)
    print "%d,%d,%d is the least likely" % (ad,bd,cd)
    print "%d,%d,%d is another likely number using the pi theory" % ((((sum(lista)/5)+(3.141592653**.5))%10),(((sum(listb)/5)+(3.141592653**.5))%10),(((sum(listc)/5)+(3.141592653**.5))%10))
    print "%d,%d,%d is another likely number using the pi theory" % ((((sum(lista)/5)+(3.141592653))%10),(((sum(listb)/5)+(3.141592653))%10),(((sum(listc)/5)+(3.141592653))%10))
    print "%d,%d,%d is another likely number using the pi theory" % ((((sum(lista)/5)+(3.141592653**2))%10),(((sum(listb)/5)+(3.141592653**2))%10),(((sum(listc)/5)+(3.141592653**2))%10))
    
    if gp>40:
        print "A double is very unlikely."   
    raw_input("Done!!")    
            
lottoroll()
    
