from typing import List
def all_construct(target_word: str, word_bank: List[str]) -> List[List[str]]:
    """_Find all possible ways of constructing a target word from a given list of words_

    Args:
        target_word (str): _Word to construct_
        word_bank (List[str]): _A list of words to choose from_

    Returns:
        List[List[str]]: _List of possible combinations for constructing the target_
    """
    all_ways = []

    if target_word == "":
        return [[]]
    for word in word_bank:
        if target_word.startswith(word):
            new_target_word: str= target_word.removeprefix(word)
            results = all_construct(target_word=new_target_word, word_bank=word_bank)
            ways = [[word] + result for result in results]
            all_ways.extend(ways)
    return all_ways



def main()-> None:
    word_bank: List[str] = ['ab', 'abc', 'cd', 'def', 'ef','abcd', 'c']
    target_word: str = 'abcdef'
    possible_construct: List[List[str]] = all_construct(target_word=target_word, word_bank=word_bank)

    print(f"Possible combinations in {word_bank} that can yield {target_word} are: {possible_construct}")

if __name__ =="__main__":
    main()