####Master File to Read All SEC Online Files and Organize Data

#Take master files from Directories, read individual files and determine type of file
import os, time, compfuncs
directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\All'
dir_ss = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\All\ss_info'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\Specs\10K'
directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\small'
directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\smaller'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\Specs\AR'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\ALLN'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\single'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\check'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\All\1992 - New'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\All\1994'
path = os.path.abspath(directory)
path_ss = os.path.abspath(dir_ss)

terms_old_1 = ["[*Summary]             COPYRIGHT 1987 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1988 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1989 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1990 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1991 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1992 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1993 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1994 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1995 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1996 SEC ONLINE, INC.",
               "*Summary            COPYRIGHT 1987 SEC ONLINE, INC.",
               "*Summary            COPYRIGHT 1988 SEC ONLINE, INC.",
               "*Summary            COPYRIGHT 1989 SEC ONLINE, INC.",
               "*Summary            COPYRIGHT 1990 SEC ONLINE, INC.",
               "*Summary            COPYRIGHT 1991 SEC ONLINE, INC.",
               "*Summary            COPYRIGHT 1992 SEC ONLINE, INC.",
               "*Summary            COPYRIGHT 1993 SEC ONLINE, INC.",
               "*Summary            COPYRIGHT 1994 SEC ONLINE, INC.",
               "*Summary            COPYRIGHT 1995 SEC ONLINE, INC.",
             ]
terms_old_2 = ["COPYRIGHT 1987 SEC ONLINE, INC.",
               "COPYRIGHT 1988 SEC ONLINE, INC.",
               "COPYRIGHT 1989 SEC ONLINE, INC.",
               "COPYRIGHT 1990 SEC ONLINE, INC.",
               "COPYRIGHT 1991 SEC ONLINE, INC.",
               "COPYRIGHT 1992 SEC ONLINE, INC.",
               "COPYRIGHT 1993 SEC ONLINE, INC.",
               "COPYRIGHT 1994 SEC ONLINE, INC.",
               "COPYRIGHT 1995 SEC ONLINE, INC."]

terms_old_3 = ["COPYRIGHT 1987 @ SEC ONLINE, INC.",
               "COPYRIGHT 1988 @ SEC ONLINE, INC.",
               "COPYRIGHT 1989 @ SEC ONLINE, INC.",
               "COPYRIGHT 1990 @ SEC ONLINE, INC.",
               "COPYRIGHT 1991 @ SEC ONLINE, INC.",
               "COPYRIGHT 1992 @ SEC ONLINE, INC.",
               "COPYRIGHT 1993 @ SEC ONLINE, INC.",
               "COPYRIGHT 1994 @ SEC ONLINE, INC.",
               "COPYRIGHT 1995 @ SEC ONLINE, INC."]
terms_old = terms_old_1 + terms_old_2 + terms_old_3
print(terms_old)
terms_new_1 = ["SEC Online Database"]
terms_not_in = "Source: SEC Online Database*"
print(terms_not_in)
start_docu = ["of", "DOCUMENTS"]



def folder_loop(path):
    """Loops through contents of a folder
    saves file path, keep only text files"""
    req_paths = []
    for path, dirs, files in os.walk(path):
        req_paths.extend([os.path.join(path, i) for i in files])
    req_paths_doc = [i for i in req_paths if os.path.splitext(i)[1] == ".doc" or os.path.splitext(i)[1] == ".DOC"]
    req_paths = [i for i in req_paths if os.path.splitext(i)[1] == ".txt" or os.path.splitext(i)[1] == ".TXT"]
    return req_paths, req_paths_doc


def check_type(a,b,c):
    """Get filing and doc date for SEC_OLD"""
    doc_type = ["10-K", "10-Q", "Annual Report to Stockholders", "Proxy Statement", "PROXY", "20-F", "10K", "ANNUAL REPORTS"]
    doco_type = ""
    doco_type_found = False
    error_type = 1
    or_a = a
    a = a.split(";")
    amm = ""
    if len(a) > 1:
        if "Amendment" in a[1].strip():
            amm = a[1].strip()
    if "10-K" in a or "10K" in b[-1]:
        doco_type = "10K"
        doco_type_found = True
    if "10-Q" in a:
        doco_type = "10Q"
        doco_type_found = True
    if "Proxy Statement" or "PROXY" in a:
        doco_type = "Proxy"
        doco_type_found = True
    if "Annual Report to Stockholders" in a or "ANNUAL REPORTS" in b[-1]:
        doco_type = "AR"
        doco_type_found = True
    if "20-F" in a:
        doco_type = "20F"
        doco_type_found = True
    if "FILING-DATE:" in or_a:
        error_type = 2
    if not any(i in or_a for i in doc_type) and not doco_type_found:
        #print(a)
        #print("Something happened")
        #print(c, b)
        #print(b[-1])
        error_type = 3
        doco_type = "UK"

        time.sleep(10)
    return [doco_type, amm], error_type


