import matplotlib.pyplot as plt
import seaborn as sns
from math import ceil
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from scipy.stats import skew

def grid_plot(df, y, hue=None, title_num= None, title_cat=None, 
            title_size= 11, axes_fontsize=9, fontweight= 'bold', 
            color_obj='MediumSeaGreen',color_num= 'MediumOrchid', save=None):

    '''
    The objetive of this function is to show the relationship between each of the attributes of X with respect to target.
    It also allows to include 'hue' to group by categories.

    In the case of non-categorical variables it generates scatterplots and if they are categorical it generates histograms.

    The function allows you to enter a title for categorical graphs and another for non-categorical graphs.

    You can also change the font size and width, the colors of the graphs and decide whether to save them.

    To run the function correctly it is mandatory to import the following libraries: seaborn, matplotlib.pyplot, pandas and 
    from math import ceil.  

    It returns each of the graphs in grid format.
    '''

    fig = plt.figure(figsize=(15,15))
    fig.subplots_adjust(hspace=0.4, wspace=0.4)

    if ceil(len(df.columns)/3) < 1:
        mnrows = 1
    else:
        mnrows = ceil(len(df.columns)/3)

    if mnrows < 3:
        mncols=mnrows
    else:
        mncols = 3

    for i, column in enumerate(df.columns):
        ax = fig.add_subplot(mnrows, mncols, i + 1)
        if df.dtypes[column] != object:

            sns.scatterplot(x = df.iloc[:,i], y = y, ax= ax, hue= hue, color=color_num)
            ax.set_title(title_num, fontsize=title_size)
            ax.set_xlabel(column, fontsize=axes_fontsize, fontweight= fontweight)

        else:
            df[column].value_counts().plot(kind="hist", ax= ax, color=color_obj)
            ax.set_title(title_cat, fontsize=title_size, fontweight= fontweight)
            ax.set_xlabel(column, fontsize=axes_fontsize, fontweight= fontweight)

    plt.show();
    
    if save != None:
        text= input('Enter the name you want to save the image: ')
        plt.savefig('./{}.png'.format(text))


def plot_predictions(ind_x, y_test, pred, title_x= '',title_y= '', new_prediction_x=None, new_prediction=None, save=None):

    '''
    The objective of this function is to plot in a graph the values of y_test with respect to the predictions made with the ML model.

    It is mandatory to put the index of X, y_test and the predictions.

    It is allowed to modify the title of the axes, enter a new prediction and save the plot.

    To enter the new prediction, it is necessary to input the X and y value of the new prediction.

    To run the function correctly it is mandatory to import the following libraries: matplotlib.pyplot and pandas.

    This function returns a dot plot with the entered values.
    '''

    plt.figure(figsize=(20, 7))
        
    p_df = pd.DataFrame()
        
    p_df['indiceX'] = ind_x
    p_df['real'] = y_test
    p_df['prediccion'] = pred

    x = p_df['indiceX']
    y1 = p_df['real']
    y2 = p_df['prediccion']

    plt.plot(x, y1,'gp',label='Actual', alpha=0.8)
    plt.plot(x, y2, 'mp', label='Prediction', alpha=0.5)
    
    if new_prediction != None:
        plt.plot(new_prediction_x, new_prediction, 'ko', label= 'New prediction')
        
    plt.title("Actual vs Prediction",fontsize=13)
    plt.xlabel(title_x,fontsize=11)
    plt.ylabel(title_y,fontsize=11)
    plt.xticks(rotation=70)
    plt.legend()

    plt.show();

    if save != None:
        text= input('Enter the name you want to save the image: ')
        plt.savefig('./{}.png'.format(text))


def correlation_test(df, color_phik= 'PiYG', color_p= 'coolwarm', save=None):

    '''
    The objective of this function is to have in a single code the heatmaps of the Pearson and Phik coefficients.

    It has as mandatory parameter a dataframe.
    The optional parameters are: change the color of any of the heatmaps and the option to save them.
    
    To run the function correctly it is mandatory to import the following libraries: seaborn, matplotlib.pyplot \
     and from phik import phik_matrix.
    
    This function returns each of the heatmaps correctly identified with the title.
    '''

    fig, axes = plt.subplots(2, 1, figsize=(15,10))
    plt.xticks(rotation = 90)
    sns.heatmap(df.phik_matrix(), cmap= color_phik, annot=True, ax= axes[0], linewidths=.5)
    axes[0].set_title(label= 'Correlation Phik', fontsize=14, fontweight= 'bold')
    
    sns.heatmap(df.corr(), cmap= color_p, annot=True, ax=axes[1], linewidths=.5)
    axes[1].set_title(label= 'Correlation Pearson', fontsize=14, fontweight= 'bold')
    
    plt.show();
    
    if save != None:
        text= input('Enter the name you want to save the image: ')
        plt.savefig('./{}.png'.format(text))


