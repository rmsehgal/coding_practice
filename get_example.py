'''
Script to generate an example coding problem to solve
should search (either this base directory or another folder) to
find the list of algorithims which I have written unit tests for
and have prompts for

Once we have this list we can select one at random and generate
a text prompt to solve.

We should be able to pass the resulting text file back
to another program and run it through the unit test defined for that
prompt 
'''
import random


def get_prompts(pfile):
    pfh = open(pfile,'r')
    pl = pfh.read()
    pfh.close()
    return pl

def select_prompt(plst):
    return random.choice(plst)







if __name__=="__main__":

    #call cli arg parsing
    
    #read list of prompts
    
    #select prompt

    #read prompt template

    #fill in and write to file template for selected prompt
    #  file name should be generated from date/time but not prompt info

    #print any relevnat info out to command line

    #DONE!!!


