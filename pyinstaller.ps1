pyinstaller --noconfirm --onedir --console --add-binary "./venv/Lib/site-packages/onnxruntime/capi/onnxruntime_providers_shared.dll;./onnxruntime/capi" --add-data "./creep_server;creep_server/" --add-data "./creep_app;creep_app/" --add-data "./creep;creep/" --hidden-import "whitenoise" --hidden-import "whitenoise.storage" --hidden-import "whitenoise.middleware" --runtime-hook "./pyi_rth_django.py" "./manage.py"