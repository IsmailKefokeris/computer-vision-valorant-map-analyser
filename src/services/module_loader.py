import importlib
import sys


def load_modules(mod_list=False):
    # LazyLoading for modules required depending on section
    if mod_list:
        local_vars = {}
        modules = [
            ('mss', 'mss_module = importlib.import_module("mss")'),
            ('cv2', 'cv = importlib.import_module("cv2")'),
            ('ultralytics', 'ultralytics = importlib.import_module("ultralytics"); YOLO = ultralytics.YOLO'),
            ('Annotator',
             'Annotator_module = importlib.import_module("ultralytics.yolo.utils.plotting"); Annotator = ultralytics.yolo.utils.plotting.Annotator'),
        ]
        for index, mod in enumerate(mod_list):
            if mod == True:
                mod_name, mod_code = modules[index]
                if mod_name not in sys.modules:
                    exec(mod_code, globals(), local_vars)
                else:
                    print(mod_name)
                    local_vars[mod_name] = sys.modules[mod_name]
                    print(f"{mod_name} exists")
        return local_vars["mss"], local_vars["cv2"], local_vars["ultralytics"], local_vars["YOLO"], local_vars["Annotator"]
    else:
        mss = importlib.import_module("mss")
        mss = mss.mss
        cv = importlib.import_module("cv2")
        ultralytics = importlib.import_module("ultralytics")
        YOLO = ultralytics.YOLO
        Annotator = importlib.import_module(
            "ultralytics.yolo.utils.plotting")
        Annotator = Annotator.Annotator
        return mss, cv, ultralytics, YOLO, Annotator
