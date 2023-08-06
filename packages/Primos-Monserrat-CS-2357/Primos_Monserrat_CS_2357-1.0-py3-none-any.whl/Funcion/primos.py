import os
os.environ["R_HOME"]=r"C:\Program Files\R\R-4.2.1"
import rpy2.robjects as ro
codigo_en_r ="""
primos<- function(n){
  for(i in 2:n){
      j=2
      primo=1
      while (j<i){
          if (i%%j==0){
              primo=0
          }
          j=j+1
      }
      if(primo==1){
          print(i)
      }
  }
}
"""
ro.r(codigo_en_r)
primos_py=ro.globalenv['primos']