from codecs import latin_1_decode


s1 = 'Type = ethernet'
s2 = 'bootproto = dhcp'

def split1(a,b):
    d = {}
    L1 = (a.split('='))
    L2 = (b.split('='))
    K,V = L1
    d[K] = V
    K,V = L2
    d[K] = V
    print(d)
    


split1(s1,s2)