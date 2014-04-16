'''
R1C2: Words With Friends Cheater
Your goal is to create a program that finds the highest scoring arrangement of Words With
Friends tiles. The points awarded for each tile are as follows:
BLANK 0
A 1
B 4
C 4
D 2
E 1
F 4
G 3
H 3
I 1
J 10
K 5
L 2
M 4
N 2
O 1
P 4
Q 10
R 1
S 1
T 1
U 2
V 5
W 4
X 8
Y 3
Z 10
A few notes:
● Your program will not accept any arguments this time. When the program is run, it will
output a prompt asking the user to input a space­delimited string of their tiles.
● The maximum number of tiles is 7. Near the end of a game a user may have as few as 1.
● You can assume the input is valid and follows the specified format exactly. You don’t
necessarily need to add any error handling for the input.
● Take into account that inputs may not necessarily contain a valid output.
● Words With Friends awards an extra 35 points if all 7 tiles are used. Your program
should take that into account.● Your output should include:
○ the final word, each tile separated by spaces
○ the point value of that word
○ the remaining unused tiles (if any), each tile separated by spaces
● If a BLANK tile is used in your final word, include BLANK in the appropriate place, and add
its interpreted letter in parentheses at the end of the word. Take into account that Word
With Friends has two BLANK tiles in each game, so two sets of parentheses may be
necessary.
● We should all use a main() function like Ian did in R1C1. It’s probably a good habit to get
into, and also it’ll keep our code uniform. That’ll help keep your submissions anonymous.
'''



# Creates wordlist from UNIX dictionary.
def get_words():
    
    words_file = open('/usr/share/dict/words')
    word_list = words_file.read().splitlines()

    return word_list

# Compares word from wordlist with tiles and determines if word can be made,
# taking blanks into account. If word can be made, it returns the word.
def can_make(poss_word, tiles):
    
    x = 0
    tiles_copy = sorted(tiles)
    for letter in poss_word:
        if letter in tiles_copy:
            tiles_copy.remove(letter)
            x += 1
        elif 'blank' in tiles_copy:
            tiles_copy.remove('blank')
            x += 1
                
    if len(poss_word) == x:
        return poss_word


# Calculates the points for the word, taking into account blanks and length bonus.
def poss_points(word, points, tiles):
    
    tiles_copy = sorted(tiles)
    total = 0

    for letter in word:
        if letter in tiles_copy:
            total += points[letter]
            tiles_copy.remove(letter)
        else:
            tiles_copy.remove('blank')
    
    if len(word) == 7:
        total += 35

    return total
# Calls previous functions to pull wordlist, check each word in list, compute score for
# buildable words, and print the highest scoring word.
def find_word(tiles, word_list):

    my_list = {}
    replaced = []
    points = {
        'a':1,'b':4,'c':4,'d':2,'e':1,'f':4,'g':3,'h':3,'i':1,'j':10,'k':5,'l':
        2,'m':4,'n':2,'o':1,'p':4,'q':10,'r':1,'s':1,'t':1,'u':2,'v':5,'w':4,'x'
        :8,'y':3,'z':10,'blank':0
        }

    # Checks if word can be made with tiles and if so, assigns it and its point
    # value as key:value dict pair.Ignores capitalized words.
    for word in word_list:
        if not word.istitle() and can_make(word, tiles):
            my_list[word] = poss_points(word, points, tiles)
            
    # If no buildable words found, restarts module.
    if my_list == {}:
        print "\nNo valid word found.\n"
        main()

    # Pulls highest scoring word and its score from dictionary.
    sorted_list = sorted(my_list.items(), key=lambda point: point[1])
    best_word = sorted_list[-1]
    high_word = best_word[0]
    high_score = best_word[1]


    # Reduces tiles to only unused letters, subs blanks in word where applicable
    # and places the 'blanked' letters in their own list.
    high_word = list(high_word)
    for letter in high_word:
        if letter in tiles:
            tiles.remove(letter)    
        elif 'blank' in tiles:
            tiles.remove('blank')
            ind = high_word.index(letter)
            high_word.remove(letter)
            high_word.insert(ind, 'blank')
            replaced.append(letter)

    # Formats and prints word, any blanked letters, word score, and any unused
    # letters.
    replaced = ['('+ each + ')' for each in replaced]        
    print (
        ' '.join(high_word) + ' ' + ' '.join(replaced) + '\n' + str(high_score)
        + '\n' + ' '.join(tiles)).upper(
        )

# Prompts user input and passes it through find_word function, then prompts for
# additional attempts
def main():

    word_list = get_words()

    get_tiles = raw_input(
        'Please enter your tile letters. Enter BLANK for a blank tile:\n'
        )

    my_tiles = get_tiles.lower().split()

    find_word(my_tiles, word_list)
    
    ask = raw_input("Enter 1 to exit, or any other key to play again.")

    if ask == '1':
        exit()
    else:
        main()
    
if __name__ == '__main__':
    main()
