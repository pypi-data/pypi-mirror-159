# Clubear
Clubear is a Python-based (Python 3) open-source package for interactive massive data analysis. The key feature of clubear is that it enables users to conduct convenient and interactive statistical analysis of massive data with only a traditional single-computer system. Thus, clubear provides a cost-effective solution when mining large-scale datasets. In addition, the clubear package integrates many commonly used statistical and graphical tools, which are useful for most commonly encountered data analysis tasks.

Every component (class) within clubear have a 'demo()' function. Demo is used to demonstrate typical examples about this class. Users can use 'demo()' to quickly get instructions. For example, if we have an object 'sf':
```
sf=cb.shuffle('airline.csv')
```
we can get the instructions related to it by:
```
sf.demon()
```
Then, a typical case will be printed for reference.


## How to use clubear
### 1. Install the package
```
pip install clubear
```

### 2. Import the package

We recommend to use clubear with Jupyter Notebook. This will lead to the best user experience.
```
import clubear as cb
```

### 3. Shuffle a dataset

For example, shuffle a CSV file 'airline.csv'. The resulting file is 'airline.csv.shuffle'.
```
sf=cb.shuffle('airline.csv')
sf.dc()
```

### 4. Use 'pump' to process data

Build a bridge between the dataset and the memory (of a computer) using a 'pump':
```
pathfile='airline.csv.shuffle'
pm=cb.pump(pathfile)
pm.subsize=10000
```

Then, one can quickly access a part of the dataset as:
```
pm.go()
```

Or view the most frequently used descriptive statistics as:
```
ck=cb.check(pm).stats()
```

### 5. Find quantitative variables

Extract variables whose 'mp' values are less than 5%:
```
ck[ck.mp<5].index
```

Pass this list to 'pm' by the 'qlist' parameter:
```
pm.qlist=[...]
```

### 6. Discover levels for qualitative variables

Detect all levels by the 'table' function as:
```
tb=cb.check(pm).table(niter=100)
```

Detect all levels for a specified variable, e.g., 'AirTime':
```
tb=cb.check(pm).table('AirTime',tv=True)
```

### 7. Make statistical graphics

Clubear provides a number of graphical tools. For example, boxplot:
```
tk = cb.tank(pm)
pt=cb.plot(tk).box(x="Year",y="ArrDelay")
```

Histogram:
```
pt=cb.plot(tk).hist('Distance')
```

Barplot:
```
pt=cb.plot(tk).mu('ArrDelay','CRSDepTime')
```


