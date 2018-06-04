dados <- read.csv("C:/PROJETOS/Metodos-Empiricos-R/Tabela15.1.csv")
ANOVA <- aov(dados$Y~dados$X, data =  dados)

IC.ALFA <- function(coefciente, anova){
  parametros <- ncol(anova$model)
  tamanho <- nrow(anova$model)
  grau_liberade = tamanho - parametros
  sAnova<-summary(anova)[[1]]
  tabela <- anova$model
  mediaX <- mean(tabela$`dados$X`)
  
  Tx <- qt((1-coefciente)/2,df =  grau_liberade ,lower.tail = FALSE)
  Se <- sqrt(sAnova[2,3])
  alfa <- anova$coefficients[1]
  x2 <- sum(tabela$`dados$X`^2)
  X_mediaX2 <- sum((tabela$`dados$X` - mediaX)^2)
  
  
  Resultado.x1 <- alfa + Tx * Se * sqrt(x2/(X_mediaX2*tamanho))
  Resultado.x2 <- alfa - Tx * Se * sqrt(x2/(X_mediaX2*tamanho))
  
  return(c(Resultado.x1, Resultado.x2))
}

vRes <- IC.ALFA(.950, ANOVA)