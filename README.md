# --- UNDER DEVELOPMENT ---
Released on:
- [Github](https://github.com/cgifl300/OCP09/)
- [Framagit](https://framagit.org/cgifl300/litreview/)
- [SDF - Gitea](https://git.sdf.org/elec/LITReview)


# LITReview OC_P09
A Django app for studies. The purpose is to release a MVP based on the django
framework and to release it on heroku cloud.

# Prerequisite
I suppose you ever installed python and git before.  
If not consider doing it:  
[python](https://www.python.org/)  
[git](https://www.git-scm.com/)  
# Setup
## Environment Setup
### Cloning the project
Go into your source directory  
`cd ~/src`  
Then start cloning  
`git clone https://github.com/cgifl300/OCP09`  
### Create the venv and install the requirements
Enter the cloned directory  
`cd OCP09`  
`python -m venv venv`  
Activate the venv for linux, bsd or macOS  
`source venv/bin/activate`  
Activate the venv for windows  
`.\venv\Scripts\activate.bat`

### Install requirements

`pip install -r requirements.txt`

# DEV

Development in progress, see [what happen here](kanban.md)

### Internal notes:

- Problem in the db UML Diagram:   
  Hotfixes - Ticket.time_created option auto_add_now didn't exist, replaced by
  auto_now_add.
- Problem with model.py:  
  Hotfixes - body = models.CharField(max_length=8192, blank=True) to body =
  models.TextField(max_length=8192, blank=True) to stick the UML model.