from math import ceil

from BibaAndBoba.biba_and_boba import BibaAndBoba


def _max_correlation(n: int) -> float:
    """
    The max_correlation function computes the maximum correlation between two frequency dictributions.

    :param n: :obj:`int`: Specify the length of the frequency distributions
    :return: The maximum correlation
    """
    i = 1
    s = 0

    for i in range(1, n + 1):
        s += 1 / i
    return s


class Comparator:
    """
    Comparator class is used to compare two people. It provides methods to get the correlation percentage of the two
    people and the words that are the same for both of them.
    """
    def __init__(self, person1: BibaAndBoba, person2: BibaAndBoba, limit: int = 10):
        if not isinstance(person1, BibaAndBoba):
            raise TypeError("You must pass a BibaAndBoba object as the argument")
        if not isinstance(person2, BibaAndBoba):
            raise TypeError("You must pass a BibaAndBoba object as the argument")

        self.__person1_freq_dist = person1.freq_dist(limit=limit)
        self.__person2_freq_dist = person2.freq_dist(limit=limit)
        self.__person_1_name = person1.get_name()
        self.__person_2_name = person2.get_name()
        self.__max_correlation = _max_correlation(len(self.__person1_freq_dist["Word"]))
        self.__same_words = set()
        self.__correlation_percent = self.__correlation()

    def __correlation(self) -> float:
        """
        The __correlation function calculates the correlation between two people.
        It does this by calculating the number of same words in both person's word list,
        based on their place in frequency distributions.

        :param self: Access variables that belongs to the class
        :return: The correlation between two people
        """
        corr = 0
        quotients_person1 = self.__person1_freq_dist["Quotient"]
        quotients_person2 = self.__person2_freq_dist["Quotient"]

        for i, word_1 in enumerate(self.__person1_freq_dist["Word"]):
            for j, word_2 in enumerate(self.__person2_freq_dist["Word"]):
                if word_1 == word_2:
                    quotient_diff = abs(quotients_person1[i] - quotients_person2[j])
                    if quotient_diff > 0.15:
                        corr += (1 / (i + 1)) - quotient_diff
                    else:
                        corr += (1 / (i + 1))
                    self.__same_words.add(word_1)
                else:
                    continue

        result = (corr / self.__max_correlation) * 100
        return ceil(result)

    def get_correlation(self) -> float:
        """
        The get_correlation function returns the correlation between two people.

        :param self: Access the class attributes
        :return: The correlation between the two columns
        """
        return self.__correlation_percent

    def get_same_words(self) -> set:
        """
        The get_same_words function returns a list of words that are the same for both people.

        :param self: Access the attributes and methods of the class in which it is used
        :return: A list of words that are the same as the word in question
        """
        return self.__same_words
