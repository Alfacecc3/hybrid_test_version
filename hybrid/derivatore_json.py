from lib.input_processing_utils import get_skillex as gsx
import json
import time

#setup settings
class HyDeveloperSettings():
    def __init__(self):
        super().__init__()
        self.syns_output = True
        self.skill_template = '#<0>\nimport random\nimport time\nrandom.seed(time.time())\nc=<1>\nprint(c[random.randint(0, len(c)-1)])\n'
        self.web_scraper_skill_template=''

devsets = HyDeveloperSettings()
devsets.syns_output=False

def intent_maker(name:str, contents:list, synsout=True, extraconts=[]):
    '''
    new intent -> dict['intents'][name.capitalize()+'Intent']['samples'] = contents\n
    add an intent to dict['intents']
    '''
    jpath='db/dataset.json'
    data = json.loads(open(jpath).read())
    data['intents'][name.capitalize().replace(' ', '')+'Intent'] = data['intents']['ExampleIntent'].copy()
    data['intents'][name.capitalize().replace(' ', '')+'Intent']['name'] = name
    data['intents'][name.capitalize().replace(' ', '')+'Intent']['samples']=contents
    if not synsout:
        data['intents'][name.capitalize().replace(' ', '')+'Intent']['outputs']=extraconts
    f=open(jpath, 'w+')
    f.write(json.dumps(data))
    f.close()
    #print(json.dumps(data))
    print('[*] Done')

def derivate(l_, t_='echo', jpath='db/dataset.json', ppath='_standard_'):
    '''
    derivate(jpath:json file path, ppath:python output file path, t_:output type, l_:index to use listed)
    usa un file json strutturato secondo la memoria di hy e genera una skill di tipo t_
    per ogni indice in l_, usa ppath come percorso del file python di output, usa "_standard_" per
    il nome di default, e jpath come percorso del file json di input.
    il file json deve essere strutturato come la memoria di hy quindi cos':
    {'intents':{'IntentName':{'name':'nome','samples':[]}, 'SecondIntent':{'name':'nome2','samples':[]}}}
    t_ possibilities:
    echo -> random output an element of string array
    webscrape -> return something from a website
    '''
    print('[*] Collecting input files...')
    json_file = json.loads(open(jpath).read())
    if ppath=='_standard_':
        import os
        n=0
        for file in os.listdir('skills/'):
            n+=1
        name='skills/skill_'+str(n)+'.py'
    else:
        name=ppath
    print('[*] skill name='+name)
    for key in json_file['intents']:
        print('[*] Actually processing '+key)
        if key in l_:
            print('[*] Found! '+key)
            if t_=='echo':
                print('[*] t_ is setted to echo')
                if devsets.syns_output==True:
                    #usa gli stessi valori di attivazione, samples[:]
                    body= devsets.skill_template.replace('<0>', gsx(json_file['intents'][key]['name'])).replace('<1>', str(json_file['intents'][key]['samples']))
                    print(body)
                else:
                    body= devsets.skill_template.replace('<0>', gsx(json_file['intents'][key]['name'])).replace('<1>', str(json_file['intents'][key]['outputs']))
                    print(body)
                f=open(name, 'w+')
                f.write(body)
                f.close()
                print('[*] Done.')
            elif t_=='webscrape':
                body=devsets.web_scraper_skill_template
                print(body)
                
intent_maker('reply_noreask_nodialgue_handler', ['niente', 'nulla', 'bene'], synsout=False, extraconts=['ah, va bene', "d'accordo", 'okk', 'ook'])
print('[*] Derivating...')
derivate(l_=['Reply_noreask_nodialgue_handlerIntent'])