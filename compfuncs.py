import re, time, os

def write_file(path_file, data, first):
    """Writes all data to file"""
    #first tells if it writtes or appends
    print(data)
    path_to_2 = os.path.join(path_file, 'id_file_data.txt')
    #with open(path_to_1,'w') as file:
        #file.writelines('\t'.join(i) + '\n' for i in data[0])
    #file.close()
    with open(path_to_2, first) as file:
        file.writelines('\t'.join(i) + '\n' for i in data)
    file.close()

def convert_filing_type(a):
    #print(a)
    doco_type = ""
    if a == "10-K":
        doco_type = "10K"
    if a == "10-Q":
        doco_type = "10Q"
    if a in ["Annual Reports to Shareholders", "Annual Reports to Shareholders"]:
        doco_type = "AR"
    if a == "20-F":
        doco_type = "20F"
    if a == "10-F":
        doco_type = "10F"
    if a == "Proxy Statement":
        doco_type = "Proxy"
    return doco_type


def get_new_all(text):
    filing_type = ""
    filing_type_a = ""
    CONAME = ""
    CROSS_REF = ""
    filing_date = ''
    document_date = ''
    ticker = ''
    exchange = ''
    CUSIP = ""
    SIC_CODES = ""
    COMMNO = ""
    IRS_ID = ""
    FYE = ""
    AUDITOR = ""
    terms = ['EXHIBIT TYPE:','FILING DATE:','REPORT PERIOD:','CONAME','TICKER: TICKER-SYMBOL:','EXCHANGE:', 'SIC CODES:']
    filings_terms = ["10-K", "10-Q", "Annual Report to Stockholders", "Proxy Statement", "PROXY", "20-F",
                     "10K", "10Q,""ANNUAL REPORTS","Annual Reports to Shareholders", "10-F"]
    indices_t = [i for i, elem in enumerate(text) if "SIC CODES:" in elem]
    names_old = [['filing_type', 'filing_type_a', 'filing_date', 'document_date',
               'CONAME','CROSS_REF','ticker','exchange', 'CUSIP', 'IRS_ID',
               'SIC_P', 'FYE', 'AUDITOR']]

    CONAME = text[[i for i, elem in enumerate(text) if "SEC Online Database" in elem][0]+2]

    try:
        filing_type = convert_filing_type([i.split(":")[1].strip() for i in text if 'EXHIBIT TYPE:' in i][0])

    except:
        filing_type = convert_filing_type(next((i for i in text if i in filings_terms), "Not found"))
        if filing_type == "Not found":
            print(text)
            time.sleep(30)
    try:
        filing_date = [i.split(":")[1].strip() for i in text if 'FILING DATE:' in i][0]

    except:
        filing_date = text[[i for i, elem in enumerate(text) if "DOCUMENT-DATE:" in elem][0] + 2]

    try:
        document_date = [i.split(":")[1].strip() for i in text if 'REPORT PERIOD:' in i][0]
    except:
        document_date = [i.split(":")[1].strip() for i in text if 'DOCUMENT-DATE:' in i][0]

    ticker = [i.split("TICKER-SYMBOL:")[1].strip() for i in text if 'TICKER: TICKER-SYMBOL:' in i][0]
    exchange = [i.split(":")[1].strip() for i in text if 'EXCHANGE:' in i][0]
    try:
        SIC_CODES = text[[i for i, elem in enumerate(text) if "SIC CODES:" in elem][0]+1].split(',')[0]
    except:
        None
    if not filing_date:
        print(text)
        time.sleep(10)
    return [filing_type,filing_type_a, filing_date, document_date, CONAME, CROSS_REF,
            ticker, exchange, CUSIP, COMMNO,IRS_ID,SIC_CODES, FYE, AUDITOR]


