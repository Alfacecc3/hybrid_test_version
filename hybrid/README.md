__principio di elaborazione__

x -> input
if x in InvocationNames: esegui la skill con x come InvocationName
y -> output = exec(skill)

*gli invocnames non sono tutti in una lista, quindi bisotgna iterare su 
tutti gli intent nel mainfile json*