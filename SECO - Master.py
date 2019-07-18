####Master File to Read All SEC Online Files and Organize Data

#Take master files from Directories, read individual files and determine type of file
import os, time
directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\All'
dir_ss = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\All\ss_info'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\Specs\10K'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\small'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\Specs\AR'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\ALLN'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\single'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\check'
directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\All\1992 - New'
path = os.path.abspath(directory)
path_ss = os.path.abspath(dir_ss)

terms_old_1 = ["[*Summary]             COPYRIGHT 1988 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1989 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1990 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1991 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1992 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1993 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1994 SEC ONLINE, INC.",
               "[*Summary]             COPYRIGHT 1995 SEC ONLINE, INC.",
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
terms_new_1 = ["SEC Online Database"]
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


def check_type(a,b):
    doc_type = ["10-K", "10-Q", "Annual Report to Stockholders", "Proxy Statement", "PROXY", "20-F"]
    doco_type = ""
    error_type = 1
    or_a = a
    a = a.split(";")
    amm = ""
    if len(a)>1:
        if "Amendment" in a[1].strip():
            amm = a[1].strip()
    if "10-K" in a:
        doco_type = "10K"
        #print("10-K")
    if "10-Q" in a:
        doco_type = "10Q"
        #print("10-Q")
    if "Proxy Statement" or "PROXY" in a:
        doco_type = "Proxy"
        #print("Proxy")
    if "Annual Report to Stockholders" in a:
        doco_type = "AR"
        #print("AR")
    if "20-F" in a:
        doco_type = "20F"
        #print("20F")
    if not any(i in or_a for i in doc_type):
        print(a)
        print("Something happened")
        print(b)
        if "FILING-DATE:" in or_a:
            error_type = 2
            doco_type = "UK"
        time.sleep(10)
    return doco_type, amm, error_type


def get_dates(a,b):
    """Get filing and doc date"""
    errors = 0
    if 'FILING-DATE:' in a:
        errors = 0
        a = a.split()
    if 'FILING-DATE:' not in a:
        print(b)
        print("Some trouble")
        time.sleep(20)
        for i in b:
            if 'FILING-DATE:' in i:
                print("Found it")
                a = i
                a = a.split()
                print(a)
                time.sleep(10)
                break
            else:
                #print("Filing-date not found")
                file_date, doc_date = None, None

    #print(b)
    if errors == 0:
        if a[0] == "FILING-DATE:":
            file_date = a[1]
        if a[2] == "DOCUMENT-DATE:":
            doc_date = a[3]

    #elif b[6].split()[0] == "FILING-DATE:":
           #file_date = b[6].split()[0]
    #elif b[6].split()[0] == "FILING-DATE:":
            #file_date = b[6].split()[0]

    #file_date, doc_date = None, None
    #print("No dates found")
    #print(b)

    return file_date, doc_date


def col_data(a):
    #print(a[4])
    names2 = [['Filing_type', 'Filing_type_a', 'Filing-date', 'Document-Date', 'CONAME','CROSS-REF', 'CUSIP','Ticker', 'IRS-ID',
               'SIC_P','SIC_A', 'FYE', 'Exchange', 'AUDITOR','STOCK-AGENT','COUNSEL']]
    data_list = ["","","", "","","","","","","","","","","","",""]
    ttlf = [['FILING-DATE:', 'DOCUMENT-DATE:', 'Document-Date', 'TICKER-SYMBOL:', 'EXCHANGE:',
             "INCORPORATION:", "COMPANY-NUMBER:","CUSIP NUMBER:","COMMISSION FILE NO.:","IRS-ID:",
             "SIC: SIC-CODES:","SIC: PRIMARY SIC:", "PRIMARY SIC:","INDUSTRY-CLASS:", ]]
    data_list[0], data_list[1], error_type = check_type(a[4],a)
    if error_type == 1:
        data_list[2], data_list[3] = get_dates(a[6],a)
    if error_type == 2:
        data_list[2], data_list[3] = get_dates(a[4],a)
    #print(data_list)
    return data_list

def main(path):
    """Main Function"""
    # Takes path from each file collect starting text for each document in text
    # Pass text to different parsing functions to collect data
    path = os.path.abspath(path)
    print(path)
    names = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count', 'start_line', 'D_base']]
    names2 = [['Filing_type', 'Filing-date', 'Document-Date', 'CONAME', 'CUSIP','Ticker', 'IRS-ID',
               'SIC_P','SIC_A', 'FYE', 'Exchange', 'AUDITOR','STOCK-AGENT','COUNSEL']]
    data_list = ["","","","","","","","","","","","","",""]
    ttlf = [['FILING-DATE:', 'DOCUMENT-DATE:', 'Document-Date', 'TICKER-SYMBOL:', 'EXCHANGE:',
             "INCORPORATION:", "COMPANY-NUMBER:","CUSIP NUMBER:","COMMISSION FILE NO.:","IRS-ID:",
             "SIC: SIC-CODES:","SIC: PRIMARY SIC:", "PRIMARY SIC:","INDUSTRY-CLASS:", ]]
    doct_found = 0
    req_paths, req_paths_doc = folder_loop(path) #creates lists of paths
    #print(req_paths_doc)
    #for filename in os.listdir(req_paths):
    for filename in req_paths:
        #print("HERE")
        #print(filename)
        doct_found = 0
        #fhand = open(os.path.abspath(directory + "\\" + filename))
        #fhand = open(os.path.abspath(directory + "\\" + filename), encoding="utf8")
        fhand = open(filename, encoding="utf8")
        [start, end] = [0, 0]
        text = []
        doc_count = 0
        line_count = 0
        doc_type_known = False
        doc_type = ''
        file_info = [filename, '', '']
        doc_info = [filename, '', '']
        doc_file_info = []
        for line in fhand:
            if doc_count == 1 and not doc_type_known:
                print("Check DOC Type")
                print(filename)
                if terms_new_1[0].lower() in line.lower():
                    doc_type_known = True
                    file_info[1] = "SEC_NEW"
                    doc_type = "SEC_NEW"
                if any(f.lower() in line.lower() for f in terms_old):
                    file_info[1] = "SEC_OLD"
                    doc_type = "SEC_OLD"
                    doc_type_known = True
                print(doc_type)

            if all(f in line for f in start_docu) and len(set(line.split()) - set(start_docu)) is 2 \
                     and all(s.isdigit for s in list(set(line.split())-set(start_docu))):
                [start, end] = [1, 0]
                text = []
                doc_count += 1
                doc_info[1] = doc_count
                doc_info[2] = line_count
                doc_file_info.append([filename, doc_type, str(doc_count), str(line_count)])
            if doc_type == "SEC_NEW":
                None
                #print(doc_type)
                #time.sleep(5)
            if doc_type == "SEC_OLD" and "TABLE OF CONTENTS" in line:
                if start == 1:
                    #print(text)
                    col_data(text)
                [start, end] = [0, 1]
            if start == 1 and end == 0:
                #print(line)
                text.append(line.strip().replace('\xa0',' '))
            #print(text)
    return None
print(path)
main(path)
