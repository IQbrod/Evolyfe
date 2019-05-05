# Evolyfe
Life simulation with Python  
  
# 0. Setup  
Install: [pip](https://pypi.org/project/pip/), [python3.x](https://www.python.org/downloads/), [matplotlib](https://matplotlib.org/users/installing.html)  
  
# 1. Simulate life  
Create your specie
```python
sp = Specie("Name",B,R,D)
#B: Spontaneous Birth Rate
#R: Replication Rate
#D: Death Rate
```
Create your population
```python
pop = Population(sp, N)
#sp: Specie
#N: Number of existing creatures at time 0
```
Let your population evolve
```python
for _ in range(T):
        pop.progress()
#T: Number of iteration for you population to evolve
#pop: Population
```
Show the results
```python
app = App()
app.displayPop(pop)
app.mainloop()
#pop: Population to display

#Red Curve: Evolution Prediction
#Black Curve: Evolution of your Population
```
## 1.1 Compare to the average
```python
app = App()
app.displayPop(pop, Q)
app.mainloop()
#Q: Number of population to get an average curve

#Green Curve: Average of the N populations with same specie and same existing creatures at time 0
```

## 1.2 Understand
To Be Continued :)
