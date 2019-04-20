import os

#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\All'
directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\Specs\10K'
path = os.path.abspath(directory)
print(os.listdir(path))

def folder_loop(path):
    """Loops through contents of a folder
    saves file path"""
    req_paths = []
    for path, dirs, files in os.walk(path):
        req_paths.extend([os.path.join(path, i) for i in files])
    return req_paths


req_paths = folder_loop(path)
print(req_paths)
for i in req_paths:
    print(i)

def getText(para, par_top, option = ""):
    """Function gathers text from text files for later parting"""
    #Gather Text From Beginning of Document Until Table of Contents
    fullText = []
    aicpa_count = 29 #number of line to check at start of document
    if option is "check":
        aicpa_count = 10
    if option is 'seconline':
        aicpa_count = 40
    for i in par_top:
        newText = []
        for j in range(i, i+aicpa_count):
           (newText.append(para[j].text.strip()) if para[j].text.strip() != '' else None)
        fullText.append(newText)
    return fullText

def det_db(file):
    """Determines if files fro Sec Online Old or New"""
    #Gather Text From Beginning of Document Until Table of Contents
    #Old After # of # Docs always has:   [*Summary]             COPYRIGHT 1990 SEC ONLINE, INC.
    #New: after # of $ Docs always gas: SEC Online Database
    ttofind_1 = ["[*Summary]             COPYRIGHT 1988 SEC ONLINE, INC.",
                 "[*Summary]             COPYRIGHT 1989 SEC ONLINE, INC.",
                 "[*Summary]             COPYRIGHT 1990 SEC ONLINE, INC.",
                 "[*Summary]             COPYRIGHT 1991 SEC ONLINE, INC.",
                 "[*Summary]             COPYRIGHT 1992 SEC ONLINE, INC.",
                 "[*Summary]             COPYRIGHT 1993 SEC ONLINE, INC.",
                 "[*Summary]             COPYRIGHT 1994 SEC ONLINE, INC.",
                 "[*Summary]             COPYRIGHT 1995 SEC ONLINE, INC.",
                 ]
    ttofind_2 = ["COPYRIGHT 1988 SEC ONLINE, INC.",
                 "COPYRIGHT 1989 SEC ONLINE, INC.",
                 "COPYRIGHT 1990 SEC ONLINE, INC.",
                 "COPYRIGHT 1991 SEC ONLINE, INC.",
                 "COPYRIGHT 1992 SEC ONLINE, INC.",
                 "COPYRIGHT 1993 SEC ONLINE, INC.",
                 "COPYRIGHT 1994 SEC ONLINE, INC.",
                 "COPYRIGHT 1995 SEC ONLINE, INC.",
                 ]
    fullText = []
    aicpa_count = 29 #number of line to check at start of document
    if option is "check":
        aicpa_count = 10
    if option is 'seconline':
        aicpa_count = 40
    for i in par_top:
        newText = []
        for j in range(i, i+aicpa_count):
           (newText.append(para[j].text.strip()) if para[j].text.strip() != '' else None)
        fullText.append(newText)
    return fullText


def main(path):
    """Main Function"""
    # First determine file type New or Old Sec
    # Second, gather text for later parsing
    # Two determine filing type: 10K, AR, 10Q, Proxy
    # Three Collect Information Equal to All 4
    # Collect Specific informaiton
    path = os.path.abspath(path)
    #names = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count',
              #'start_paragraph', 'Company Name','SIC', 'DATE', 'TICKER']]
    #names2 = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count', 'start_paragraph',
               #'Document Type', 'Company Name', 'Filing Date','Document Date',
               #'TICKER', 'Exchange','Incorporation', 'CUSIP', 'SIC']]
    #names3 = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count']]
    #names4 = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count']]
    names = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count', 'start_line', 'D_base']]
    names2 = [['Filing_type', 'Filing-date', 'Document-Date', 'Ticker', 'Exchange']]
    names_10K = [['Icorp', 'Cusip', 'DUNS', 'IRS', 'SIC', 'FYE']]
    names_10Q = [['Icorp', 'Cusip', 'DUNS', 'IRS', 'SIC', 'FYE']]
    names_AR = [['Icorp', 'Cusip', 'DUNS', 'IRS', 'SIC', 'FYE']]
    names_PX = [['Icorp', 'Cusip', 'DUNS', 'IRS', 'SIC', 'FYE']]

#fipath(0, directory, 0)
