LOCALCLASSPATH=lib/gson.jar:classes:lib:
echo "Starting Dude..."
java -Xmx12g -classpath ${LOCALCLASSPATH} lrg.dude.duplication.DuDe config.txt