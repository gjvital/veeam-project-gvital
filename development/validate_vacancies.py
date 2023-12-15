from environments import*
from assertDefinitions_pipeline import*
from assertsByGroups import*
import re
from Elements import *

def test_locating_vacancies(chrome_environment_setup):

        #comparing test
        locating_vacancies()

        #end_test
        quit_browser()