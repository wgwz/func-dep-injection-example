# dependency injection with function

MESSAGE_LOG = 'log.txt'

def parse_message(raw_text, log_function=None):
    text = 'message: ' + raw_text
    if log_function:
        log_function(MESSAGE_LOG, text=text)
    return text

def log_message(filename, text):
    with open(filename, 'a+') as f:
        f.write(text + '\n')
    return 'message logged at ' + filename

def message_tasks(raw_text):
    parse_message(raw_text=raw_text, log_function=log_message)
    return 'message tasks complete'

if __name__ == '__main__':
    message_tasks(raw_text='next message')
