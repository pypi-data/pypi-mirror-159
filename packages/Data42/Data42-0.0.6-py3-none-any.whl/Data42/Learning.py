import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE

def generar_muestras_balanceo(dataset, columna):
    """ Esta función permite crear muestras sintéticas, a partir de conjuntos de datos de clasificación desequilibrados.
        Para emplear esta función es necesario (import : Numpy, pandas, from imblearn.over_sampling import SMOTE)
        Se ayuda de la función SMOTE (Tecnica de sobremuestreo de minorias sintéticas)
        Se basa en la creación de muestras sinteticas, en el grupo/grupos minoritario(s).
    Parameters:
            -dataset: Set de datos desbalanceado
            -columna: Tiene que estar incluída en el set de datos desbalanceado, puede ser de tipo "string" ó "númerico". 
                      Esta columna representara a la clase o grupo que pertence mi muestra (ejemplo: Tipo, Clase, Grupo, Ypredict)
    
    Output: Regresa el dataset balanceado (el cual contiene las muestras originales, como las muestras creadas)
    """
    X= dataset.drop([columna],1)
    y= dataset[columna]

    smt= SMOTE(random_state=42)
    X_train_sm, y_train_sm = smt.fit_resample(X, y)

    dataset_balanceado= pd.concat([X_train_sm,y_train_sm], axis=1)
    
    return dataset_balanceado


def balanceado(df, target):
	'''
	Function to know how balanced a column is.
	Input:
	    - df: dataframe
	    - target: column
	Output: 
	    Dataframe with the categories of the column and their weight.  

	Libraries used:
	    import pandas as pd
	    import numpy as np    
	'''

	list_b = []
	for index, value in df[target].value_counts().items():
	    list_b.append({'Categoria': index, 'Peso': round(float(value )/ len(df[target])*100, 2)})

	return pd.DataFrame(list_b)


def correlation_coeff(dataset,threshold):
    ''' 
        The correlation coefficient is a statistical measure of the strength of the relationship 
        between the relative movements of two variables.
        Parameters X_train ,Threshold where threshold is 
        the maximimum percent in correlation in the independants variables will be high correlated.
        X_train is the dataset, in this case we just interestd on the indepedant features, that wy we use X_train.
        threshold values must bue from 0 to 1 like, 0.5, 0.7, 0.9.
        Function will return witch variable have a high correlation in indepeant features.
    '''
    col_corr = set() #Set of all the names of corralated columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if corr_matrix.iloc[i, j] > threshold: # we are interested in absolute coeff value
                colname = corr_matrix.columns[i] #guetting the name of column
                col_corr.add(colname)
    return col_corr


def balance_observation(df, target):
    '''
    Function to know the balance classes.
    Input:
        - df: dataframe
        - target: column
    Output: 
        Dataframe with the categories of the column and their weight.  

    Libraries used:
        import pandas as pd
        import numpy as np    
    '''

    new_list = []
    for index, value in df[target].value_counts().items():
        new_list.append({'Category': index, 'Weight': round(float(value )/ len(df[target])*100, 2)})

    return pd.DataFrame(new_list)


def replace_missings_train_test(X_test, X_train, col):
    '''
	Function to eliminate or replace missings. This version is for dataframes that have been separated into train and test.
	The user is asked for the dataframe and the column that they want to act on, and they are given options to choose what they want to
	do with the missings.

	Parameters:
	                - df: dataframe
	                - col: column you want to modify

	Libraries used:
	    import pandas as pd
	    import numpy as pd                
	'''

    tipo = str(X_test[col].dtype)
    if 'int' in tipo or 'float' in tipo:
        op = str(input("Enter Mean to change your missings to the mean or Median to change them to the median"))
        if op.lower() == "mean":
            X_train[col] = X_train[col].fillna(X_train[col].mean())
            X_test[col]  = X_test[col].fillna(X_train[col].mean())
            print("The missings of your column have been replaced by the mean of train on train and test sets")
        elif op.lower() == "median":
            X_train[col] = X_train[col].fillna(X_train[col].median())
            X_test[col]  = X_test[col].fillna(X_train[col].median())
            print("The missings of your column have been replaced by the median of train on train and test sets")
    else:
        print("Your variable is not numerical, changing the missings in train and test sets by the mode of train...")
        X_train[col] = X_train[col].fillna(X_train[col].mode().iloc[0])
        X_test[col]  = X_test[col].fillna(X_train[col].mode().iloc[0])
        print("The missings of your column have been replaced in train and test sets by the mode of train")