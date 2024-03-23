def factor(num,factors):
    if num:
        return 1
    else:
        return factors.append(num)+factors.append(factor(num-1))