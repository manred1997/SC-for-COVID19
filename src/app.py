from src.constants.conditions import (
    FEATURE_MODE,
    FLAGS
)
from src.constants.texts import (
    NAME_INPUT,
    SEX_INPUT,
    AGE_INPUT,
    DISCLAIMER_MESSEAGE,
    SUGGEST_EDUCATION_MESSAGE,
    THANK_MESSEAGE,
    INIT_QUESTION,
    A1, A2, A3, A4, B1, B2, B3, C1, C2, C3,
    ASK_RELEVANT_SYMP,
    ASK_RISK_FACTOR,
)
from src.utils import display


class Application(object):
    def __init__(self):
        

        self.flag = None
        self.risk_factor = None
        self.personal_info = {}

    def run(self, mode):
        education_mode = None
        
        # clear demography
        self._clear_demography()
        self.get_personal_info()
        # print(self.personal_info)

        assert mode in FEATURE_MODE
        if mode == 'screening':
            self.screening_feature()
            print(self.flag)
            if self.flag in FLAGS:
                pass
                #TODO
            else:
                education_mode = input(SUGGEST_EDUCATION_MESSAGE)
            # if education_mode:
            #     self.education()
            display(THANK_MESSEAGE)
        elif mode == 'education':
            pass
        else:
            raise Exception("For feature mode, Only sceening or education is available")


    def _clear_demography(self):
        ''' Clear all previous information about demography
        '''
        self.personal_info = {
            "name": "",
            "sex" : "",
            "age" : ""
        }

    def screening_feature(self):
        disclaimer_mess = input(DISCLAIMER_MESSEAGE)
        self.flag = None

        if disclaimer_mess.lower() == 'n':
            self.flag = None
            return
        else:
            init_symptom = input(INIT_QUESTION)
            if init_symptom.lower() == 'n':
                self.flag = None
                return
            else:
                return_a = self._a_question()
                if return_a:
                    return
                else:
                    self._bc_question()
                    
    def education(self):
        pass

        

    def get_personal_info(self):
        name = input(NAME_INPUT)
        sex = input(SEX_INPUT)
        age = input(AGE_INPUT)
        self.update_personal_info(
            name=name,
            sex=sex,
            age=age
        )
    def update_personal_info(self,name:str="",sex:str="",age:str="") -> None:
        ''' Update self.personal_info
        '''
        self.personal_info['name'] = name
        self.personal_info['sex'] = sex
        self.personal_info['age'] = int(age)

    def _a_question(self):
        a1 = input(A1)
        a2 = input(A2)
        a3 = 'n'
        if a2.lower() == 'y':
            a3 = input(A3)
        a4 = input(A4)
        if a1.lower() == 'y' or a3.lower() == 'y' or a4.lower() == 'y':
            self.flag = 'red'
            return 1
        else:
            return 0
    
    def _bc_question(self):
        b1 = input(B1)
        if b1.lower() == 'y':
            self.flag = 'red'
            return
        b2 = input(B2)
        if b2.lower() == 'y':
            b3 = input(B3)
            if b3.lower() in ['y', 'idk']:
                self._ask_risk_factor()
                if self.risk_factor:
                    self.flag = 'red'
                    return
                else:
                    c2 = input(C2)
                    if int(c2) > 3:
                        self.flag = 'yellow'
                        return
        c1 = input(C1)
        c1_1 = self._ask_relevant_symptom()
        # print(self.personal_info)

        if c1_1.lower() == 'y' or c1.lower() == 'y':
            c3 = None
            if self.personal_info['sex'] == 'female':
                c3 = input(C3)
            if self.personal_info['age'] > 60 or c3 == 'y':
                self.flag = 'yellow'
                return
            if not self.risk_factor:
                self._ask_risk_factor()
                c1_1 = self._ask_relevant_symptom()
                if self.risk_factor or c1_1 == 'y':
                    self.flag = 'yellow'
                    return
                else:
                    self.flag = 'green'
        else:
            self.flag = 'green'

    def _ask_risk_factor(self):
        check_risk_factor = input(ASK_RISK_FACTOR)
        if check_risk_factor == 'y':
            self.risk_factor = True
        else: self.risk_factor = False
    
    def _ask_relevant_symptom(self):
        check_relevant_symptom = input(ASK_RELEVANT_SYMP)
        return check_relevant_symptom

    def _red_flag(self):
        pass
    def _yello_flag(self):
        pass
    def _green_flag(self):
        pass
