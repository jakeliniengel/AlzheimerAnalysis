import os
import javabridge
import weka.core.jvm as jvm
import weka.core.serialization as serialization
from weka.core.converters import Loader
from weka.classifiers import Classifier
from blog.models import Alzheimer

class percentagemAlzheimer():
   def functionProcessamento(self, ca1_r, ca1_l, ca2_ca3_r, ca2_ca3_l, sub_r, sub_l, sexo, id):
      jvm.start()
      path = os.path.dirname(os.path.abspath(__file__))
      # TODO: verificar qual o sexo do individuo para carregar o modelo corretamente
      modelo = path+"\\naive_bayes_feminino_novo.model"
      if(sexo=="Male"):
         print("É masculino")
         modelo=path+"\\naive_bayes_feminino_novo.model"
      objects = serialization.read_all(modelo)
      classifier = Classifier(jobject=objects[0])
      loader = Loader(classname="weka.core.converters.ArffLoader")
      arquivo = open(path+"\\novo_individuo.arff", "w")
      conteudo = list()
      conteudo.append("@relation alzheimer \n\n")
      conteudo.append("@attribute doente {SIM, NAO} \n")
      conteudo.append("@attribute ca1_right real \n")
      conteudo.append("@attribute ca1_left real \n")
      conteudo.append("@attribute ca2_ca3_right real\n")
      conteudo.append("@attribute ca2_ca3_left real \n")
      conteudo.append("@attribute subic_right real \n")
      conteudo.append("@attribute subic_left real \n\n")
      conteudo.append("@data \n")
      #aqui passar as variáveis 
      conteudo.append("SIM,"+ str(ca1_r)+","+str(ca1_l)+","+ str(ca2_ca3_r)+","+ str(ca2_ca3_l)+","+str(sub_r)+","+str(sub_l))
      print(conteudo)
      arquivo.writelines(conteudo)
      arquivo.close()

      data = loader.load_file(path+"\\novo_individuo.arff")
      data.class_is_last()
      for index, inst in enumerate(data):
         pred = classifier.classify_instance(inst)
         dist = classifier.distribution_for_instance(inst)
         pc_doenca = round(((pred) * 100),2)
         pc_saudavel = round(((100 - pc_doenca)),2) 
         print(" Porcentagem de alzheimer=" + str(pc_doenca) + "%, porcentagem saudavel=" + str(pc_saudavel) + "%")
         alzheimer = Alzheimer.objects.get(id=id)
         alzheimer.resultado_ad = pc_doenca
         alzheimer.resultado_cn = pc_saudavel
         alzheimer.status_seg = 2
         alzheimer.save()
      jvm.stop()



