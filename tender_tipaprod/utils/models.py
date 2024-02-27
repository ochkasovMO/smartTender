from sklearn.metrics import roc_auc_score, f1_score, accuracy_score, precision_score, recall_score, confusion_matrix, ConfusionMatrixDisplay
def display_results(model, y_test, preds):
    roc = roc_auc_score(y_test, preds)
    prec = precision_score(y_test, preds)
    recall = recall_score(y_test, preds)
    f1 = f1_score(y_test, preds)
    accuracy = accuracy_score(y_test, preds)
    print('ROC AUC: ', roc)
    print('F1 score: ', f1)
    print('Accuracy: ', accuracy)
    print('Precision: ', prec)
    print('Recall: ', recall)
    cm = confusion_matrix(y_test, preds, labels=[0,1])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[0,1])
    disp.plot()
    for i in range(len(model.feature_names_in_)):
        print(model.feature_names_in_[i],' : ',model.feature_importances_[i])