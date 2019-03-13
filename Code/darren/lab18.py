#lab18.py
# Peaks and Valleys

#peak/valley finder

# def peakfinder(indata):
#     peaklist = []
#     for index in range(1, 20):
#         if indata[index] > indata[index - 1] and indata[index] > indata[index + 1]:
#             peaklist.append(index)
#     return peaklist
#
# def valleyfinder(indata):
#     valleylist = []
#     for index in range(1, 20):
#         if indata[index] < indata[index - 1] and indata[index] < indata[index + 1]:
#             valleylist.append(index)
#     return valleylist
#
# def peakvalleyfinder(indata):
#     pvlist = []
#     for index in range(1, 20):
#         if indata[index] < indata[index - 1] and indata[index] < indata[index + 1]:
#             pvlist.append(index)
#         if indata[index] > indata[index - 1] and indata[index] > indata[index + 1]:
#             pvlist.append(index)
#         else:
#             continue
#     return pvlist
#
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]
data = [1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 2, 1, 9, 9]
# pv = peakvalleyfinder(data)
# print(f"This chart has peaks and valleys at indices {pv}.")


#lake finder
def lakefinder(inlist):
    peaklist = []
    resultlist = []
    highestpeak = 0
    for index in range(len(inlist)):
        if index == 0:
            if inlist[index + 1] < inlist[index]:
                peaklist.append((index, inlist[index]))
                highestpeak = inlist[index]
        if index == len(inlist) -1:
            if inlist[index - 1] < inlist[index]:
                peaklist.append((index, inlist[index]))
                highestpeak = inlist[index]
        if index > 0 and index < len(inlist) - 1:
            if inlist[index - 1] < inlist[index] and inlist[index + 1] < inlist[index]:
                if inlist[index] >= highestpeak:
                    peaklist.append((index, inlist[index]))
                    highestpeak = inlist[index]
        if inlist[index] == highestpeak and (index, inlist[index]) not in peaklist:
            peaklist.append((index, inlist[index]))
    for index in range(len(peaklist)- 1):
        previousnum = 0
        if peaklist[index][1] != peaklist[index - 1][1]:
            previousnum = peaklist[index][1]
            resultlist.append((peaklist[index][0], peaklist[index + 1][0], peaklist[index][1]))
    print(peaklist)
    print(resultlist)
    print(previousnum)
peaks = lakefinder(data)
# print(peaks)

#water calculator
#random data version

# import random
# data = []
# prevnum = 0
# for index in range(21):
#     if index == 0:
#         randnum = random.randint(0,10)
#         prevnum = randnum
#         data.append(randnum)
#     else:
#         randnum = random.randint(prevnum - 1, prevnum + 1)
#         while randnum < 0:
#             randnum = random.randint(prevnum, prevnum + 1)
#         while randnum > 10:
#             randnum = random.randint(prevnum - 1, prevnum)
#         prevnum = randnum
#         data.append(randnum)
# print(data)

#water calculator
#preset data version

# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# data = [1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 2, 1, 9]
#
# watertotal = 0
# for boxrow in range(10):
#     lastpeak = 1
#     boxrowdif = 10 - boxrow
#     for boxcol in range(len(data)):
#         if data[boxcol] >= lastpeak:
#             lastpeak = data[boxcol]
#         if data[boxcol] > boxrowdif:
#             print('x', end=' ')
#         if data[boxcol] <= boxrowdif:
#             if data[boxcol - 1] > data[boxcol] and boxrowdif < lastpeak:
#                 print('0', end=' ')
#                 watertotal += 1
#             if data[boxcol - 1] < data[boxcol] and boxrowdif < lastpeak:
#                 print('0', end=' ')
#                 watertotal += 1
#             if data[boxcol - 1] == data[boxcol] and boxrowdif < lastpeak:
#                 print('0', end=' ')
#                 watertotal += 1
#             if boxcol < data[lastpeak]:
#                 print(' ', end=' ')
#             if boxcol > data[lastpeak] and boxrowdif >= lastpeak:
#                 print (' ', end=' ')
#             if boxcol == data[lastpeak]:
#                 print(' ', end=' ')
#     print()
# print(f"The water total is {watertotal}.")

#rough draft

# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# peaks = [7, 9]

# highestnum = 0
# highestnumlist = []
# for index in range(len(data)):
#     if data[index] >= highestnum:
#         highestnum = data[index]
#         highestnumlist.append(highestnum)
# print(highestnumlist)

# def lakefinder(datalist, peaklist):
#     outlist = []
#     for index in range(len(datalist)):
#         if datalist[index] in peaklist:
#             print(index)
#             print(datalist[index])
#             print(outlist)
#             outlist.append((index, datalist[index]))
#     return(outlist)
# lakes = lakefinder(data, peaks)
# print(lakes)
