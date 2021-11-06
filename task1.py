def reverse_text (text):
    # your code here
    reversed_text = []
    for i in text.split():
        alpha = []
        not_alpha = []
        for index, value in enumerate(i):
            if value.isalpha():
                alpha.append(value)
            else:
                not_alpha.append((index, value))
        alpha.reverse()
        for index, value in not_alpha:
            alpha.insert(index, value)
        reversed_txt = ''.join(alpha)
        reversed_text.append(reversed_txt)
    return ' '.join(reversed_text)

if __name__ == '__main__':
    reverse_text()
    