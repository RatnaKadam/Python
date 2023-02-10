import pandas

# Creating a dataframe from CSV file
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Converting Dataframe's data to a dictionary
my_dict = {}
for (index, row) in df.iterrows():
    my_dict[f"{row.letter}"] = f"{row.code}"

# Taking user input and creating NATO list
user_input = input("Enter a word: ").upper()
NATO_list = []
for every_character in user_input:
    value = my_dict[every_character]
    NATO_list.append(value)

print(NATO_list)
