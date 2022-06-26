import sys
import os
from pydub import AudioSegment



def convert(file):
    """
    

    Parameters
    ----------
    file : TYPE
        DESCRIPTION.
    audformat : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    audio = AudioSegment.from_file(file)
    name = file.split("/")[-1]
    
    audio.export(directory+"/"+"Music/"+name, format="mp3")
    
    return



if __name__=="__main__":
    directory = '/'.join(__file__.split('/')[:-1])
    os.chdir(directory)
    try:
        os.mkdir("Music")
    except FileExistsError:
        pass
    path = sys.argv[1]
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".wma"):
                print("Converting: "+name)
                convert(path+'/'+name)
    print("Finished!")
    