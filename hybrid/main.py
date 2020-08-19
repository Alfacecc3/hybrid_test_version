import json
import lib.input_processing_utils as ipu
import lib.skill_processor as skp
import os

devmode=False
'''
if devmode is True the file data.json is unlocked
so i will ask for precisely values to save them
'''

class IA():
    '''
    methods:
    __init__ {
        append to instance dataset and skills
        then run the main loop
    }
    run {
        main loop, if devmode {
            on_known_input() -> skill_n.py()
            on_unknown_inp() -> input for indexname and contents
        } elif not devmode {
            on_known_input() -> skill_n.py()
            on_unknown_inp() -> non ho capito, usr will repeat in other words, try to understand them.
        }
    }
    do {
        exec the content of a skill using its first line as name.
    }
    '''
    def __init__(self):
        super().__init__()
        self.data = json.loads(open('db/dataset.json').read())
        self.skills = skp.read_skills()
        #self.do('saluta')
        while True:
            self.run()

    def run(self):
        x=input('>> ').casefold()
        #è negli intent?
        found=False
        for intent_key in self.data['intents']:
            if x in self.data['intents'][intent_key]['samples']:
                try:
                    self.do(ipu.get_skillex(self.data['intents'][intent_key]['name']))
                    found=True
                except KeyError:
                    print('scusa, non ho capito')
        if not found:
            if devmode:
                #update dataset.json and make a new skill or
                #update dataset.json and update a new skil too
                #update json
                newindexname=ipu.get_skillex(input('indexname: ').casefold().replace(' ', ''))
                newintentname=newindexname.capitalize().replace(' ', '')+'Intent'
                contents=input('possibilities: ').split(', ')
                self.data['intents'][newintentname] = {
                    "name":newindexname,
                    "samples":contents
                }
                f=open('db/dataset.json', 'w+')
                f.write(json.dumps(self.data))
                f.close()
                #make a new skill
                num=0
                for name in os.listdir('skills/'):
                    num+=1
                skillname='skill_'+str(num)+'.py'
                f=open('skills/'+skillname, 'w+')
                f.write(self.data['skill_template'].replace('<0>', newindexname).replace('<1>', str(contents)))
                f.close()
            else:
                print('scusa, non ho capito')
    
    def do(self, w:str):
        '''
        esegui il valore di skills[w]
        '''
        f = lambda x:'#'+x if not x.startswith('#') else x
        exec(self.skills[f(w)])

hy=IA()