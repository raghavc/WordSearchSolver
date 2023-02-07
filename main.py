import cv2
import pytesseract

def main ():
# Main Word Search Into Matrix
    image = cv2.imread("word_search.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(thresh)
    lines = text.split("\n")
    char_matrix = [list(line) for line in lines]

    # Word Search Bank Portion 
    WordBank = cv2.imread("word_search_bank.png")
    text = pytesseract.image_to_string(WordBank)
    words = text.split()
    words_to_find = words
# Define a function to check for a word in a given direction
def check_word( words_to_find, char_matrix):
    found_word = ""
    Entire_Found_List = []
    counter = 0
    for x in range (len(words_to_find)):
        for r in range(len(char_matrix)):
            for c in range(len(char_matrix[0])):
                ########################################
                ########################################
                ########################################
                ########################################
                if char_matrix.charAt(r,c)==words_to_find[counter].charAt(x):
                    #upper left diagnol
                    #
                    #
                    while (char_matrix.charAt(x)!= -1):
                        for i in range(len(char_matrix)):
                            if char_matrix.charAt(r-i,c-i)==words_to_find.charAt(x+i):
                                found_word = found_word + char_matrix.charAt((r-i),(c-i))
                    if (found_word == words_to_find[x]):
                        Entire_Found_List[counter] = found_word 
                        counter+1
                    found_word.clear()
                    #Direct Upper Value
                    #
                    #
                    while (char_matrix.charAt(x)!= -1):
                        for i in range(len(char_matrix)):
                            if char_matrix.charAt(r-i,c)==words_to_find.charAt(x+i):
                                found_word = found_word + char_matrix.charAt((r-i),(c))
                    if (found_word == words_to_find[x]):
                        Entire_Found_List[counter] = found_word 
                        counter+1
                    found_word.clear()
                    #Upper Right Diagnol
                    #
                    #
                    while (char_matrix.charAt(x)!= -1):
                        for i in range(len(char_matrix)):
                            if char_matrix.charAt(r-i,c+i)==words_to_find.charAt(x+i):
                                found_word = found_word + char_matrix.charAt((r-i),(c+i))
                    if (found_word == words_to_find[x]):
                        Entire_Found_List[counter] = found_word 
                        counter+1
                    found_word.clear()
                    #Direct Right Value
                    #
                    #
                    while (char_matrix.charAt(x)!= -1):
                        for i in range(len(char_matrix)):
                            if char_matrix.charAt(r,c+i)==words_to_find.charAt(x+i):
                                found_word = found_word + char_matrix.charAt((r),(c+i))
                    if (found_word == words_to_find[x]):
                        Entire_Found_List[counter] = found_word 
                        counter+1
                    found_word.clear()
                    #Bottom Right Diagnol
                    #
                    #
                    while (char_matrix.charAt(x)!= -1):
                        for i in range(len(char_matrix)):
                            if char_matrix.charAt(r+i,c+i)==words_to_find.charAt(x+i):
                                found_word = found_word + char_matrix.charAt((r+i),(c+i))
                    if (found_word == words_to_find[x]):
                        Entire_Found_List[counter] = found_word 
                        counter+1
                    found_word.clear()
                    #Direct Bottom Value
                    #
                    #
                    while (char_matrix.charAt(x)!= -1):
                        for i in range(len(char_matrix)):
                            if char_matrix.charAt(r+i,c)==words_to_find.charAt(x+i):
                                found_word = found_word + char_matrix.charAt((r+i),(c))
                    if (found_word == words_to_find[x]):
                        Entire_Found_List[counter] = found_word 
                        counter+1
                    found_word.clear()
                    #Bottom Left Diagnol
                    #
                    #
                    while (char_matrix.charAt(x)!= -1):
                        for i in range(len(char_matrix)):
                            if char_matrix.charAt(r+i,c-i)==words_to_find.charAt(x+i):
                                found_word = found_word + char_matrix.charAt((r+i),(c-i))
                    if (found_word == words_to_find[x]):
                        Entire_Found_List[counter] = found_word 
                        counter+1
                    found_word.clear()
                    #Direct left value
                    #
                    #
                    while (char_matrix.charAt(x)!= -1):
                        for i in range(len(char_matrix)):
                            if char_matrix.charAt(r,c-i)==words_to_find.charAt(x+i):
                                found_word = found_word + char_matrix.charAt((r),(c-i))
                    if (found_word == words_to_find[x]):
                        Entire_Found_List[counter] = found_word 
                        counter+1
                    found_word.clear()
    return Entire_Found_List

    

                




if __name__ == "__main__":
    main()
# Return the found words
