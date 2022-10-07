def th(client_id, sentence):
    """Cleans up the passed sentence, removing or reformatting invalid data.

    Args:
      client_id (str): Client ID of sentence's speaker
      sentence (str): Sentence to be cleaned up.

    Returns:
      (str): Cleaned up sentence. Returning None or a `str` of whitespace flags the sentence as invalid.
    """
    # TODO: Add more missing
    sentence = sentence.replace("แแ", "แ")
    sentence = sentence.replace("กฏหมาย", "กฎหมาย") # missing word but speaker speak correct
    return sentence