def get_dates(a,b):
    """Get filing and doc date for SEC_OLD"""
    #Looks for lines with filing and document date
    errors = 0
    #print(b)
    if 'FILING-DATE:' in a:
        errors = 0
        a = a.split()
    if 'FILING-DATE:' not in a:
        #print(b)
        #print("Some trouble")
        #time.sleep(10)
        for i in b:
            if 'FILING-DATE:' in i:
                a = i
                a = a.split()
                break
            else:
                file_date, doc_date = None, None
    if len(a) > 4:
        errors = 1
        print(a)
    if errors == 0:
        if a[0] == "FILING-DATE:":
            file_date = a[1]
        if a[2] == "DOCUMENT-DATE:":
            doc_date = a[3]
    if errors == 1:
        file_date = a[a.index("FILING-DATE:") + 1]
        doc_date = a[a.index("DOCUMENT-DATE:") + 1]
        time.sleep(10)
    return [file_date, doc_date]

def get_rest_data(text):
    """Get rest of the data in the following order:
    CONAME, CROSSREFERENCE, TICKER, EXCHANGE, INCORP, CUSIP
    COMMISION NO, IRS-ID, SIC Codes, """
    data_prem = compfuncs.get_nte(text)
    return None

def col_data(text,b,c):
    """Same but to call functions to collect new data"""
    #a is the text
    #b is the file name for debugging
    #c is doc info
    #print(text)
    d = list(c) # creates copy to extend
    names2 = [['Filing_type', 'Filing_type_a', 'Filing-date', 'Document-Date', 'CONAME','CROSS_REF','Ticker','Exchange',
               'CUSIP', 'IRS-ID', 'SIC_P','SIC_A', 'FYE', 'AUDITOR','STOCK-AGENT','COUNSEL']]
    data_list = ["","","", "","","","","","","","","","","","",""]
    ttlf = [['FILING-DATE:', 'DOCUMENT-DATE:', 'Document-Date', 'TICKER-SYMBOL:', 'EXCHANGE:',
             "INCORPORATION:", "COMPANY-NUMBER:","CUSIP NUMBER:","COMMISSION FILE NO.:","IRS-ID:",
             "SIC: SIC-CODES:","SIC: PRIMARY SIC:", "PRIMARY SIC:","INDUSTRY-CLASS:", ]]
    data_list_1, error_type = check_type(text[4], text, b)
    #print(data_list_1)
    if error_type == 1:
        data_list_2 = get_dates(text[6],text) #doc and fiel date
    if error_type == 2:
        data_list_2 = get_dates(text[4],text) #doc and fiel date
    #print(data_list_2)
    data_list_3 = [CONAME, CROSS_REF, TICKER, EXCHANGE] = compfuncs.get_nte(text)
    #print(data_list_3)
    data_list_4 = [INCORP, CUSIP, COMMNO, IRS, P_SIC, IND_CLASS, FYE, AUDITOR] = compfuncs.get_iconumbers(text)
    data_list_1.extend(data_list_2)
    data_list_1.extend(data_list_3)
    data_list_1.extend(data_list_4)
    d.extend(data_list_1)
    return d

def col_data_new(text,b,c):
    #a is the text
    #b is the file name for debugging
    #c is doc info
    d = list(c) # creates copy to extend
    compfuncs.get_new_all(text)
    return d


