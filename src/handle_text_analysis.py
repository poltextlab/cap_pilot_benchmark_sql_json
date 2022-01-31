import hu_core_news_lg
import src.DAO

dao = src.DAO


def process_text(nlp: hu_core_news_lg,
                 text_id: str,
                 text: str,
                 sentence_id: int,
                 word_id: int
                 ) -> (int, int):
    """
    Function for creating the records in MONDAT and CONLL_SZO table. Sentence_id and word_id are gotten is parameter.
    The function returns the modified (increased) values of sentence_id and word_id for later use.

    :param word_id:
    :param sentence_id:
    :param nlp: loaded model for sentence splitting, and morphological and dependency analysis
    :param text_id: The foreign key for each sentence; the text_id field in MONDAT tables' records
    :param text: text to segment into sentences
    :return: (sentence_id: int, word_id: int)
    """

    doc = nlp(text)
    for sentence in doc.sents:

        # create the whole sentence in MONDAT table!
        mondat_id = sentence_id
        raw_text = sentence.text
        text_id = text_id

        insert_statement = ("INSERT INTO `mondat` (`mondat_id`, `raw_text`, `text_id`) " "VALUES(%s, %s, %s)")
        data = (mondat_id, raw_text, text_id)
        dao.execute_insert(insert_statement, data)

        for token in sentence:

            szo_id = word_id
            sorszam = 0
            szoalak = token.text
            lemma = token.lemma_
            entity_IOB = " ".join([token.ent_iob_, token.ent_type_])
            POS = token.pos_
            morf_analysis = str(token.morph)
            dependencia_el = token.dep_
            mondat_id = sentence_id

            insert_statement = ("INSERT INTO `CONLL_SZO` (`szo_id`, `sorszam`, `szoalak`, `lemma`, `entity_IOB`, `POS`, `morf_analysis`, `dependencia_el`, `mondat_id`) " "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
            data = (szo_id, sorszam, szoalak, lemma, entity_IOB, POS, morf_analysis, dependencia_el, mondat_id)
            dao.execute_insert(insert_statement, data)

            word_id += 1

        sentence_id += 1

    return sentence_id, word_id
