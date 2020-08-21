__principio di elaborazione__

x -> input
if x in InvocationNames: esegui la skill con x come InvocationName
y -> output = exec(skill)

*gli invocnames non sono tutti in una lista, quindi bisotgna iterare su 
tutti gli intent nel mainfile json*

# Derivatore

### sintassi:

```python
derivate(l_=["IntentName"], t_="skill_type", jpath='path for json source file', ppath='output path')
```
1. `skill_type` indica il tipo di skill, può essere:
    1. `echo` per le skill botta e risposta
    1. `webScrape` per le skill con ricerca su google`

fra gli [intents]() deve esserci "IntentName", per crearlo usa:

```python
intent_maker('hello', ['input1', 'input2'])
```
oppure:
```python
intent_maker('hello', ['in1', 'in2'], synsout=False, extraconts=['out1', 'out2'])
```
con il secondo metodo se l'utente scrivesse in1 o in2 hy risponderà casualmente con out1 o out2.

invece nel primo esempio scrivendo input1 o input2 hy risponderà casualmente con input1 o input2. questo può essere utile quando l'utente saluta e bisogna di salutarlo, tipo 
> "ciao"

> "ciao" 

ma se ad un 
> "che fai"

hy rispondesse 
 
 >"come stai"
 
sarebbe un problema.

_
# HYBRID
## hypermark making

la funzione `get_skillex(x)` dall'unità di processo per gli input ritorna x la cui ultima lettera è "a".

ad esempio, con
```python
from lib.input_processing_utils import get_skillex
print(get_skillex('saluti'))
```
si avrà come output "saluta" che è una parola sensata. se per esempio si passa
> get_skillex("AskHandler")

si avrà
> "AskHandlea"

anche se la parola non è sensata hybrid andrà ad eseguire comunque la skill salvata con "AskHandlea".

## hypermark predicting
dato un input `x` hybrid cerca nel suo dataset un [Intent]() che abbia `x` nella lista chiamata ["samples"]().

### python:
```python
#<0>
import time, random
random.seed(time.time())
c=[]
print (c[random.randint(0, len(c)-1)])
```
### json:
```json
{
    "name":"nome",
    "samples":[]
}
```
adesso ottengo un input:
> ## x=input('>> ').casefold().replace('?', '')
trova il file taggato con hypermark f(x):
```python
import json
d = json.loads("filepath.json")
if x in d['samples']:
    do(x)

def do(x):
    f=lambda y: y[len(y)-1]='a' #sostitusici l'ultima lettera con una 'a'
    #trova il file indicizzato con f(x)