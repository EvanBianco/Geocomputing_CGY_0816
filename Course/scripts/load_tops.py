def my_tops(filename ='data/B-41_tops.txt'):
    """
    Takes a file as input and returns a dictionary of tops
    f : a filename path
    """
    my_tops = {}
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('#') == 0:
                row = line.strip('\n')
                split_rows = row.split(',')
                name = split_rows[0]
                depth = float(split_rows[-1].strip())
                my_tops[name] = depth
    return my_tops