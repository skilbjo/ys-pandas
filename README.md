# ys-pandas

## Install
`git clone git@github.com:skilbjo/ys-pandas`

## How to use `virtualenv` and `virtualenvwrapper`

Create the `virtualenv`:
`$ mkvirtualenv data`

Show the `virtualenv`'s:
````bash
$ lsvirtualenv
data
====
````

Start the `virtualenv`:
````
$ workon data
$ (data)ys-pandas
````

Install the dependencies:
`pip install -r requirements.txt`

Stop the virtualenv
`$ deactivate`

## Data for Analysis
### SQL
````sql
		select
			cast(dateadd(d,  0, dateadd(d, -1 , dateadd(mm, (Year - 1900) * 12 + Month, 0))) as date) as Date, *
		from 
			ETLStaging..FinanceAnalytics
````

## Run in console
`$ python analysis.py`

## Run in iPython
`$ ipython notebook analysis.ipynb %matplotlib inline`

### Useful iPython shortcuts

|   Shortcut  |         Action         |
|:-----------:|:----------------------:|
| Shift-Enter |        run cell        |
|  Ctrl-Enter |    run cell in-place   |
|  Alt-Enter  | run cell, insert below |
|   Ctrl-m x  |        cut cell        |
|   Ctrl-m c  |        copy cell       |
|   Ctrl-m v  |       paste cell       |
|   Ctrl-m d  |       delete cell      |


