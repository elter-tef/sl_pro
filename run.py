from app import create
app = create()
@app.route('/')
def autors():
	return 'hello'
