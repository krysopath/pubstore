import pubstore as pbs

if __name__ == '__main__':
    pbs.init_db()
    pbs.app.run(debug=True)

