
# # Challange # #
# Write a code to find the word in a list that would come first alphabetically

# # Example: When given the list below 
# # word_list = ["hamster", "turtle", "cat", "bird"]
# The code should find "bird" as the word that would come first alphabetically


def alphabet(words):
        return min(words)

if __name__ == "__main__":
    word_list = ["hamster", "turtle", "cat", "bird"]
    print(alphabet(word_list))

    

