def tokenizer(text):
    words = text.split(' ') # no n-gram
    tokenized_words = []
    for word in words:
        tokenized_words.append(word_tokenizer(word))
    return tokenized_words


def word_tokenizer(word):
    if ('.' not in word) and ('\'' not in word):
        return word
    else:
        if '\'' in word:
            # 따옴표로 시작해서 따옴표로 끝나는 단어의 따옴표 삭제, 단어 도중에 따옴표가 나오는 경우 따옴표 포함 뒤의 글자 모두 삭제
            if word.index('\'') == 0:
                word = word[1:]

            if '\'' in word:
                word = word[:word.index('\'')]

            return word

        if '.' in word:
            # .com 으로 끝나는 단어는 토큰화되지 않도록
            if word[-4:] == ".com":
                return word

            # 마침표로 연결된 단어에서 마침표 앞, 뒤 및 사이에 있는 글자가 모두 1개일 경우 마침표 삭제, 0개 혹은 2개 이상이면 토큰화되지 않도록
            elif len(word) % 2 == 1:
                for i in range(len(word)):
                    if word[i] == '.' and i%2==1:
                        continue
                    elif word[i] != '.' and i%2==0:
                        continue
                    else: break
                else: word = word.replace('.','')
            else: return word

        return word

if __name__ == '__main__':
    text = '''i've 'hello' 'hello'world' imlab's PH.D I.B.M snu.ac.kr 127.0.0.1 galago.gif ieee.803.99 naver.com gigabyte.tw pass..fail'''
    print(tokenizer(text))