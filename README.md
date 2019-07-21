# Fama-French Decomposer
Fama-French Model used to analyse and decompose Berkshire Hathaway's returns. The program runs a Linear Regression of Berkshire Hathaway's returns against Fama-French 49 Industry Portfolios (Availiable at http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html), and randomly drops unsignificant regressors until the F-Statistic and Adjusted R² values aren't inceasing significantly (Caped at a minimum of 5 explanatory variables)

TODO:
- Doesn't keep most optimal model (2nd best), have to fix loop
- Separate FF Factors and Berkshire Hathaway's returns & find a way to import more data (to be able to decompose any Hedge Fund's most significant investments / risk factors)
