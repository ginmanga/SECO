####Master File to Read All SEC Online Files and Organize Data

#Take master files from Directories, read individual files and determine type of file
import os
directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\All'
dir_ss = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\All\ss_info'
directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\Specs\10K'
directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\small'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\Specs\AR'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\ALLN'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\single'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\check'
path = os.path.abspath(directory)
path_ss = os.path.abspath(dir_ss)

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
start_docu = ["of", "DOCUMENTS"]
doc_type = ["10-K","10-Q", "Annual Report to Stockholders", "Proxy Statement"]

#for filename in os.listdir(path_ss):
    #print(filename)
#for filename in os.listdir(directory):
    #print(filename)
    #fhand = open(os.path.abspath(directory+"\\"+filename), encoding="utf8")
    #fhand = open(os.path.abspath(directory + "\\" + filename))
    #for line in fhand:
       #print(line)


#def tenk(AA):
    #"""Handles data collection in old 10K files"""
def find_doc_type(text):
    if any(t in line for t in doc_type) and doct_found == 0:
        print(line)
        if line.strip() == "10-K":
            data_list[0] = "10K"
        if line.strip() == "10-Q":
            data_list[0] = "10Q"
        if line.strip() == "Proxy Statement":
            data_list[0] = "Proxy"
        if line.strip() == "Annual Report to Stockholders":
            data_list[0] = "AR"
        doct_found = 1

def col_data(a):
    print(a[4])
def main(path):
    """Main Function"""
    # Takes path from each file collect starting text for each document in text
    # Pass text to different parsing functions to collect data
    path = os.path.abspath(path)
    print(path)
    #names = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count',
              #'start_paragraph', 'Company Name','SIC', 'DATE', 'TICKER']]
    #names2 = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count', 'start_paragraph',
               #'Document Type', 'Company Name', 'Filing Date','Document Date',
               #'TICKER', 'Exchange','Incorporation', 'CUSIP', 'SIC']]
    #names3 = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count']]
    #names4 = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count']]
    names = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count', 'start_line', 'D_base']]
    names2 = [['Filing_type', 'Filing-date', 'Document-Date', 'CONAME', 'CUSIP','Ticker', 'IRS-ID',
               'SIC_P','SIC_A', 'FYE', 'Exchange', 'AUDITOR','STOCK-AGENT','COUNSEL']]
    data_list = ["","","","","","","","","","","","","",""]
    ttlf = [['FILING-DATE:', 'DOCUMENT-DATE:', 'Document-Date', 'TICKER-SYMBOL:', 'EXCHANGE:',
             "INCORPORATION:", "COMPANY-NUMBER:","CUSIP NUMBER:","COMMISSION FILE NO.:","IRS-ID:",
             "SIC: SIC-CODES:","SIC: PRIMARY SIC:", "PRIMARY SIC:","INDUSTRY-CLASS:", ]]
    doct_found = 0


    for filename in os.listdir(directory):
        print(filename)
        doct_found = 0
        #fhand = open(os.path.abspath(directory + "\\" + filename))
        fhand = open(os.path.abspath(directory + "\\" + filename), encoding="utf8")
        [start, end] = [0, 0]
        text = []
        for line in fhand:
            if all(f in line for f in start_docu) and len(set(line.split()) - set(start_docu)) is 2 \
                     and all(s.isdigit for s in list(set(line.split())-set(start_docu))):
                [start, end] = [1, 0]
                text = []
            if "TABLE OF CONTENTS" in line:
                if start == 1:
                    print(text)
                    col_data(text)
                [start, end] = [0, 1]
            if start == 1 and end == 0:
                #print(line)
                text.append(line.strip().replace('\xa0',' '))
            #print(text)




    return None
main(path)

def det_db(file):
    """Determines if files fro Sec Online Old or New"""
    #Gather Text From Beginning of Document Until Table of Contents
    #Old After # of # Docs always has:   [*Summary]             COPYRIGHT 1990 SEC ONLINE, INC.
    #New: after # of $ Docs always gas: SEC Online Databas

    fhand = open(file)
    for i in fhand:
        print("LINE")
        print(i)
    fullText = []
    return fullText