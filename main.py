import os
import pathlib
from tkinter.filedialog import askopenfilename

import UnityPy


def unpack_all_assets(source_path: str, destination_path: str):

    # load that file via UnityPy.load
    env = UnityPy.load(source_path)

    # iterate over internal objects
    for count, obj in enumerate(env.objects):

        # process specific object types
        if obj.type.name in ["Texture2D", "Sprite"]:

            # parse the object data
            data = obj.read()

            # create destination path
            dest = os.path.join(destination_path, f'extracted_{count}')

            # make sure that the extension is correct
            # you probably only want to do so with images/textures
            dest, ext = os.path.splitext(dest)
            dest = dest + f".png"

            img = data.image
            img.save(dest)


if __name__ == '__main__':
    path_input = pathlib.Path(askopenfilename(filetypes=[('Unity Bundles', '*.unity3d')]))
    if path_input.suffix.lower() == '.unity3d':
        unpack_all_assets(source_path=str(path_input), destination_path=str(path_input.parents[0]))

    else:
        raise Exception(f'Error: Invalid filetype {path_input.suffix.lower()}')
