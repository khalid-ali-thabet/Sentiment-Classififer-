punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def strip_punctuation (word):
    for char in punctuation_chars:
        word = word.replace(char, '')
    return word

def get_neg(string):
    count = 0
    string = strip_punctuation(string) # remove punctuation chars
    string_list = string.split() # list of words 
    for word in string_list:
        if word.lower() in negative_words: # all words must be lower 
            count += 1
    return count

def get_pos (string):
    count = 0
    string = strip_punctuation(string) # remove punctuation chars
    string_list = string.split() # convert it to list of words
    for word in string_list:
        if word.lower() in positive_words:
            count += 1
    return count

output_file = open("resulting_data.csv","w")
output_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
output_file.write('\n')


data_file = open("project_twitter_data.csv", 'r')

data_lines = data_file.readlines()
for row in data_lines[1:]:
    
    row_vals = row.strip().split(',')
    row_string = '{}, {}, {}, {}, {}'.format(row_vals[1],row_vals[2],get_pos(row_vals[0]),get_neg(row_vals[0]),get_pos(row_vals[0])-get_neg(row_vals[0]))
    output_file.write(row_string)
    output_file.write('\n')


output_file.close()
data_file.close()