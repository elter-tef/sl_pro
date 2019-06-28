import os
def degrade():
	d = os.getcwd().split('/')
	d = d[:len(d)] 
	d.append('app.db')
	os.remove('/'.join(d))
