# DuDe-Relations-Plugin

DuDe is a text-based, language-independent code duplication (code clones) detector, gravitating around the concept of duplication chain.

This project takes the output from DuDe and creates a json with nodes and links. The nodes are files that have duplicated code and the links have a target and a source which represent two files with the same duplicated code block.

<h2 >Motivation</h2>
The reason for this project is to analyse a project folder of your choice by obtaining relations between files with the same duplicated code and seeing them graphically represented in DX Platform.

<h2 >Screenshots</h2>
In DX Platform Relations you would get something like this:

![HIERARCHICAL EDGE BUNDLING](/graph1.png)

![FORCE DIRECTED GRAPH](/graph2.png)

<h2 >Requirements</h2>

You **MUST** have **Java 11/above**, **Python version 3.8/above** and **bash** installed in order to run this project.

<h2 >Usage</h2>

<h4 >DX Platform</h4>

After you clone this repository or download the zip, follow the steps below:

1. Download and install [DX-Platform](https://drive.google.com/file/d/1bC4ZJ_RVcGJezAHZ45AIF8UKAh3gG3NY/view) on your computer. Follow the README for installation guidelines.
2. Import your desired project to DX Platform following the guidelines from it's README.
3. Go to the plugins directory in the DX Platform project and create a folder named 'dude-relations'
4. Go to the directory where you have downloaded this project and modify the paths from deploy.sh script in order to fit the paths on your computer.

_Example: on the first line we copy the plugin-info.json from this project to the plugins directory in DX Platform so you would get something like this_

  **cp /home/user/DuDe-Relations-Plugin/plugin-info.json** (the absolute path to the json file on your computer) **/home/user/.dx-platform/plugins/plugin-info.json** (the absolute path to the file in plugins directory of dx - you can name this file however you want i chose plugin-info for consistency)
  
5. Run the deploy.sh script which you can find in the root folder of this project.
6. Run dx platform
`$ ./startDx.sh`
7. Open your favorite browser on **localhost:6060/index.html**
8. Open the project you wish to analyze.
9. Go to configurations and add a new configuration command for Dude Relations plugin. The command must have a name, a description and a root folder (the absolute path to the folder where your project exists in dx platform).

_Example for root folder: /home/user/.dx-platform/projects/your_project_name_

10.Run the command.

11.Go to Relations in dx-platform and see the results. Well done!

<h4 >Standalone</h4>

After you clone this repository or download the zip, follow the steps below:

Go to the root directory of this project and run the command:

`$ python3 dude_relations_plugin.py result.json <absolute path to folder you wish to analyse>`

**You will see the results in the result.json file.**

<h4 >Docker</h4>

You can also get this project as a Docker container from [DockerHub](https://hub.docker.com/r/alexandraveres7/dude-relations)

To get the container:

`$ docker pull alexandraveres7/dude-relations`

To run the container use the command below:

`$ docker run -v <path to folder you want to create relations for>:/ale -v <path to folder you wish to see results in/result.json>:/dude-relations/result.json alexandraveres7/dude-relations`

**You will see the results in the result.json file.**

<h2 >Contribute</h2>
We are not open to new contributors.

<h2 >Credits</h2>

Thank you to the team that developed DuDe. Our project would not have been possible without your work!

https://wettel.github.io/dude.html

<h2 >License</h2>

 Copyright 2021 Alexandra Veres & Norica Bacuieti

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
