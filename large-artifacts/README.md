# README

1. Modify the number of estimators of the random forest classifier in `large_rf.py`. 30K estimators yields a ~24GB joblib model object. 

2. Execute the script `large_rf.py` : 

```
nohup python -u large_rf.py > run-logs 2>&1 & 
```

The model will be saved as `rf.joblib`

3. If you want to deploy the model, runtime.yaml and score.py are found in the `model-artifact/ folder. Simply put `rf.joblib` in that folder, zip the content of the folder using: 

```
cd model-artifact/
zip artifact.zip * -0
```
4. Optionally upload the artifact to Object Storage using the OCI CLI: 

```
oci os object put --namespace <object_storage_namespace> --bucket-name <bucket_name> --file ./archive.zip --name archive.zip --parallel-upload-count 10 
```
(you may want to pick more parallel count for larger artifacts. 20 for a 24 GB artifact is good. 
