def scoringfn(model, data, num_features = 7, nonzero = False, splines = False):
    # creating empty lists to save the scores
    train_scores = []
    test_scores = []
    
    if nonzero:
        data = data[data['log(area)'] != 0].reset_index()
    
    # splitting the data into target and features
    X, y = data.drop(columns = ['log(area)']), data['log(area)']
        
    # adding splines to the X and Y variables only
    if splines and type(LinearRegression()).__name__ == 'LinearRegression':
        spline = SplineTransformer()
        spline.fit(X[['X', 'Y']])
        xy_splined = pd.DataFrame(spline.transform(X[['X', 'Y']]), columns = spline.get_feature_names_out())
        X.drop(columns = ['X', 'Y'])
        X = pd.concat([xy_splined, X], axis = 1)
                         
        
    # splitting the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                       test_size = 0.25, random_state = 42)
    
    # scaling the data
    scaler = MinMaxScaler()
    scaler.fit(X_train)
    X_train = pd.DataFrame(scaler.transform(X_train), columns = scaler.get_feature_names_out())
    X_test = pd.DataFrame(scaler.transform(X_test), columns = scaler.get_feature_names_out())

    
    # initializing the feature selection process
    select = RFE(model, n_features_to_select = num_features)
    select.fit(X_train, y_train)
    print(f'features selected are:\n{X_train.columns[select.get_support()]}')
    
    X_train_selected = select.transform(X_train)
    X_test_selected = select.transform(X_test)
    
        
    # fitting the model and storing the scores
    linear = model.fit(X_train_selected, y_train)
    train_preds = linear.predict(X_train_selected)
    test_preds = linear.predict(X_test_selected)
    train_scores.append(r2_score(y_train, train_preds))
    test_scores.append(r2_score(y_test, test_preds))
    
    print(f'maximum R2 score on the training data: {np.max(train_scores)}')
    print(f'maximum R2 score on the testing data: {np.max(test_scores)}')