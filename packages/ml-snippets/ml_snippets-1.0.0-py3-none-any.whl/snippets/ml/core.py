import mlflow

def experiment(expr_name):
    if mlflow.get_experiment_by_name(expr_name) is None:
        mlflow.create_experiment(expr_name)
        mlflow.set_experiment(expr_name)
    mlflow.end_run()
    mlflow.start_run()
    
def params(params,value):
    mlflow.log_params(params,value)
    
def metrics(metrics,value):
    mlflow.log_metrics(metrics,value)
    
def artifacts(artifacts):
    mlflow.log_artifacts(artifacts)
    
def tags(tags):
    mlflow.set_tags(tags)
    