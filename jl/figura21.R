library(stats)
n <- 150
d <- 100000
X <- matrix ( runif ( n * d , min = 0 , max = 1) , nrow = n , ncol = d)
epsilon <- 0.1
k <- ceiling (4 * log( n ) / ( ( epsilon ^2)/2 -( epsilon ^3)/3 ) )
k
sample_pairs <- combn (n , 2)
Phi <- matrix ( rnorm ( k * d , mean = 0 , sd = 1 / sqrt ( k ) ) , nrow = k,ncol = d )
Z <- X %*% t( Phi )
rm(Phi); gc()

selected_pairs <- sample(ncol(sample_pairs), 500)
pairs <- sample_pairs[, selected_pairs]

D_original <- apply(pairs, 2, function ( pair ) {
    i <- pair [1]; j <- pair [2]
    sqrt(sum((X[i, ] - X[j , ])^2) )
})

D_proj <- apply (pairs , 2 , function ( pair ) {
    i <- pair [1]; j <- pair [2]
    sqrt (sum (( Z [i , ] - Z [j , ]) ^2) )
})

R <- D_proj / D_original

cumplen <- (R >= (1 - epsilon ) ) & (R <= (1 + epsilon ) )
porcentaje_cumple <- mean(cumplen) * 100

cat(sprintf("Porcentaje de pares proyectados a la dimension %d que cumplen la cota: %.3f%%\n",k , porcentaje_cumple))

plot(R, pch=19, col = ifelse ((R >= (1 - epsilon ) ) & (R <= (1 + epsilon ) ) , " darkgreen ", "red ") ,
    main = sprintf("Distorsion de las distancias proyectadas (k = %d)", k),
    xlab = "Indice del par de puntos ", ylab = "R = || Tu(xi) - Tu(xj)|| / || xi - xj ||",
    ylim = c(min (R, 1 - epsilon ) - 0.05 , max (R, 1 + epsilon ) +0.05) )

abline ( h = 1 - epsilon , col = " blue ", lty = 2 , lwd = 2)
abline ( h = 1 + epsilon , col = " blue ", lty = 2 , lwd = 2)
abline ( h = 1 , col = " black ", lty = 1 , lwd = 1)
