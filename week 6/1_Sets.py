def uniquify(lis : list):
    return list(set(lis))

def count_specials(n : int):
    return list(set(range(3,n,3)) | set(range(7,n,7)) & set(range(1,n)))

