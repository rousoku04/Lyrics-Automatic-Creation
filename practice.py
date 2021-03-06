import markov
import logging
import sys
from distutils.util import strtobool

logger = logging.getLogger(__name__)
fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"
logging.basicConfig(level=logging.DEBUG, format=fmt)

def make_songs(filename):
    filename = filename
    # args = filename

    # format = bool(strtobool(args[2])) if args[2:3] else True
    # max_chars = int(args[3]) if args[3:4] else 70
    # min_chars = int(args[4]) if args[4:5] else 25
    min_chars = 2
    max_chars = 3


    """
    1. Load text -> Parse text using MeCab
    """
    parsed_text = markov.parse_text('data/' + filename + '.txt')
    logger.info('Parsed text.')


    """
    2. Build model
    """
    text_model = markov.build_model(parsed_text, format=format, state_size=2)
    logger.info('Built text model.')

    json = text_model.to_json()
    open('data/' + filename + '.json', 'w').write(json)

    # Load from JSON
    # json = open('input.json').read()
    # text_model = markovify.Text.from_json(json)


    """
    3. Make sentences
    """
    try:
        for _ in range(3):
            sentence = markov.make_sentences(text_model, max=max_chars, min=min_chars)
            logger.info(sentence)
            # return sentence

    except KeyError:
        logger.error('KeyError: No sentence starts with "start".')
        logger.info('If you set format=True, please change "start" to another word.')
        logger.info('If you set format=False, you cannot specify "start".')

    