def get_nte(text):
    """Get name exchange ticker"""
    all_data = []
    CONAME = ""
    CROSS_REF = ""
    TICKER = ""
    EXCHANGE = ""
    text = [re.sub("��", "", i) for i in text]
    indices_t = [i for i, elem in enumerate(text) if 'TICKER-SYMBOL:' in elem]
    indices_e = [i for i, elem in enumerate(text) if 'EXCHANGE:' in elem]
    indices_c = [i for i, elem in enumerate(text) if 'CROSS-REFERENCE:' in elem]
    indices_incorp = [i for i, elem in enumerate(text) if 'INCORPORATION:' in elem]
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
        #print(text)
        #print(CONAME, CROSS_REF, TICKER, EXCHANGE)
    #all_data = [CONAME, CROSS_REF, TICKER, EXCHANGE]
    return [CONAME, CROSS_REF, TICKER, EXCHANGE]

def get_iconumbers(text):
    """INCORP AND COMPANY NUMBERS"""
    all_data = []
    INCORP = ""
    CUSIP = ""
    COMMNO = ""
    IRS = ""
    IND_CLASS = "" #not collected
    FYE = ""
    AUDITOR = ""
    P_SIC = ""
    A_SIC = ""
    text = [re.sub("��", "", i) for i in text]
    indices = []
    terms = ['INCORPORATION:','CUSIP NUMBER:','COMMISSION FILE NO.:','IRS-ID:', 'INDUSTRY-CLASS:','FYE:',
             'AUDITOR:' ]
    #indices_incorp = [i for i, elem in enumerate(text) if 'INCORPORATION:' in elem]
    #indices_CUSIP = [i for i, elem in enumerate(text) if 'CUSIP NUMBER:' in elem]
    #indices_COMNO = [i for i, elem in enumerate(text) if 'COMMISSION FILE NO.:' in elem]
    #indices_IRS = [i for i, elem in enumerate(text) if 'IRS-ID:' in elem]
    #indices_IND_CLASS = [i for i, elem in enumerate(text) if 'INDUSTRY-CLASS:' in elem]
    #indices_FYE = [i for i, elem in enumerate(text) if 'FYE:' in elem]
    #indices_AUDITOR = [i for i, elem in enumerate(text) if 'AUDITOR:' in elem]

    try:
        INCORP = [i.split(":")[1].strip() for i in text if 'INCORPORATION:' in i][0]
    except:
        INCORP = ""
    try:
        temp = [i for i in text if 'CUSIP NUMBER:' in i][0].split(":")
        CUSIP = temp[[i.strip() for i in temp].index('CUSIP NUMBER')+1]
    except:
        None
    try:
        temp = [i for i in text if 'COMMISSION FILE NO.:' in i][0].split(":")
        COMMNO = temp[[i.strip() for i in temp].index('COMMISSION FILE NO.')+1]
    except:
        None
    try:
        temp = [i for i in text if 'IRS-ID:' in i][0].split(":")
        IRS = temp[[i.strip() for i in temp].index('IRS-ID')+1]
    except:
        None
    try:
        temp = [i for i in text if 'FYE:' in i][0].split(":")
        FYE = temp[[i.strip() for i in temp].index('FYE')+1].strip()
    except:
        None
    try:
        temp = [i for i in text if 'AUDITOR:' in i][0].split(":")
        AUDITOR = temp[[i.strip() for i in temp].index('AUDITOR')+1]
    except:
        None
    try:
        temp = [i for i in text if 'SIC:' in i][0].split(":")
        temp1 = [i for i in text if 'PRIMARY SIC:' in i][0].split(":")
        if temp == temp1:
            A_SIC = P_SIC = temp[[i.strip() for i in temp].index('PRIMARY SIC') + 1].strip()
        if temp != temp1:
            P_SIC = temp1[[i.strip() for i in temp1].index('PRIMARY SIC') + 1].strip()
            A_SIC = temp[[i.strip() for i in temp].index('SIC-CODES') + 1:].strip()
    except:
        None
    #return [INCORP, CUSIP, COMMNO, IRS, P_SIC, IND_CLASS, FYE, AUDITOR]
    return [INCORP, CUSIP, COMMNO, IRS, P_SIC, FYE, AUDITOR]