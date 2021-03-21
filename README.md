# DuDe-Relations-Plugin

This project takes the output from an existing plugin named DuDe (Duplicate Detector) and creates a json with nodes and links. The nodes are files that have duplicated code and the links have a target and a source which represent two files with the same duplicated code block.

<h2 >Motivation</h2>
The reason for this project is to analyse a project folder of your choice by obtaining relations between files with the same duplicated code and seeing them graphically represented in DX Platform.

<h2 >Screenshots</h2>

![HIERARCHICAL EDGE BUNDLING](/graph1.png)

![FORCE DIRECTED GRAPH](/graph2.png)

<h2 >Requirements</h2>

You **MUST** have **Java 11/above** and **Python version 3.8/above** installed in order to run this project.

<h2 >Usage</h2>

<h4 >DX Platform</h4>

1. Install dx platform on your computer.
2. Go to the plugins directory in the dx platform project and create a folder named 'dude-relations'
3. Go to the directory where you have downloaded this project and modify the paths from deploy.sh script in order to fit the paths on your computer.
4. Run the deploy.sh script which you can find in the root folder of this project.
5. Run dx platform
`$ ./startDx.sh`
6. Open your favorite browser on **localhost:6060/index.html**
7. Open the project you wish to analyze.
8. Go to configurations and add a new configuration command for Dude Relations plugin. The command must have a name, a description and a root folder (the absolute path to the folder where your project exists).

_Example for root folder: /home/user/.dx-platform/projects/your_project_name_

9.Run the command.

10.Go to Relations in dx-platform and see the results. Well done!

<h4 >Standalone</h4>

Go to the root directory of this project and run the command below:

`$ python3 dude_relations_plugin.py result.json <absolute path to folder you wish to analyse>`

<h2 >Contributing</h2>
We are not open to new contributors.

<h2 >Credits</h2>

Thank you to the team that developed DuDe. Our project would not have been possible without your work!

https://wettel.github.io/dude.html
