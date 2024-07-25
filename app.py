from main import control
app=control.create_app()
with app.app_context():
    control.db.create_all()

if __name__=='__main__':
    app.run(debug=True)
