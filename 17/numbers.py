ONES = 'one two    three   four five six    seven   eight   nine'.split() 

TO_TWENTY = 'one two    three   four five six    seven   eight   nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()

TWENTY_TO_NINETY = 'twenty thirty forty fifty sixty seventy eighty ninety'.split()


def one_to_99():
    numbers = []
    for i in TO_TWENTY:
        numbers.append(i)

    for tens in TWENTY_TO_NINETY:
        numbers.append(tens)
        for one in ONES:
            numbers.append("%s-%s" % (tens, one))

    return numbers

if __name__ == "__main__":
    for i in one_to_99():
        print "%s, " % i,
    
    for hundred in ONES:
        print "%s hundred, " % hundred,
        for other in one_to_99():
            print "%s hundred and %s," % (hundred, other),

    print "one thousand",
