FROM openkbs/jdk11-mvn-py3

WORKDIR /dude-relations

COPY dude_relations_plugin.py dude_relations_plugin.py
COPY dude dude
COPY result.json result.json

ENTRYPOINT ["sudo", "python3", "dude_relations_plugin.py", "result.json"]
