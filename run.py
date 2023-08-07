from mcl.app.ModelEngine import ModelEngine
import json

mEngine = ModelEngine("https://raw.githubusercontent.com/MaastrichtU-CDS/FAIRmodels/main/models/radiotherapy/stiphout_2011.ttl", libraryLocation="mcl/app")
modelExecutor = mEngine.getModelExecutor()

print("Model parameters:")
print(json.dumps(modelExecutor.getModelParameters(), indent=4))

print("===============================")
print(modelExecutor.executeModel({
    "https://raw.githubusercontent.com/MaastrichtU-CDS/FAIRmodels/main/models/radiotherapy/stiphout_2011.ttl#InputFeature_TLength": 3,
    "https://raw.githubusercontent.com/MaastrichtU-CDS/FAIRmodels/main/models/radiotherapy/stiphout_2011.ttl#InputFeature_cTStage": 2,
    "https://raw.githubusercontent.com/MaastrichtU-CDS/FAIRmodels/main/models/radiotherapy/stiphout_2011.ttl#InputFeature_cNStage": 1
}))