
def get_nte(text):
    """Get name exchange ticker"""
    all_data = []
    CONAME = ""
    CROSS_REF = ""
    TICKER = ""
    EXCHANGE = ""
    indices_t = [i for i, elem in enumerate(text) if 'TICKER-SYMBOL:' in elem]
    indices_e = [i for i, elem in enumerate(text) if 'EXCHANGE:' in elem]
    indices_c = [i for i, elem in enumerate(text) if 'CROSS-REFERENCE:' in elem]
    if indices_c:
        CONAME = text[indices_c[0]-1]
        CROSS_REF = text[indices_c[0]].split(":")[1]
    if indices_t and not indices_c:
        CONAME = text[indices_t[0]- 1]
    if indices_t:
        temp = text[indices_t[0]].split()
        TICKER = temp[temp.index("TICKER-SYMBOL:")+1]
        EXCHANGE = temp[temp.index("EXCHANGE:") + 1]
    if not indices_t and indices_e:
        temp = text[indices_e[0]].split()
        EXCHANGE = temp[temp.index("EXCHANGE:") + 1]
    if CONAME == "":
        terms = [" CORP", " INC"]
        f = [i for i in text[3:] if any(r in i for r in terms)]
        try:
            CONAME = f[0][0:f[0].index("INC")-1]+" INC"
        except:
            CONAME = f[0][0:f[0].index("CORP")-1]+" CORP"
        print(text)
        print(CONAME, CROSS_REF, TICKER, EXCHANGE)
    all_data = [CONAME, CROSS_REF, TICKER, EXCHANGE]
    return all_data