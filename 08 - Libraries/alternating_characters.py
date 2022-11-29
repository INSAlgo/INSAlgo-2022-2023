def alternatingCharacters(s):
    match = re.findall(r"(A+|B+)",s)
    return(sum(list(map(len,match)))-len(match))
