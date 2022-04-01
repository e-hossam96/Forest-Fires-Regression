class Evaluate_Model():
    def __init__(self, model, data):
        self.model = model
        self.data = data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            data.drop(['log(area)'], axis = 1), data['log(area)'], random_state = 42)
    def cross_validate_model(self, cv):
        scores = cross_val_score(model, self.data.drop(columns = ['log(area)']), self.data['log(area)'], cv = cv)
        print(f'max R2 score: {np.max(scores): .6f}')
        print(f'mean R2 score: {np.mean(scores): .6f}')
        print(f'min R2 score: {np.min(scores): .6f}')
    def evaluate_model(self):
        self.model.fit(self.X_train, self.y_train)
        train_preds = model.predict(self.X_train)
        test_preds = model.predict(self.X_test)
        print(f'R2 score on training set: {r2_score(self.y_train, train_preds): .6f}')
        print(f'R2 score on  testing set: {r2_score(self.y_test, test_preds): .6f}')