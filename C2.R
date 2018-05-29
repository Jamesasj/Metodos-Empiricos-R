dados <- read.csv("~/Documents/Metodos-Empiricos-R/Tabela15.1.csv")
rl.regressao <- lm(dados$Y ~ dados$X)
plot(dados$Y ~ dados$X)
abline(rl.regressao)