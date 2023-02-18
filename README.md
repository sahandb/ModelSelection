# ModelSelection
implement KFold function from scratch

you can called it crossValidation Split or kfold


Here I implement one of the famous approaches of cross validation. Ten-Time-Ten-Fold. Implemented function below that takes the whole data and returns a ten-column matrix of indices for test parts:

//TenFoldsfunction takes whole data and returns indices of test patterns in the columns of matrix M.
M=Tenfolds(data)

To apply Ten-Time-Ten-Fold., you have to use above function ten times.
