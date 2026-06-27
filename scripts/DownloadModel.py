from vosk import Model, SetLogLevel

SetLogLevel(-1)

model = Model(model_path=r"C:\Workship\PythonApp\assistent\model\vosk-model-small-ru-0.22", lang="ru")