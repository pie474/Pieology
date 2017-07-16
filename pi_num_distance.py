__author__ = 'chinmay'

def pi_generate(num_dec):
    """
    generator to approximate pi to n decimals
    returns a single digit as character of pi each time iterated until num_dec generated
    this function is from http://www.daniweb.com/software-development/python/code/249177

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

"""
calculates and prints in a file distances between each type of digit(1, 2, 3, 4, 5, etc) for a certain # of digits of pi
for example, for 10 digits of pi:3.141592653 distances for 1 would be: 2, 2,...
"""

file = open("pi_distance.csv", "w")
#pi_str = ''.join(pi_generate(num_digits))
zero_dis, zero_diso, zero_diss, one_dis, one_diso, one_diss, two_dis, two_diso, two_diss, three_dis, three_diso, three_diss, four_dis, four_diso, four_diss, five_dis, five_diso, five_diss, six_dis, six_diso, six_diss, seven_dis, seven_diso, seven_diss, eight_dis, eight_diso, eight_diss, nine_dis, nine_diso, nine_diss = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
sum_0, count_0, sum_1, count_1, sum_2, count_2, sum_3, count_3, sum_4, count_4, sum_5, count_5, sum_6, count_6, sum_7, count_7, sum_8, count_8, sum_9, count_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
counter = 1
num_digits = 10000
for pidigit in pi_generate(num_digits):
    #print(pidigit),
    if (pidigit == "0"):
        zero_dis = counter
        zero_diss = str(zero_diss)+","+str(zero_dis - zero_diso)
        sum_0 = sum_0 + (zero_dis - zero_diso)
        zero_diso = zero_dis
        count_0 += 1
    if (pidigit == "1"):
        one_dis = counter
        one_diss = str(one_diss)+","+str(one_dis - one_diso)
        sum_1 = sum_1 + (one_dis - one_diso)
        one_diso = one_dis
        count_1 += 1
    if (pidigit == "2"):
        two_dis = counter
        two_diss = str(two_diss)+","+str(two_dis - two_diso)
        sum_2 = sum_2 + (two_dis - two_diso)
        two_diso = two_dis
        count_2 += 1
    if (pidigit == "3"):
        three_dis = counter
        three_diss = str(three_diss)+","+str(three_dis - three_diso)
        sum_3 = sum_3 + (three_dis - three_diso)
        three_diso = three_dis
        count_3 += 1
    if (pidigit == "4"):
        four_dis = counter
        four_diss = str(four_diss)+","+str(four_dis - four_diso)
        sum_4 = sum_4 + (four_dis - four_diso)
        four_diso = four_dis
        count_4 += 1
    if (pidigit == "5"):
        five_dis = counter
        five_diss = str(five_diss)+","+str(five_dis - five_diso)
        sum_5 = sum_5 + (five_dis - five_diso)
        five_diso = five_dis
        count_5 += 1
    if (pidigit == "6"):
        six_dis = counter
        six_diss = str(six_diss)+","+str(six_dis - six_diso)
        sum_6 = sum_6 + (six_dis - six_diso)
        six_diso = six_dis
        count_6 += 1
    if (pidigit == "7"):
        seven_dis = counter
        seven_diss = str(seven_diss)+","+str(seven_dis - seven_diso)
        sum_7 = sum_7 + (seven_dis - seven_diso)
        seven_diso = seven_dis
        count_7 += 1
    if (pidigit == "8"):
        eight_dis = counter
        eight_diss = str(eight_diss)+","+str(eight_dis - eight_diso)
        sum_8 = sum_8 + (eight_dis - eight_diso)
        eight_diso = eight_dis
        count_8 += 1
    if (pidigit == "9"):
        nine_dis = counter
        nine_diss = str(nine_diss)+","+str(nine_dis - nine_diso)
        sum_9 = sum_9 + (nine_dis - nine_diso)
        nine_diso = nine_dis
        count_9 += 1
    counter += 1
file.write("zero distances"+","+zero_diss+"\n")
file.write("one distances"+","+one_diss+"\n")
file.write("two distances"+","+two_diss+"\n")
file.write("three distances"+","+three_diss+"\n")
file.write("four distances"+","+four_diss+"\n")
file.write("five distances"+","+five_diss+"\n")
file.write("six distances"+","+six_diss+"\n")
file.write("seven distances"+","+seven_diss+"\n")
file.write("eight distances"+","+eight_diss+"\n")
file.write("nine distances"+","+nine_diss+"\n")


file.write("digit 0 dist average, "+str(float(sum_0) / count_0)+"\n")
file.write("digit 1 dist average, "+str(float(sum_1) / count_1)+"\n")
file.write("digit 2 dist average, "+str(float(sum_2) / count_2)+"\n")
file.write("digit 3 dist average, "+str(float(sum_3) / count_3)+"\n")
file.write("digit 4 dist average, "+str(float(sum_4) / count_4)+"\n")
file.write("digit 5 dist average, "+str(float(sum_5) / count_5)+"\n")
file.write("digit 6 dist average, "+str(float(sum_6) / count_6)+"\n")
file.write("digit 7 dist average, "+str(float(sum_7) / count_7)+"\n")
file.write("digit 8 dist average, "+str(float(sum_8) / count_8)+"\n")
file.write("digit 9 dist average, "+str(float(sum_9) / count_9)+"\n")
file.close()
exit()