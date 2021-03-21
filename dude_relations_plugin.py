import os
import sys
import time
import subprocess
import csv
import json


class Graph:
  def __init__(self, nodes: list, links: list):
    self.nodes = nodes
    self.links = links


class GraphNode:
  def __init__(self, name: str):
    self.name = name
    self.component = 1


class GraphLink:
  def __init__(self, source: str, target: str, value: int):
    self.source = source
    self.target = target
    self.value = value


class Result:
  def __init__(
      self,
      name: str,
      description: str,
      visualTags: list,
      entity: str,
      timestamp: int,
      content: Graph,
  ):
    self.name = name
    self.description = description
    self.entity = entity
    self.visualTags = visualTags
    self.timestamp = timestamp
    self.content = content
  
  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)


class DuDeRelations:
  def run_dude(self) -> None:
    current_dir = os.getcwd()
    os.chdir(current_dir+"/dude/")
    process = subprocess.Popen("/bin/bash " + current_dir + "/dude/dude.sh", shell=True)
    process.wait()
    os.chdir(current_dir)
  
  def config_path_to_folder(self, base_folder_path) -> None:
    
    with open("dude/config.txt", "r") as config_file:
      lines = config_file.readlines()
    lines[1] = "project.folder=" + base_folder_path + "\n"

    f = open("dude/config.txt", "w")
    f.writelines(lines)
    f.close()
  
  def get_dude_list(self):
    with open("dude/config.txt", "r") as config_file:
      lines = config_file.readlines()
    config_project_name = lines[0]
    project_name = config_project_name.split("=").pop().replace("\n", "")
    
    with open("dude/" + project_name + "-duplication.csv", "r") as file:
      duplication_list = [row for row in csv.reader(file)]
    
    return duplication_list
  
  def get_nodes(self, dude_list):
    nodes_names = []
    if len(dude_list) > 0:
      for pair in dude_list:
        first_file = pair[0]
        if first_file not in nodes_names:
          nodes_names.append(first_file)
        second_file = pair[1]
        if second_file not in nodes_names:
          nodes_names.append(second_file)
    nodes = [GraphNode(name) for name in nodes_names]
    
    return nodes
  
  def get_links(self, dude_list):
    links = []
    for list in dude_list:
      file_source = list[0]
      file_target = list[1]
      nr_of_duplicated_lines = list[2]
      links.append(GraphLink(file_source, file_target, nr_of_duplicated_lines))
    
    return links


if __name__ == "__main__":
  
  if len(sys.argv) < 2:
    print("Invalid number of arguments!")
    sys.exit(-1)
  
  output_file_path = sys.argv[1]
  base_folder_path = sys.argv[2]
  
  dude_relations = DuDeRelations()
  dude_relations.config_path_to_folder(base_folder_path)
  
  dude_relations.run_dude()
  dude_list = dude_relations.get_dude_list()

  nodes = dude_relations.get_nodes(dude_list)
  links = dude_relations.get_links(dude_list)
  graph = Graph(nodes=nodes, links=links)
  visual_tags = ["digraph", "hierarchical-edge-bundle", "forced-layered-graph"]
  time_in_millisec = int(round(time.time() * 1000))

  result = Result(
    name="DuDe Relations",
    description="A plugin for creating relations between files with the same duplicated code.",
    entity="FILES",
    visualTags=visual_tags,
    timestamp=time_in_millisec,
    content=graph,
  )

  result_json_formatted = result.toJSON()
  f = open(output_file_path, "w")
  f.write("[")
  f.write(result_json_formatted)
  f.write("]")
  f.close()
