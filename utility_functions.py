def split_data(data, fraction = 0.8):
    train_data = data.sample(frac = fraction, random_state = 42)
    test_data = data.drop(train_data.index)
    X_train, y_train = train_data.drop(columns = ['log(area)']), train_data['log(area)']
    X_test, y_test = test_data.drop(columns = ['log(area)']), test_data['log(area)']
    return (X_train, X_test, y_train, y_test)

def fit_evaluate(model, data):
    X_train, X_test, y_train, y_test = split_data(data)
    model.compile(optimizer = 'adam', loss = 'mean_squared_error')
    history = model.fit(X_train, y_train, epochs = 20, validation_split = 0.2, verbose = 0)
    print(f'training R2 score: {r2_score(y_train, model.predict(X_train)): .5f}')
    print(f'testing R2 score: {r2_score(y_test, model.predict(X_test)): .5f}')
    return history

def plot_scores(history):
    plt.figure(figsize = (8, 4))
    plt.plot(history.history['loss'], label = 'Loss')
    plt.plot(history.history['val_loss'], label = 'Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Values')
    plt.legend()