def c_mat(y_test, X_test, modelo, xticklabels=None, yticklabels=None, save= None):
    '''
    The y_test parameter must contain the y_test of the model being tested, just as the X_test must contain the X_test of the model being tested.

    The model parameter is the model for which we will represent the confusion matrix.

    xticklabels needs a list of labels to assign to the x-axis values. The default value is None.

    yticklabels needs a list of labels to assign to the y-axis values. The default value is None.
    
    The default save parameter is None, which reflects whether the graph will be saved or not.

    '''

    predictions = modelo.predict(X_test)

    c_mat = confusion_matrix(y_test, predictions)

    sns.heatmap(c_mat/c_mat.sum(axis=1),
                annot=True,
                cmap='Spectral',
                cbar=True,
                linewidths=3,
                linecolor='w',
                square=True,
                xticklabels=xticklabels,
                yticklabels=yticklabels)
    plt.show();
    
    print(classification_report(y_test, predictions))

    if save != None:
        text= input('Introduce el nombre con el que deseas guardar la imagen: ')
        plt.savefig('./{}.png'.format(text))


def data_report_numeric(df):
    '''
    Function to make a summary table of the numerical variables of the dataset.
    parameters:
            -df:dataframe
    Output:
            Dataframe with the following data for each column:
                  n_instances, mean, std, min, max, q25, q50, q75, missings (%), outliers (%) and skew
    Libraries:
            - import numpy as np
            - from scipy.stats import skew
    '''
    # to know which columns are numeric
    list_columns = df.select_dtypes(include=np.number).columns

    dict_num = {}    

    for columna in df[list_columns]:

        count = len(df[columna])
        percent_missing = round(df[columna].isnull().sum()*100 / len(df[columna]), 2)

        q25 = np.percentile(df[columna], 25)
        q50 = np.percentile(df[columna], 50)
        q75 = np.percentile(df[columna], 75)
        iqr = q75 -q25

        cutoff = iqr * 1.5
        lower = q25 - cutoff
        upper = q75 + cutoff
        
        # n outliers
        n_outliers = 0
        for x in df[columna]:
            if x < lower or x > upper:
                n_outliers += 1
            percent_outliers = round(n_outliers / count *100, 2)  

        mean = df[columna].mean()
        maximo = df[columna].max()
        minimo = df[columna].min()
        desv = df[columna].std()

        skew_column = skew(df[columna])

        dict_num[columna] = [count, mean, desv, minimo, maximo, q25, q50, q75, percent_missing, percent_outliers, skew_column]

    report_num_df = pd.DataFrame(dict_num, )
    report_num_df.index = ['n_instancess', 'mean', 'std', 'min', 'max', 'q25', 'q50', 'q75', 'missings (%)', 'outliers (%)', 'skew']

    return report_num_df


def data_report_categ(df):
    '''
    Function to make a summary table of the categorical variables of the dataset.
    parameters:
            -df:dataframe
    Output:
            Dataframe with the following data for each column:
                - number of observations
                - number of different categories
                - % cardinality
                - fashion
                - weight (%) of the mode
    Libraries:
            - import numpy as np
            - import pandas as pd               
    '''
    
    dict_cat = dict()

    for column in df:
        #if column not numeric
        if column not in df.select_dtypes(include=np.number).columns:

            n_observations = len(df[column])
            n_cat = df[column].nunique()
            perc_cardin = round(n_cat/n_observations * 100, 2)
            mode = df[column].mode()[0]
            w_mode = round(len(df[df[column] == df[column].mode()[0]]) / df.shape[0] * 100, 2)

            dict_cat[column] = [n_observations, n_cat, perc_cardin, mode, w_mode]

        table = pd.DataFrame(dict_cat)
        table.index = ['n_instances', 'n_categories', 'cardin (%)', 'mode', 'mode (%)']

    return table


def data_report(df):
    '''
    General data report.
    Parameters:
                - df: dataframe
    Output:
            Dataframe con:
                - Column name
                - Data type
                - % Missings 
                - % Cardinalidad 
    
    Libraries used:
        import pandas as pd
        import numpy as pd
    '''
    
    # COLUMN NAMES
    cols = pd.DataFrame(df.columns.values, columns = ['COL_N'])

    # COLUMNS TYPES
    types = pd.DataFrame(df.dtypes.values, columns = ['DATA_TYPE'])

    # MISSINGS --> df % nans per columns
    percent_missing = round(df.isnull().sum()*100 / len(df), 2)
    percent_missing_df = pd.DataFrame(percent_missing.values, columns = ['MISSINGS (%)'])
    
    # UNIQUE VALUES --> % unique values per column
    unicos = pd.DataFrame(df.nunique().values, columns = ['UNIQUE_VALUES'])

    percent_candin = round(unicos['UNIQUE_VALUES']*100 / len(df), 2)
    percent_candin_df = pd.DataFrame(percent_candin.values, columns = ['CARDIN (%)'])

    # Unimos
    concatenado = pd.concat([cols, types, percent_missing_df, unicos, percent_candin_df], axis = 1)
    concatenado.set_index('COL_N', drop = True, inplace = True)

    return concatenado.T