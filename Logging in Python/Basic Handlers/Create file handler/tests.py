from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    answers = [
        ['logging.FileHandler(log_filename)', 'logging.FileHandler(filename=log_filename)'],
        ['addHandler']
    ]


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


