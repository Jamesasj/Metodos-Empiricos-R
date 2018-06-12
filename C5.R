dados     <- read.csv("~/Documentos/Metodos-Empiricos-R/BAEZA3.1.csv", header=TRUE, sep=";")
dados$total <- rowSums(dados[2:5])
dados$TF <- 1 + log2(dados$total)

dados$documentos <- rowSums(dados[2:5] > 0)
dados$IDF <- log2(4/dados$documentos)


dados$TFIDF <- dados$TF * dados$IDF 
dados <- dados[order(-dados$TF),]



plot(dados$TF , col = "green", pch = "+", cex = 1, lty = "solid", lwd = 2)
points(dados$IDF, col = "red", pch = "x", cex = 1, lty = "solid", lwd = 2)

plot(dados$TFIDF~ dados$IDF,   col="blue", pch = "x", cex = 1, lty = "solid", lwd = 2)