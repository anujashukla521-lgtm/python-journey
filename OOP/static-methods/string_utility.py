class StringUtility:
   

    @staticmethod
    def count_vowels(text):
        count = 0
        for char in text:
            if char.lower() in "aeiou":
                count+=1
        return count

    @staticmethod
    def count_characters(text):
        count = 0
        for char in text:
            count+=1
        return count

    @staticmethod
    def reverse_string(text):
        reverse = text[::-1]
        return reverse

        
print("Number of vowels:",StringUtility.count_vowels("anuja"))
print("Number of characters:",StringUtility.count_characters("anuja"))
print("Reverse string:",StringUtility.reverse_string("python"))