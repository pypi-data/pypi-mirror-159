PIPELINE_UID_XCOM='pipeline_uid_ff069534-5069-45b1-b737-aea6229db4bf'


def get_dag_run_pipeline_run_id(task_instance):
    return task_instance.xcom_pull(key=f'{task_instance.dag_id}_pipeline_run_id')
