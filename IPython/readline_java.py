import sys

from org.gnu.readline import Readline
from org.gnu.readline import ReadlineLibrary
from org.gnu.readline import ReadlineCompleter


class PyCompleter(ReadlineCompleter):
    def __init__(self, completer=None):
        self.completer = completer
        
    def complete(self, text, state):
        "@sig public String complete(java.lang.String text, java.lang.int state)"
        result = None
        if self.completer != None:
            result = self.completer(text, state)
        return result

pycompleter = PyCompleter()
begidx = None
endidx = None
DEBUG = False

def setup_readline():
    global begidx, endidx
    Readline.load(ReadlineLibrary.GnuReadline)
    Readline.initReadline("jython")
    Readline.setWordBreakCharacters(" \t\n`~!@#$%^&*()-=+[{]}\\|;:'\",<>/?")
    Readline.setCompleter(pycompleter)
    begidx = 0
    endidx = 0

setup_readline()

def unsupported(s):
    if DEBUG is True:
        print >> sys.stderr, "Unsupported Readline Operation: %s" % s

def parse_and_bind(string):
    return Readline.parseAndBind(string)

def get_line_buffer():
    return Readline.getLineBuffer()

def insert_text(string):
    unsupported('insert_text(%s)' % string) 
    
def read_init_file(filename=None):
    Readline.readInitFile(filename)

def read_history_file(filename="~/.history"):
    Readline.readHistoryFile(filename)

def write_history_file(filename="~/.history"):
    Readline.writeHistoryFile(filename)

def clear_history():
    Readline.clearHistory()

def add_history(line):
    Readline.addToHistory(line)

def get_history_length():
    return Readline.getHistorySize()

def set_history_length(length):
    unsupported('set_history_length(%r)' % length)

def get_current_history_length():
    return Readline.getHistorySize()

def get_history_item(index):
    return Readline.getHistoryLine(index)
    
def set_completer(function=None):
    pycompleter.completer = function
    
def get_completer():
    pycompleter.completer
    
def get_completion_type():
    """Get the type of completion being attempted."""
    unsupported("get_completion_type()")
    return 0

def get_begidx():
    return begidx

def get_endidx():
    return endidx
    
def set_completer_delims(string):
    Readline.setWordBreakCharacters(string)

def get_completer_delims():
    return str(Readline.getWordBreakCharacters())
    
# xxx
def on_completion(text, state):
    result = None
    completer = get_completer()
    if completer != None:
        result = completer(text, state)
    return result

# xxx
def flex_complete(text, start, end):
    global begidx, endidx
    begidx = start
    endidx = end
    # return completion_matches(text, on_completion)
    return None

def remove_history_item(pos):
    unsupported('remove_history_item(%r)' % pos)

def redisplay():
    unsupported('redisplay()')

def set_startup_hook(function=None):
    unsupported('set_startup_hook(%s)' % function)
    
def set_pre_input_hook(function=None):
    unsupported('set_pre_init_input_hook(%s)' % function)

