
def calc_weight(data, x_grade):
    res = []
    for i in range(len(data)):
        x = 0
        y = 0
        z = 0
        k = 0
        if 'math' in data[i]:
            x+=1
            y+=0.8
            z+=0.05
            k+=1
        if 'phis' in data[i]:
            x+=0.7
            y+=1
            z+=0.3
            k+=1
        if 'lgeb' in data[i]:
            x+=1
            y+=0.5
            z+=0.05
            k+=1
        if 'calc' in data[i]:
            x+=1
            y+=0.6
            z+=0.01
            k+=1
        if 'metr' in data[i]:
            x+=1
            y+=0.6
            z+=0.1
            k+=1
        if 'arch' in data[i]:
            x+=0.3
            y+=0.8
            z+=0.5
            k+=1
        if 'art' in data[i]:
            x+=0.1
            y+=0.01
            z+=1
            k+=1
        if 'asrt' in data[i]:
            x+=0.9
            y+=1
            z+=0.7
            k+=1
        if 'bio' in data[i]:
            x+=0.5
            y+=0.8
            z+=0.5
            k+=1
        if 'botan' in data[i]:
            x+=0.4
            y+=0.8
            z+=0.7
            k+=1
        if 'chem' in data[i]:
            x+=0.4
            y+=0.9
            z+=0.4
            k+=1
        if 'comp' in data[i]:
            x+=1
            y+=0.5
            z+=0.2
            k+=1
        if 'dram' in data[i]:
            x+=0
            y+=0.2
            z+=1
            k+=1
        if 'draw' in data[i]:
            x+=0.1
            y+=0.2
            z+=1
            k+=1
        if 'ecom' in data[i]:
            x+=0.8
            y+=0.3
            z+=0.8
            k+=1
        if 'lang' in data[i]:
            x+=0.01
            y+=0.1
            z+=1
            k+=1
        if 'engl' in data[i]:
            x+=0.05
            y+=0.07
            z+=1
            k+=1
        if 'fren' in data[i]:
            x+=0.05
            y+=0.2
            z+=1
            k+=1
        if 'geog' in data[i]:
            x+=0.4
            y+=0.8
            z+=0.9
            k+=1
        if 'geol' in data[i]:
            x+=0.4
            y+=0.7
            z+=0.9
            k+=1
        if 'gym' in data[i]:
            x+=0
            y+=0.05
            z+=1
            k+=1
        if 'hist' in data[i]:
            x+=0.05
            y+=0.1
            z+=1
            k+=1
        if 'heal' in data[i]:
            x+=0.1
            y+=0.5
            z+=1
            k+=1
        if 'lit' in data[i]:
            x+=0.01
            y+=0.1
            z+=1
            k+=1
        if 'psyc' in data[i]:
            x+=0.1
            y+=0.4
            z+=1
            k+=1
        if 'read' in data[i]:
            x+=0
            y+=0.1
            z+=1
            k+=1
        if 'sing' in data[i]:
            x+=0
            y+=0.02
            z+=1
            k+=1
        if 'writ' in data[i]:
            x+=0.01
            y+=0.3
            z+=1
            k+=1
        if k==0:
            k+=1
        x = ((x_grade[i]+1) * (x+1)) / k
        y = ((x_grade[i]+1) * (y+1)) / k
        z = ((x_grade[i]+1) * (z+1)) / k
        res.append((x, y, z))

    return res


def ml_alg(data):
    return calc_weight(data['subject'], data['grade'])
