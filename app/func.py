import os
def degrade():
	d = os.getcwd().split('/')
	d = d[:len(d)] 
	d.append('app.db')
	os.remove('/'.join(d))

def js_dict(u, delite = '_sa_instance_state'):
	d = dict(u.__dict__)
	del d[delite]
	return d
