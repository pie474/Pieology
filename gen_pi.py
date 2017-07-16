__author__ = 'chinmay'

def pd(n, i):
    if(n==0): return "NaN"
    ex = float(n) / 10
    return str(((ex - i / ex)) * 100)

def pi_generate(num_dec):
    """
    generator to approximate pi to n decimals

    returns a single digit as character of pi each time iterated until num_dec generated
    # this function is by vegaseat http://www.daniweb.com/software-development/python/code/249177

    """
    #result = []
    n, q, r, t, k, m, x = 0, 1, 0, 1, 1, 3, 3
    while True:
        #print('q=%i,r=%i,t=%i'%(q,r,t))
        if 4 * q + r - t < m * t:
            yield str(m)
            #result.append(str(m))
            n += 1
            if n > num_dec: return #result
            q, r, t, k, m, x = (10 * q,
                                10 * (r - m * t),
                                t,
                                k,
                                (10 * (3 * q + r)) // t - 10 * m,
                                x)
        else:
            q, r, t, k, m, x = (q * k,
                                (2 * q + r) * x,
                                t * x,
                                k + 1,
                                (q * (7 * k + 2) + r * x)//(t * x),
                                x + 2)

file = open("pi_chart3.csv", "w")
file.write("# of digits in pi, 0s, 1s, 2s, 3s, 4s, 5s, 6s, 7s, 8s, 9s\n")
for num_digits in range(100, 1100, 100):
    zeros, ones, twos, threes, fours, fives, sixes, sevens, eights, nines = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for pidigit in pi_generate(num_digits):
        if (pidigit == "0"): zeros += 1
        if (pidigit == "1"): ones += 1
        if (pidigit == "2"): twos += 1
        if (pidigit == "3"): threes += 1
        if (pidigit == "4"): fours += 1
        if (pidigit == "5"): fives += 1
        if (pidigit == "6"): sixes += 1
        if (pidigit == "7"): sevens += 1
        if (pidigit == "8"): eights += 1
        if (pidigit == "9"): nines += 1
    print("\n")
    print("zeros:%i"% zeros)
    print("ones:%i"% ones)
    print("twos:%i"% twos)
    print("threes:%i"% threes)
    print("fours:%i"% fours)
    print("fives:%i"% fives)
    print("sixes:%i"% sixes)
    print("sevens:%i"% sevens)
    print("eights:%i"% eights)
    print("nines:%i"% nines)
    file.write(str(num_digits)+","+str(zeros)+","+str(ones)+","+str(twos)+","+str(threes)+","+str(fours)+","+str(fives)+","+str(sixes)+","+str(sevens)+","+str(eights)+","+str(nines)+"\n")
    file.write("percentages,"+pd(num_digits, zeros)+","+pd(num_digits, ones)+","+pd(num_digits, twos)+","+pd(num_digits, threes)+","+pd(num_digits, fours)+","+pd(num_digits, fives)+","+pd(num_digits, sixes)+","+pd(num_digits, sevens)+","+pd(num_digits, eights)+","+pd(num_digits, nines)+"\n")
file.close()
