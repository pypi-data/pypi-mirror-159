import rpy2.robjects as ro

sumaEnteros_r = """
sumaEnteros <- function(n, m){
    print(n + m)
}
"""

ro.r(sumaEnteros_r)

sumaEnteros = ro.globalenv['sumaEnteros']

restaEnteros_r = """
restaEnteros <- function(n, m){
    print(n - m)
}
"""

ro.r(restaEnteros_r)

restaEnteros = ro.globalenv['restaEnteros']

primos_r = """
primos <- function(n){
    for (i in 0:n) {
        contador <- 0
        for (j in 0:i) {
            if (i %% (j+1) != 0){
                next
            } else {
                contador <- contador + 1
                if (contador == 3) {
                } else if (contador < 3 && j == i-1 && i != 1) {
                    print(i)
                }
            }
        }
    }
}
"""

ro.r(primos_r)

primos = ro.globalenv['primos']


