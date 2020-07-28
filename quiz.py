import random

def get_def_and_pop(word_list, word_dict):
	random_index = random.randrange(len(word_list))
	word = word_list.pop(random_index)
	definition = word_dict.get(word)
	return word,definition


def get_word_defination(rawstring):
    word, definition = rawstring.split(',', 1)
    return word, definition



fh = open("C:\\Users\\Akhlaq Ali Orakzai\\Desktop\\Python FInal Project\\Vocabulary_list.csv","r")
wd_list = fh.readlines()


wd_set = set(wd_list)
fh = open("C:\\Users\\Akhlaq Ali Orakzai\\Desktop\\Python FInal Project\\Vocabulary_set.csv", "w")
fh.writelines(wd_set)

word_dict = dict()
for rawstring in wd_set:
    word, definition = get_word_defination(rawstring)
    word_dict[word] = definition

while True:
	wd_list = list(word_dict)
	choice_list = []
	for x in range(4):
		word, definition = get_def_and_pop(wd_list, word_dict)
		choice_list.append(definition)

	random.shuffle(choice_list)
	print(word)
	print("-------------")

	for idx, choice in enumerate(choice_list):
		print(idx+1, choice)
	choice = int(input("Enter 1,2,3,4; 0 to exit"))
	if choice_list[choice-1] == definition:
		print("Correct!\n")
	elif choice == 0:
		exit(0)
	else:
		print("Incorrect!\n")
