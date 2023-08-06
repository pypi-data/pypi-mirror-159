import rpy2.robjects as ro

n_primos = input('¿Cuantos numeros primos desea calcular? ')
rFuntion = """
                calculo_num_primos <- function(n_primos) 
                {
                    ncontrol    <- 0
                    i           <- 0
                    # while (ncontrol != n_primos) # Saca los n numeros primos
                    while (i != n_primos)          # Saca los primos del 1 a n
                    {
                        i           <- i + 1
                        ndivisiones <- 0
                        for (j in 1:i)
                        {
                            if (i%%j == 0)
                            {
                                ndivisiones <- ndivisiones + 1
                            }    
                        }

                        if (ndivisiones <= 2)
                        {
                                print(i)
                                ncontrol <- ncontrol + 1
                        }
                    }
                }
            """

ro.r(rFuntion)

numerosPrimos = ro.globalenv['calculo_num_primos']
numerosPrimos(n_primos)

