from environments import *
from assertDefinitions_pipeline import *
from Elements import *
from assertsByGroups import *

def test_research_development(chrome_environment_setup):
        choose_research_and_development()

        quit_browser()