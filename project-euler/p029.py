def generate():
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            yield a ** b

print len(set(generate()))
