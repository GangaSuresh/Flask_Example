from market import app

#check is run.py is executed directly not imported
if __name__=='__main__':
    app.run(debug=True)