import re
import os
import codecs

input_name = os.getcwd()+'\\quiz.txt'
tmp_name = os.getcwd()+'\\nquiz.txt'
final_name = os.getcwd()+'\\aquiz.txt'


with codecs.open(input_name, 'r', encoding='utf-8') as fi,  codecs.open(tmp_name, 'w', encoding='utf-8') as fo:

    for line in fi:

        text = line
        regex = re.compile(r'^\d+.')
        matchobj = regex.search(text)
        blank = text.strip()
        headex = re.compile('\d과목\s:')
        headobj = headex.search(text)
        if headobj :
            text=""
        elif matchobj:
            fo.write(text)
        elif blank=="" :
            text=""
        else :
            opt1 = re.compile('①|❶')
            opt2 = re.compile('②|❷')
            opt3 = re.compile('③|❸')
            opt4 = re.compile('④|❹')

            matchobj1 = opt1.search(text)
            matchobj2 = opt2.search(text)
            matchobj3 = opt3.search(text)
            matchobj4 = opt4.search(text)
            
            if matchobj1 and matchobj2 :
                opt=matchobj2.group()
                twoline=re.split(opt,text)
                line1=twoline[0].lstrip()
                line2="②"+twoline[1]
                fo.write(line1)
                fo.write("\n")
                fo.write(line2)
                
            elif matchobj3 and matchobj4 :
                opt=matchobj4.group()
                twoline=re.split(opt,text)
                line1=twoline[0].lstrip()
                line2="④"+twoline[1]
                fo.write(line1)
                fo.write("\n")
                fo.write(line2)
               
            else  :
                fo.write(text.lstrip())
                
            if matchobj4 :
                fo.write("\n")
            
with codecs.open(tmp_name, 'r', encoding='utf-8') as fi,  codecs.open(final_name, 'w', encoding='utf-8') as fo:
        
    for line in fi:

        text = line
        qex = re.compile('^\d+.')
        opt1 = re.compile('①')
        opt2 = re.compile('②')
        opt3 = re.compile('③')
        opt4 = re.compile('④')
        copt1 = re.compile('❶')
        copt2 = re.compile('❷')
        copt3 = re.compile('❸')
        copt4 = re.compile('❹')
        
        qobj = qex.search(text)
        optobj1 = opt1.search(text)
        optobj2 = opt2.search(text)
        optobj3 = opt3.search(text)
        optobj4 = opt4.search(text)
        coptobj1 = copt1.search(text)
        coptobj2 = copt2.search(text)
        coptobj3 = copt3.search(text)
        coptobj4 = copt4.search(text)
        blank = text.strip()
  
        if qobj:
            fo.write(text)
        elif optobj1 :
            new_line=text.replace('①','A.')
            fo.write(new_line.lstrip())
        elif optobj2 :
            new_line=text.replace('②','B.')
            fo.write(new_line.lstrip())
        elif optobj3 :
            new_line=text.replace('③','C.')
            fo.write(new_line.lstrip())
        elif optobj4 :
            new_line=text.replace('④','D.')
            fo.write(new_line.lstrip())
        elif coptobj1 :
            new_line=text.replace('❶','A.')
            fo.write(new_line.lstrip())
            ans="ANSWER: A"
        elif coptobj2 :
            new_line=text.replace('❷','B.')
            fo.write(new_line.lstrip())
            ans="ANSWER: B"
        elif coptobj3 :
            new_line=text.replace('❸','C.')
            fo.write(new_line.lstrip())
            ans="ANSWER: C"
        elif coptobj4 :
            new_line=text.replace('❹','D.')
            fo.write(new_line.lstrip())
            ans="ANSWER: D"
        elif blank=="" :
            fo.write(ans)         
            fo.write("\n")
            fo.write("\n")
