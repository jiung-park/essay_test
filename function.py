def extractNoun(text_parsed):
    words = []
    for sentence in text_parsed.sentences:
        for word in sentence.words:
            lemma = word.lemma.split('+')
            xpos = word.xpos.split('+')
            for tok, pos in zip(lemma, xpos):
                if pos.startswith('n') or pos == 'f':
                    words.append(tok)
    return words


def checkNecessaryKeyWord(text_parsed, necessary_key_word):
    text_noun = extractNoun(text_parsed)
    flag = True
    for noun in necessary_key_word:
        if noun not in text_noun:
            flag = False
            return flag
    return flag


def checkDependencyKeyWord(text_parsed, dependency_key_word):
    flag = True
    for sentence in text_parsed.sentences:
        for word in sentence.words:
            lemma = word.lemma.split('+')
            xpos = word.xpos.split('+')
            head = word.head
            for key_word_bunch in dependency_key_word:
                for key_word in key_word_bunch[0]:
                    if key_word in lemma:
                        lemma_comp = sentence.words[head-1].lemma.split('+')
                        xpos_comp = sentence.words[head-1].xpos.split('+')
                        flag_comp = False
                        for key_word_comp in key_word_bunch[1]:
                            if key_word_comp in lemma_comp:                            
                                flag_comp = True
                        flag = flag_comp and flag
    return flag