def ones():
    return 'one two    three   four five six    seven   eight   nine'.split() 

def to_twenty():
    return 'one two    three   four five six    seven   eight   nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()

def twenty_to_ninety():
    return 'twenty thirty forty fifty sixty seventy eighty ninety'.split()


def one_to_99():
    numbers = []
    for i in to_twenty():
        numbers.append(i)

    for tens in twenty_to_ninety():
        numbers.append(tens)
        for one in ones():
            numbers.append("%s-%s" % (tens, one))

    return numbers

if __name__ == "__main__":
    for i in one_to_99():
        print "%s, " % i
    
    for hundred in ones():
        print "%s-hundred, " % hundred
        for other in one_to_99():
            print "%s-hundred and %s," % (hundred, other)

    print "one-thousand"
