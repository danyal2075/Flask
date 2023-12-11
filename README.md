# How to start the project

- import Flask
- Create its instance
- pass condition instance = run(debug=True)
- Creating route()
  - Pass a function which performs certain action
  - render_templates()
  - pass the data Dict


- To send the data from back end into front end
  - {{dict_name.key_name}}


- To sent data from front end into back end
  - sending data from one page into another
  
  - Method[POST , GET]
    - POST: is use to send data
      - So i need to pass it in the form
    - GET: is used to receive data
  - request() : from where want to get the value

  - Note: Check the commit what are changed. How it is implemented

- jsonify
  - use to pass the data in Dict format


- App2.py:
  - Jinja Formatting is used

- dbapi.py:
  - Contains database connection
  - Syntax 




Project Plan:

Project Main Folder:

- Project Code Folder : Create repo of this folder. it includes codes, requirements, README.md etc. Never include venv folder inside the git folder.
  - Main.py
  - requiements.txt
  - .gitignore : This file inculdes all those files or dic which we donot want to upload into git. Please see the file to find how to write it
  - README.md
  - and all other supporting files
- venv folder


Creating conda env 
  conda create -p (envname) 