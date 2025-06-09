# UWaterloo Steel Bridge Team SAP2000 Script

This repo contains code to automate the optimization of bridge designs by generating geometry and member properties in Python and porting them into SAP2000 using the SAP2000 Python API.

## Cloning the Repo
To clone the repo, open an instance of a terminal in the folder you want the code to go into. You can do this by right clicking in the folder, and there should be an option that says "Open in terminal".

Once in the terminal, type ```git clone https://github.com/duck-wad/SAP2000-API-Script.git``` and press enter, the code should clone into the folder.


## Dependencies
The packages required to run the script are in the requirements.txt file. I would recommend creating a virtual environment (I use Conda) to install the packages in, but not required.

Navigate into the folder with the Python files and open a terminal. If using a virtual environment, activate. Then type ``` pip install -r requirements.txt ``` and the packages should download. 
