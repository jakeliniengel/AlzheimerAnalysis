import os
import javabridge
import weka.core.jvm as jvm
import weka.core.serialization as serialization
from weka.core.converters import Loader
from weka.classifiers import Classifier

os.environ["_JAVA_OPTIONS"] = "-Dfile.encoding=UTF-8"
jvm.start(packages=True)
path = os.path.dirname(os.path.abspath(__file__))
objects = serialization.read_all(path+"\\naive_bayes_feminino.model")
classifier = Classifier(jobject=objects[0])
loader = Loader(classname="weka.core.converters.ArffLoader")
data = loader.load_file(path+"\\teste.arff")
data.class_is_last()
for index, inst in enumerate(data):
   pred = classifier.classify_instance(inst)
   dist = classifier.distribution_for_instance(inst)
   print(str(index+1) + ": label index=" + str(pred) + ", class distribution=" + str(dist))
jvm.stop()


