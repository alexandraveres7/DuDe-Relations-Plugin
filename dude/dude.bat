set LOCALCLASSPATH=lib/gson.jar;classes;lib;
echo "Starting Dude..."
java -Xmx1024m -classpath %LOCALCLASSPATH% lrg.dude.duplication.DuDe config.txt