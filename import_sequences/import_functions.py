from Bio import SeqIO
from Bio import Seq
import glob
import os

test_data = "/Users/jlbodzin/PycharmProjects/sequence_confirmation/import_sequences/test_email_seq_data.txt"

print(test_data)


def import_from_email(test_data:str):
    #TODO:write function to parse data pasted from email
    imported_data = open(test_data, "r")
    allthedata = imported_data.read()
    #split_words = words.splitlines()
    print(allthedata)
    pass

def import_from_abi(folder_name:str):
    os.chdir(folder_name)

    for file in glob.glob("*.abi"):
        files.append(file) #list of all files loaded


    pass

def import_oligos():
    #TODO:write a function to import all oligo sequences for alignment.
    pass

def import_DNA_seq():
    #TODO:write a function that import DNA and or protein sequences for alignment with sequencing data
    pass

"""
class sequence_core_data(Seq):
    def __init__(self,data,alphabet=Alphabet(), sample_number: int, primer: str, clone_name: int, gel_number: int, lane_number: int, comments: int)
        def super().__init__(self, data, alphabet=Alphabet())
        self.sample_number = sample_number
        self.primer = primer
        self.clone_name = clone_name
        self.gel_number = gel_number
        self.lane_number = lane_number
        self.comments = comments

"""


print("Test")
import_from_email(test_data)