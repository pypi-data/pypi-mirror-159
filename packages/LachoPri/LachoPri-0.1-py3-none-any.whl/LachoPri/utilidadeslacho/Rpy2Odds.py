import rpy2
from rpy2.robjects.packages import importr
base = importr('base')
utils = importr('utils')
rpy2.robjects.r('''
    f <- function(r, verbose=FALSE){
    optimus <- c()
    p <- 2:r
    for (i in p){
        prime <- 1
        sqrt <- ceiling(i^0.5)+1
        for(j in 2:sqrt){
            if (i%%j==0 && i!=j){ 
                prime <- 0
            }
        }
        if (prime == 1){
            optimus <- append(optimus,i)      
        } 
    }
    return(optimus)
}        
''')
r_f = rpy2.robjects.globalenv['f']

#print(r_f.r_repr())

def calcularpris(n):
    resultlist = r_f(n)
    return resultlist



