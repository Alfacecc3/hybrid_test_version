import os
def make_skill(name: str, contents: str):
    n=0
    for filename in os.listdir('skills/'):
        n+=1
    skillname='skill_'+str(n)+'.py'
    base = open('dataset/skill_template.txt').read(); i=0
    out=base.replace('<0>', name).replace('<1>', contents)
    f=open('skills/'+skillname, 'w+')
    f.write(out)
    f.close()

def read_skills(path='skills/'):
    d={}
    for filename in os.listdir(path):
        d[open(path+filename).read().split('\n')[0]] = open(path+filename).read()
    return d
