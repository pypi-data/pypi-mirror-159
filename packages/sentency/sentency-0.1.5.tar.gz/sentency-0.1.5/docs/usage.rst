=====
Usage
=====

To use sentency in a project::

    import spacy
    from spacy import displacy

    from sentency.regex import regexize_keywords
    from sentency.sentency import Sentex

    text = """
    Screening for abdominal aortic aneurysm. 
    Impression: There is evidence of a fusiform 
    abdominal aortic aneurysm measuring 3.4 cm.
    """
    aaa_keywords = "abdominal aortic aneurysm"
    ignore_keywords = "screening aneurysm"

    keyword_regex = regexize_keywords(aaa_keywords)
    ignore_regex = regexize_keywords(ignore_keywords)

    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe(
    "sentex", config={
            "sentence_regex": keyword_regex, 
            "ignore_regex": ignore_regex,
            "annotate_ents": True,
            "label": "AAA"
            }
    )

    doc = nlp(text)

    displacy.render(doc, style="ent", options = {"ents": ["AAA"]})
