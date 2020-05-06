import pandas as pd
pd.set_option('display.max_colwidth', -1)

#Loading data and reformating the columns
show_data = pd.read_csv('jeopardy.csv')
show_data = show_data.rename(columns = {" Air Date": "Air Date", " Round" : "Round", " Category": "Category", " Value": "Value", " Question":"Question", " Answer": "Answer"})

#Finds questions which contain a certain word
def find_in_q(words):
    filter_func = lambda x: all(i.lower() in x.lower() for i in words)
    return show_data[show_data['Question'].apply(filter_func)]

#Creating a test for our function
test_words = ['king', 'england']
print(find_in_q(test_words))

#Column which contains the float equivalents of question values
convert_to_float = lambda x: float(x[1:].replace(',', '',) if x != 'None' else 0)
show_data['Float Value'] = show_data['Value'].apply(convert_to_float)

#Finding the mean value of questions containing a certain word
new_df = find_in_q(["King"])
print(new_df['Float Value'].mean())