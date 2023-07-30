from search_service import app
if __name__ == "__main__":
    app.run(port='4001')
    #app.run(debug=True, passthrough_errors=True, use_debugger=False, use_reloader=False)