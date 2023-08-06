# %%
%load_ext autoreload
%autoreload 2
import sys
sys.path.append(r'C:\Program Files\DIgSILENT\PowerFactory 2022 SP1\Python\3.10')
import powerfactory as powerfactory

sys.path.append(r'D:\User\seberlein\Code\powerfactorypy\src')
import powerfactorypy 
import importlib
#importlib.reload(powerfactorypy)

import time
import statistics
from re import sub

app = powerfactory.GetApplication()
pfbi = powerfactorypy.PFBaseInterface(app)
pfbi.app.Show()
pfbi.app.ActivateProject(r'\seberlein\powerfactorypy_base')

# %%
terminal_1 = pfbi.get_obj(r"Network Model\Network Data\Grid\Terminal 1")
# %% 
project_folder = pfbi.app.GetActiveProject()
terminal_1 = pfbi.get_obj(r"Network Model\Network Data\Grid\Terminal 1",project_folder)

time_with_folder = []
time_without_folder = []
for i in range(9):
    start = time.perf_counter()
    terminal_1 = pfbi.get_obj(r"Ntwork Model\Network Data\Grid\Terminal 1",project_folder)
    time_with_folder.append(time.perf_counter() - start)

    start = time.perf_counter()
    terminal_1 = pfbi.get_obj(r"Network Model\Network Data\Grid\Terminal 1")
    time_without_folder.append(time.perf_counter() - start)

print(statistics.mean(time_with_folder))
print(statistics.mean(time_without_folder))
# %% 
pfbi.set_attr("Library\Dynamic Models\Linear_interpolation",{"sTitle":1})
pfbi.set_attr("Library\Dynamic Models\Linear_interpolation",
    {"sTitle":"Dummy title","des":"Dummy description"})
# %%
pfbi.get_attr("Library\Dynamic Models\Linear_interpolation",["sTile","desc"])
pfbi.get_attr("Library\Dynamic Models\Linear_interpolation",["sTitle","desc"])
# %%
pfbi.get_obj(r"\Libry\Dynamic Models\Linear_interpolation")
# %%
project_folder = pfbi.app.GetActiveProject()
powerfactorypy.PFStringManipuilation.delete_classes(str(project_folder))
# %%
pfbi.create_by_path("Library\Dynamic Models\dummy.BlkDef")
# %%
pfbi.create_by_path(4)
# %%
pfbi.create_in_folder(r"Library\Dynamic Models","dummy2.BlkDef")
pfbi.create_in_folder(r"Library\Dynamic Models",2)
# %%
contents1 = pfbi.get_from_folder(r"Network Model\Network Data\Grid\Voltage source ctrl")
contents2 = pfbi.get_from_folder(r"Network Model\Network Data\Grid\Voltage source ctrl",
    obj_name="Angle")
# %%
folder = r"Network Model\Network Data"
terminals = pfbi.get_from_folder(folder,obj_name="Terminal*",attr="uknom", 
    attr_lambda=lambda x : True)
# %%
