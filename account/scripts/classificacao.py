import os
import javabridge
import weka.core.jvm as jvm
import weka.core.serialization as serialization
from weka.core.converters import Loader
from weka.classifiers import Classifier

class percentagemAlzheimer():
   def functionProcessamento(self, ca1_r, ca1_l, ca2_ca3_r, ca2_ca3_l, sub_r, sub_l, sexo):
      jvm.start()
      # TODO: verificar qual o sexo do individuo para carregar o modelo corretamente
      modelo = "naive_bayes_feminino_novo.model"
      if(sexo=="Male"):
         print("É masculino")
         modelo="naive_bayes_feminino_novo.model"
      objects = serialization.read_all(modelo)
      classifier = Classifier(jobject=objects[0])
      loader = Loader(classname="weka.core.converters.ArffLoader")

      arquivo = open("teste2.arff", "w")

      conteudo = list()
      conteudo.append("@relation alzheimer \n")
      conteudo.append("@attribute doente {SIM, NAO} \n")
      conteudo.append("@attribute ca1_right real \n")
      conteudo.append("@attribute ca1_left real \n")
      conteudo.append("@attribute ca2_ca3_right real\n")
      conteudo.append("@attribute ca2_ca3_left real \n")
      conteudo.append("@attribute subic_right real \n")
      conteudo.append("@attribute subic_left real \n")
      conteudo.append("@data \n")
      #aqui passar as variáveis 
      conteudo.append("SIM,"+ ca1_r+","+ca1_l+","+ ca2_ca3_r+","+ ca2_ca3_l+","+sub_r+","+sub_l)
      arquivo.writelines(conteudo)
      arquivo.close()

      data = loader.load_file("novo_individuo.arff")
      data.class_is_last()
      for index, inst in enumerate(data):
         pred = classifier.classify_instance(inst)
         dist = classifier.distribution_for_instance(inst)
         pc_doenca = round(((pred) * 100),2)
         pc_saudavel = round(((100 - pc_doenca)),2) 
         print(" Porcentagem de alzheimer=" + str(pc_doenca) + "%, porcentagem saudavel=" + str(pc_saudavel) + "%")
         return (pc_doenca, pc_saudavel)
      jvm.stop()