def main(path):
    """Main Function"""
    # Takes path from each file collect starting text for each document in text
    # Pass text to different parsing functions to collect data
    path = os.path.abspath(path)
    print(path)
    names = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count', 'start_line', 'D_base']]
    names_old = [['Filing_type', 'Filing-date', 'Document-Date', 'CONAME', 'CUSIP','Ticker', 'IRS-ID',
               'SIC_P','SIC_A', 'FYE', 'Exchange', 'AUDITOR','STOCK-AGENT','COUNSEL']]
    data_list = ["","","","","","","","","","","","","",""]
    ttlf = [['FILING-DATE:', 'DOCUMENT-DATE:', 'Document-Date', 'TICKER-SYMBOL:', 'EXCHANGE:',
             "INCORPORATION:", "COMPANY-NUMBER:","CUSIP NUMBER:","COMMISSION FILE NO.:","IRS-ID:",
             "SIC: SIC-CODES:","SIC: PRIMARY SIC:", "PRIMARY SIC:","INDUSTRY-CLASS:", ]]

    names_old = [['Filing_type', 'Filing_type_a', 'Filing-date', 'Document-Date',
               'CONAME','CROSS_REF','Ticker','Exchange', 'CUSIP', 'IRS-ID',
               'SIC_P', 'FYE', 'AUDITOR']]
    doct_found = 0
    req_paths, req_paths_doc = folder_loop(path) #creates lists of paths
    #print(req_paths_doc)
    #for filename in os.listdir(req_paths):
    for filename in req_paths:
        doct_found = 0
        #fhand = open(os.path.abspath(directory + "\\" + filename))
        #fhand = open(os.path.abspath(directory + "\\" + filename), encoding="utf8")
        fhand = open(filename, encoding="utf8")
        #fhand = open(filename)
        [start, end] = [0, 0]
        text = []
        doc_count = 0
        line_count = 0
        doc_type_known = False
        doc_type = ''
        file_info = [filename, '', '']
        doc_info = [filename,'','','']
        doc_data = []
        start_docu = ["of", "DOCUMENTS"]

        for line in fhand:
            if not doc_type_known:
                if terms_new_1[0].lower() in line.lower() and line.strip() != "Source: SEC Online Database*":
                    doc_type_known = True
                    file_info[1] = "SEC_NEW"
                    doc_type = "SEC_NEW"
                if any(f.lower() in line.lower() for f in terms_old):
                    file_info[1] = "SEC_OLD"
                    doc_type = "SEC_OLD"
                    doc_type_known = True
            #print(line)
            #if all(f in line for f in start_docu):
                #print(line)
                #print(len(set(line.split()) - set(start_docu)))
            if all(f in line for f in start_docu):
                check = [word for word in line.strip().split() if word not in start_docu]
                if len(check) == 2 and all(s.isdigit for s in check):
                    #print("WEE HEEEEEEEEEEEERTEEEEEEEEEEEEEEEEE")
                    #print(line)
                    [start, end] = [1, 0]
                    text = []
                    doc_type_known = False
                    doc_count += 1
                    doc_info[2] = doc_count
                    doc_info[3] = line_count
                    # print(doc_info)
                    #doc_file_info.append([filename, doc_type, str(doc_count), str(line_count)])
                    # print(doc_file_info)


            #if all(f in line for f in start_docu) and len(set(line.split()) - set(start_docu)) is 2 \
                     #and all(s.isdigit for s in list(set(line.split())-set(start_docu))):
                #print("WEE HEEEEEEEEEEEERTEEEEEEEEEEEEEEEEE")
                #print(line)
                #print(time.sleep(5))
                #[start, end] = [1, 0]
                #text = []
                #doc_type_known = False
                #doc_count += 1
                #doc_info[2] = doc_count
                #doc_info[3] = line_count
                #print(doc_info)
                #doc_file_info.append([filename, doc_type, str(doc_count), str(line_count)])
                #print(doc_file_info)

            if doc_type == "SEC_OLD" and "TABLE OF CONTENTS" in line:
                if start == 1:
                    text.append(line.strip().replace('\xa0', ' '))
                    doc_info[1] = doc_type
                    #print(doc_info)
                    #print(text)
                    #print(text)
                    doc_data.append(col_data(text, filename, doc_info))
                    #doc_info.extend(col_data(text, filename, doc_info))
                [start, end] = [0, 1]
                doc_type_known = False
            if doc_type == "SEC_NEW" and "* * * * * * * * * * CONTENTS * * * * * * * * * *" in line:
                if start == 1:
                    text.append(line.strip().replace('\xa0', ' '))
                    doc_info[1] = doc_type
                    #print(doc_info)
                    #print(text)
                    col_data_new(text, filename, doc_info)
                    #doc_info.extend(col_data(text, filename, doc_info))
                [start, end] = [0, 1]
                doc_type_known = False
            if start == 1 and end == 0:
                text.append(line.strip().replace('\xa0',' '))
            line_count += 1
        #print(doc_data)
    return doc_data
print(path)
main(path)
