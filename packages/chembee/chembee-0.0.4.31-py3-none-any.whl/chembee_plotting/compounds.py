from rdkit.Chem import Draw

def plot_compound_list(mols, file_name=, prefix=, suffix=): 

    Draw.MolsToGridImage(mols,molsPerRow=5,subImgSize=(200,200),legends=[x.GetProp("ReadyBiodegradability") + "    " + x.GetProp("Dataset") for x in mols])    
    Draw_m